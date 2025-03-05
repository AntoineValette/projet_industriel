from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

from filtrage_logs_server import get_ping_filtered, get_ram_filtered, get_reseau_filtered,get_memoire_filtered, get_sql_lock_filtered, get_swap_filtered, get_sql_statistic_filtered, get_storage_filtered, get_sql_general_filetered
from db_utils import get_db_connection
from functools import reduce
from filtrage_logs_server import get_cpu_filtered

# Paramètres par défaut du DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définition du DAG qui s'exécute toutes les heures
dag = DAG(
    'hourly_etl_job',
    default_args=default_args,
    description='ETL : extraction des dernières 60 min de chaque table, traitement, et écriture dans la table dataset',
    schedule='@hourly',
    catchup=False,
    is_paused_upon_creation=True  # Le DAG sera inactif dès sa création = à modifier pour prod
)


def get_df(since: datetime, table: str) -> pd.DataFrame:
    """
    Fonction pour requêter la base postgres et renvoyer un dataframe correspondant
    """
    with get_db_connection() as conn:
        # Vous pouvez utiliser pd.read_sql pour simplifier
        query = f"SELECT * FROM {table} WHERE dt_insertion >= '{since.isoformat()}'"
        df = pd.read_sql(query, conn)
    return df


def fusion_horaire():
    now = datetime.now()
    since = now - timedelta(minutes=60)

    """chargelent des données depuis Postgres"""
    df_logOk = get_df(since, "logOK")
    df_logErr = get_df(since, "logERR")

    df_ping = get_ping_filtered(get_df(since, "myreport_ping"))
    df_cpu = get_cpu_filtered(get_df(since, "myreport_cpu"))
    df_ram = get_ram_filtered(get_df(since, "myreport_ram"))
    df_reseau = get_reseau_filtered(get_df(since, "myreport_reseau"))
    df_sql_management_storage = get_memoire_filtered(get_df(since, "myreport_memoire"))
    df_sql_lock = get_sql_lock_filtered(get_df(since, "myreport_sql_lock"))
    df_swap = get_swap_filtered(get_df(since, "myreport_swap"))
    df_sql_statistic = get_sql_statistic_filtered(get_df(since, "myreport_sql_statistic"))
    df_storage = get_storage_filtered(get_df(since, "myreport_espace_disque"))
    df_sql_general = get_sql_general_filetered(get_df(since, "myreport_sql_general"))

    print("-----------importation des dataframes terminée-----------")

    """préparation de df_logERR"""
    # Conversion de la colonne ETL_StartDateTime en Datetime pandas
    df_logErr['etl_start_datetime'] = pd.to_datetime(df_logErr['etl_start_datetime'], format="%Y-%m-%d %H:%M:%S")
    # Ajout d'une colonne Date et heure ne tenant pas compte des minutes
    df_logErr["Date et heure"] = df_logErr["etl_start_datetime"].dt.floor("h")


    print("-----------préparation de logERR terminée-----------")

    """Utiliser des crosstab (ou pivot) et joindre les DataFrames"""
    # Comptage des catégories par Date et heure
    df_cat = pd.crosstab(df_logErr["Date et heure"], df_logErr["type_error"])
    # Comptage des programmes par Date et heure
    df_prog = pd.crosstab(df_logErr["Date et heure"], df_logErr["program_name"])
    # Joindre les deux sur l'index (qui est "Date et heure" dans les 2 crosstabs)
    df_error_grouped2 = df_cat.join(df_prog, how="outer")
    # Remettre "Date et heure" en colonne si besoin
    df_error_grouped2 = df_error_grouped2.reset_index()

    print("-----------transformation/enrichissement de logERR terminée-----------")

    # sommer le nb d'erreurs dans les colonnes erreur pour la vérification
    error_columns = [col for col in df_error_grouped2.columns if "Error" in col]
    df_error_grouped2["Total_Errors"] = df_error_grouped2[error_columns].sum(axis=1)

    """préparation de df_logOK"""
    # Conversion de la colonne ETL_StartDateTime en Datetime pandas
    df_logOk['etl_startdatetime'] = pd.to_datetime(df_logOk['etl_startdatetime'], format="%d/%m/%Y %H:%M")

    """Réduction du df pour qu'il soit dans la bonne période ==>> SUPPRIMER CA POUR MISE EN PROD"""
    """
    start_date = df_logErr['etl_start_datetime'].min()
    end_date = df_logErr['etl_start_datetime'].max()
    df_reduced = df_logOk[(df_logOk['etl_startdatetime'] >= start_date) & (df_logOk['etl_startdatetime'] <= end_date)]
    """
    df_reduced = df_logOk

    """suite de la préparation de df_logOK"""
    # Ajout d'une colonne Date et heure ne tenant pas compte des minutes
    df_reduced.loc[:, "Date et heure"] = df_reduced["etl_startdatetime"].dt.floor("h")
    df_grouped = df_reduced.groupby("Date et heure").agg(
        nb_operations=("insert_mode", "count"),  # Nombre total de lignes dans l'heure
        rows_added=("rows_added", "sum"),  # Somme des lignes ajoutées
        rows_updated=("rows_updated", "sum"),  # Somme des mises à jour
        rows_deleted=("rows_deleted", "sum")  # Somme des suppressions
    ).reset_index()

    print("-----------préparation de logOK terminée-----------")

    """fusion des log ok et log erreur"""
    df_final = df_error_grouped2.merge(
        df_grouped,
        on="Date et heure",
        how="outer",
    )

    # Changement des valeurs NaN en 0
    df_final = df_final.fillna(0)

    print("-----------fusion de logERR et logOK terminée-----------")

    """Fusion des DF de stat server"""
    dfs = [df_reseau, df_sql_statistic, df_sql_lock, df_sql_general, df_ping, df_storage, df_swap,
           df_sql_management_storage, df_ram, df_cpu]
    df_server_stats = reduce(lambda left, right: pd.merge(left, right, on="date_heure", how="outer"), dfs)

    df_server_stats['Date et heure'] = pd.to_datetime(df_server_stats['date_heure'])

    print("-----------fusion des dataframes des logs servers terminée-----------")

    # Fusion des deux df conso
    df_global = df_final.merge(
        df_server_stats,
        on="Date et heure",
        how="outer",
    )
    df_global = df_global.fillna(0)

    print("-----------fusion de globale terminée-----------")

    df_global = df_global.drop(columns='date_heure')

    """enregistrement"""
    with get_db_connection() as conn:
        df_global.to_sql("dataset", if_exists='append', index=False, con=conn)
    
    print("-----------enregistrement terminée-----------")


# Définition du PythonOperator pour exécuter le job ETL
etl_task = PythonOperator(
    task_id='hourly_etl_task',
    python_callable=fusion_horaire,
    dag=dag
)
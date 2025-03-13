import pandas as pd
from datetime import datetime
from functools import reduce
from dags.classification_error import dorErrorDict, dorProgrammDict, categorize_programm
from dags.filtrage_logs_server import get_ping_filtered, get_ram_filtered, get_reseau_filtered,get_memoire_filtered, get_sql_lock_filtered, get_swap_filtered, get_sql_statistic_filtered, get_storage_filtered, get_sql_general_filetered
from dags.db_utils import get_db_connection
from dags.filtrage_logs_server import get_cpu_filtered

def get_df(table: str) -> pd.DataFrame:
    """
    Fonction pour requêter la base postgres et renvoyer un dataframe correspondant
    """
    with get_db_connection() as conn:
        # Récupérer toutes les données depuis le début de l'historique
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, conn)
    return df

def create_historical_dataset():
    now = datetime.now()
    end_time = now.replace(minute=0, second=0, microsecond=0)

    """Chargement des données depuis Postgres"""
    df_logOk = get_df("logOK")
    df_logErr = get_df("logERR")

    df_ping = get_ping_filtered(get_df("myreport_ping"))
    df_cpu = get_cpu_filtered(get_df("myreport_cpu"))
    df_ram = get_ram_filtered(get_df("myreport_ram"))
    df_reseau = get_reseau_filtered(get_df("myreport_reseau"))
    df_sql_management_storage = get_memoire_filtered(get_df("myreport_memoire"))
    df_sql_lock = get_sql_lock_filtered(get_df("myreport_sql_lock"))
    df_swap = get_swap_filtered(get_df("myreport_swap"))
    df_sql_statistic = get_sql_statistic_filtered(get_df("myreport_sql_statistic"))
    df_storage = get_storage_filtered(get_df("myreport_espace_disque"))
    df_sql_general = get_sql_general_filetered(get_df("myreport_sql_general"))

    print("-----------importation des dataframes terminée-----------")

    """Préparation de df_logERR"""
    df_logErr['etl_start_datetime'] = pd.to_datetime(df_logErr['etl_start_datetime'], format="%Y-%m-%d %H:%M:%S")
    df_logErr["date_and_heure"] = df_logErr["etl_start_datetime"].dt.floor("h")

    df_logErr['program_name'] = df_logErr['program_name'].apply(categorize_programm)

    print("-----------préparation de logERR terminée-----------")

    """Utiliser des crosstab (ou pivot) et joindre les DataFrames"""
    df_cat = pd.crosstab(df_logErr["date_and_heure"], df_logErr["type_error"])

    for error in dorErrorDict.keys():
        if error not in df_cat.columns:
            df_cat[error] = 0

    df_prog = pd.crosstab(df_logErr["date_and_heure"], df_logErr["program_name"])

    for old, new in dorProgrammDict.items():
        if old not in df_prog.columns and old != "":
            df_prog[old] = 0

    df_error_grouped2 = df_cat.join(df_prog, how="outer").reset_index()

    print("-----------transformation/enrichissement de logERR terminée-----------")

    error_columns = [col for col in df_error_grouped2.columns if "Error" in col]
    df_error_grouped2["Total_Errors"] = df_error_grouped2[error_columns].sum(axis=1)

    """Préparation de df_logOK"""
    df_logOk['etl_start_datetime'] = pd.to_datetime(df_logOk['etl_start_datetime'], format="%d/%m/%Y %H:%M")
    df_logOk["date_and_heure"] = df_logOk["etl_start_datetime"].dt.floor("h")

    df_grouped = df_logOk.groupby("date_and_heure").agg(
        nb_operations=("insert_mode", "count"),
        rows_added=("rows_added", "sum"),
        rows_updated=("rows_updated", "sum"),
        rows_deleted=("rows_deleted", "sum")
    ).reset_index()

    print("-----------préparation de logOK terminée-----------")

    """Fusion des log ok et log erreur"""
    df_final = df_error_grouped2.merge(df_grouped, on="date_and_heure", how="outer").fillna(0)

    print("-----------fusion de logERR et logOK terminée-----------")

    """Fusion des DF de stat server"""
    dfs = [df_reseau, df_sql_statistic, df_sql_lock, df_sql_general, df_ping, df_storage, df_swap,
           df_sql_management_storage, df_ram, df_cpu]
    df_server_stats = reduce(lambda left, right: pd.merge(left, right, on="date_heure", how="outer"), dfs)
    df_server_stats['date_and_heure'] = pd.to_datetime(df_server_stats['date_heure'])

    print("-----------fusion des dataframes des logs servers terminée-----------")

    # Fusion des deux df conso
    df_global = df_final.merge(df_server_stats, on="date_and_heure", how="outer").fillna(0)
    df_global = df_global.drop(columns='date_heure')
    df_global.columns = df_global.columns.str.lower()

    print("-----------fusion globale terminée-----------")

    # Trier le DataFrame par date_and_heure
    df_global = df_global.sort_values(by="date_and_heure")

    """Enregistrement"""
    with get_db_connection() as conn:
        df_global[df_global["date_and_heure"] < end_time].to_sql("dataset", if_exists='append', index=False, con=conn)

    print("-----------enregistrement terminé-----------")

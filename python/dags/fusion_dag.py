from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from classification_error import dorErrorDict, dorProgrammDict, categorize_programm
from filtrage_logs_server import (
    get_ping_filtered, get_cpu_filtered, get_ram_filtered, get_reseau_filtered,
    get_memoire_filtered, get_sql_lock_filtered, get_swap_filtered,
    get_sql_statistic_filtered, get_storage_filtered, get_sql_general_filetered
)
from db_utils import get_db_connection
from functools import reduce
import os
import pytz

start_date_str = os.getenv('START_DATE', '2025-03-11T00:00:00')
start = datetime.fromisoformat(start_date_str)

# Paramètres par défaut du DAG
default_args = {
    'owner': 'airflow',
    'start_date': start,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définition du DAG qui s'exécute toutes les heures
dag = DAG(
    'hourly_etl_job',
    default_args=default_args,
    description='ETL horaire : extraction des 60 dernières minutes de chaque table, traitement et écriture dans "dataset"',
    schedule_interval='3 * * * *',
    catchup=False,
    is_paused_upon_creation=True
)

def get_df(since: datetime, until: datetime, table: str) -> pd.DataFrame:
    with get_db_connection() as conn:
        if table in ["logOK", "logERR"]:
            query = f"""
                SELECT * FROM {table}
                WHERE etl_start_datetime >= '{since.isoformat()}'
                AND etl_start_datetime < '{until.isoformat()}'
            """
        else:
            query = f"""
                SELECT * FROM {table}
                WHERE date_heure >= '{since.isoformat()}'
                AND date_heure < '{until.isoformat()}'
            """
        df = pd.read_sql(query, conn)

    if df.empty:
        print(f"⚠️ Aucune donnée trouvée pour {table} entre {since} et {until}.")
        if table in ["logOK", "logERR"]:
            return pd.DataFrame(columns=["etl_start_datetime", "program_name", "type_error"])
        else:
            return pd.DataFrame(columns=["date_heure"])

    return df

def fusion_horaire(data_interval_start, data_interval_end):
    # Définition des timezones
    cet = pytz.timezone('Europe/Paris')

    # Vérifie si les intervalles sont des chaînes et les convertit uniquement si nécessaire
    if isinstance(data_interval_start, str):
        data_interval_start = datetime.fromisoformat(data_interval_start)  # Déjà en UTC
    if isinstance(data_interval_end, str):
        data_interval_end = datetime.fromisoformat(data_interval_end)  # Déjà en UTC

    # Conversion vers CET (Europe/Paris)
    data_interval_start = data_interval_start.astimezone(cet)
    data_interval_end = data_interval_end.astimezone(cet)

    start_of_last_hour = data_interval_start
    end_of_last_hour = data_interval_end

    df_logOk = get_df(start_of_last_hour, end_of_last_hour, "logOK")
    df_logErr = get_df(start_of_last_hour, end_of_last_hour, "logERR")

    tables_functions = {
        "myreport_ping": get_ping_filtered,
        "myreport_cpu": get_cpu_filtered,
        "myreport_ram": get_ram_filtered,
        "myreport_reseau": get_reseau_filtered,
        "myreport_memoire": get_memoire_filtered,
        "myreport_sql_lock": get_sql_lock_filtered,
        "myreport_swap": get_swap_filtered,
        "myreport_sql_statistic": get_sql_statistic_filtered,
        "myreport_espace_disque": get_storage_filtered,
        "myreport_sql_general": get_sql_general_filetered
    }

    df_dict = {}
    for table, filter_func in tables_functions.items():
        df = get_df(start_of_last_hour, end_of_last_hour, table)
        if not df.empty:
            df = filter_func(df)
        df_dict[table] = df

    if df_logOk.empty and df_logErr.empty and all(df.empty for df in df_dict.values()):
        print("⚠️ Aucune donnée disponible dans aucune table. Fin du traitement.")
        return

    print("✅ Importation des DataFrames terminée.")

    df_logErr['etl_start_datetime'] = pd.to_datetime(df_logErr['etl_start_datetime'], format="%Y-%m-%d %H:%M:%S")
    df_logErr["date_and_heure"] = df_logErr["etl_start_datetime"].dt.floor("h")
    df_logErr['program_name'] = df_logErr['program_name'].apply(categorize_programm)

    df_cat = pd.crosstab(df_logErr["date_and_heure"], df_logErr["type_error"])
    for error in dorErrorDict:
        if error not in df_cat.columns:
            df_cat[error] = 0

    df_prog = pd.crosstab(df_logErr["date_and_heure"], df_logErr["program_name"])
    for prog in dorProgrammDict:
        if prog not in df_prog.columns and prog != "":
            df_prog[prog] = 0

    df_errors = df_cat.join(df_prog, how="outer").reset_index()
    print("✅ Préparation de logERR terminée.")

    df_logOk['etl_start_datetime'] = pd.to_datetime(df_logOk['etl_start_datetime'], format="%d/%m/%Y %H:%M")
    df_logOk["date_and_heure"] = df_logOk["etl_start_datetime"].dt.floor("h")
    df_logOk_grouped = df_logOk.groupby("date_and_heure").agg(
        nb_operations=("insert_mode", "count"),
        rows_added=("rows_added", "sum"),
        rows_updated=("rows_updated", "sum"),
        rows_deleted=("rows_deleted", "sum")
    ).reset_index()
    print("✅ Préparation de logOK terminée.")

    df_logs = df_errors.merge(df_logOk_grouped, on="date_and_heure", how="outer").fillna(0)

    df_server_stats = reduce(lambda l, r: pd.merge(l, r, on="date_heure", how="outer"), df_dict.values())
    df_server_stats = df_server_stats.rename(columns={'date_heure': 'date_and_heure'})
    df_server_stats['date_and_heure'] = pd.to_datetime(df_server_stats['date_and_heure'])
    print("✅ Fusion des logs serveurs terminée.")

    df_global = df_logs.merge(df_server_stats, on="date_and_heure", how="outer").fillna(0)
    df_global.columns = df_global.columns.str.lower()
    print("✅ Fusion globale terminée.")

    with get_db_connection() as conn:
        existing_dates = pd.read_sql("SELECT date_and_heure FROM dataset", conn)
        new_rows = df_global[~df_global['date_and_heure'].isin(existing_dates['date_and_heure'])]

        if not new_rows.empty:
            new_rows.to_sql("dataset", if_exists='append', index=False, con=conn)
            print("✅ Nouvelles lignes insérées dans la table dataset.")
        else:
            print("⚠️ Aucune nouvelle ligne à insérer.")


etl_task = PythonOperator(
    task_id='hourly_etl_task',
    python_callable=fusion_horaire,
    op_kwargs={
        'data_interval_start': '{{ data_interval_start }}',
        'data_interval_end': '{{ data_interval_end }}'
    },
    dag=dag
)
import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def importLogETL():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(
        host=Settings.POSTGRES_HOST,
        database=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
    )
    cur = conn.cursor()

    log("import de 241016_LogETL")
    filename = "/data/logETL/241016_LogETL.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO logOK (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_Id, launcher_Name, program_id,program_name, schedules_id, schedules_name, schedules_startdatetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
        log("import de 241016_LogETL [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")


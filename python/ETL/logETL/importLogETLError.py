import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def importLogETLerror():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(
        host=Settings.POSTGRES_HOST,
        database=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
    )
    cur = conn.cursor()

    log("import de 241016_LogETLError")
    filename = "/data/logETL/241016_LogETLError.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
        log("import de 241016_LogETLError [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")


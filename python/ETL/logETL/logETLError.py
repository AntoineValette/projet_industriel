import csv
import os
import psycopg2

from core.log import log
from core.settings import Settings

def logEtlError():
    filename = "/data/logETL/241016_LogETLError.csv"
    if os.path.isfile(filename):
        log("Connexion à PostgreSQL")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract de 241016_LogETLError")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
        log("+-- extract de 241016_LogETLError [ok]")
        conn.commit()
        cur.close()

        log("+-- transform 241016_LogETLError ...")
        log("+-- load 241016_LogETLError ...")

        conn.close()
        log("PostgreSQL - close")

from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime
import sys
from core.settings import settings
import os


def log(msg):
    print(f"[{datetime.now()}] {msg}", flush=True)
    sys.stdout.flush()  # Force l'affichage immédiat

def consummer():
    conn = psycopg2.connect(settings.POSTGRES_URL)
    cur = conn.cursor()

    consumer = KafkaConsumer(
        'logOK_topic', 'logERR_topic',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id='log_consumer_group'
    )

    for message in consumer:
        data = message.value
        if data == "Fin de l'import historique":
            if message.topic == "logOK_topic":
                if not os.path.exists("/shared/historique_import_complete_LogETL.txt"):
                    with open("/shared/historique_import_complete_LogETL.txt", 'w') as f:
                        f.write("Historique importé avec succès.")
                        log("Fin de l'importation historique, fichier signal logOK créé.")
            elif message.topic == "logERR_topic":
                log("etape 2")
                if not os.path.exists("/shared/historique_import_complete_LogETLError.txt"):
                    with open("/shared/historique_import_complete_LogETLError.txt", 'w') as f:
                        f.write("Historique importé avec succès.")
                        log("Fin de l'importation historique, fichier signal logERR créé.")
        else:
            if message.topic == 'logOK_topic':
                cur.execute("""
                    INSERT INTO logOK (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_Id, launcher_Name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, tuple(data.values()))

            if message.topic == 'logERR_topic':
                cur.execute("""
                    INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, tuple(data.values()))

        conn.commit()

    cur.close()
    conn.close()

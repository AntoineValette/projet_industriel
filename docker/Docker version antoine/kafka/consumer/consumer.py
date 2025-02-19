from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime

def log(msg):
    print(f"[{datetime.now()}] {msg}")

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="supever",
    password="DORsupever2025"
)
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
    if message.topic == 'logOK_topic':
        cur.execute("""
            INSERT INTO logOK (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_Id, launcher_Name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(data.values()))
        log("Inséré dans logOK")

    elif message.topic == 'logERR_topic':
        cur.execute("""
            INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(data.values()))
        log("Inséré dans logERR")

    conn.commit()

cur.close()
conn.close()

import csv
import os
import psycopg2
from datetime import datetime

from core.log import log
from core.settings import Settings

def myreport_cpu():
    filename = "/data/logServer/myreport_cpu_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_cpu")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                # Conversion de la première colonne en date
                date_heure_str = row[reader.fieldnames[0]]
                date_heure = date_heure_str.split(" - ")[0]
                row['Date et heure'] = datetime.strptime(date_heure, "%d/%m/%Y %H:%M:%S")
                cur.execute("""
            INSERT INTO myreport_cpu (
             	date_heure,date_heure_raw,
                Somme, Somme_RAW, 
                Processeur_1, Processeur_1_RAW, Processeur_2, Processeur_2_RAW, 
                Processeur_3, Processeur_3_RAW, Processeur_4, Processeur_4_RAW, 
                Processeur_5, Processeur_5_RAW, Processeur_6, Processeur_6_RAW, 
                Processeur_7, Processeur_7_RAW, Processeur_8, Processeur_8_RAW, 
                Temps_mort_cpu, Temps_mort_cpu_RAW, Couverture_cpu, Couverture_cpu_RAW
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
            """, tuple(row.values()))
        log("+-- extract myreport_cpu [ok]")
        conn.commit()
        cur.close()

        log("+-- transform myreport_cpu ...")
        log("+-- load myreport_cpu ...")

        conn.close()
        log("PostgreSQL - close")

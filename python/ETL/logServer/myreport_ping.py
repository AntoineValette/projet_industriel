import csv
import os
import psycopg2
from datetime import datetime

from core.log import log
from core.settings import Settings

def myreport_ping():
    filename = "/data/logServer/myreport_ping_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_ping")
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
                cur.execute("""INSERT INTO myreport_ping (
                                date_heure,date_heure_raw,
                                temps_du_ping, temps_du_ping_raw, 
                                minimum, minimum_raw, maximum, maximum_raw, 
                                perte_de_paquets, perte_de_paquets_raw, temps_mort, temps_mort_raw, 
                                couverture, couverture_raw) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                            , tuple(row.values()))
        log("+-- extract myreport_ping [ok]")
        conn.commit()
        cur.close()

        log("+-- transform myreport_ping ...")
        log("+-- load myreport_ping ...")

        conn.close()
        log("PostgreSQL - close")

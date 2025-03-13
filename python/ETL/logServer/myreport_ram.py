import csv
import os
import psycopg2
from datetime import datetime

from core.log import log
from core.settings import Settings

def myreport_ram():
    filename = "/data/logServer/myreport_ram_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_ram")
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
                    INSERT INTO myreport_ram (
                        date_heure,date_heure_raw, 
                        memoire_disponible_pct, 
                        memoire_disponible_pct_RAW, 
                        memoire_disponible_go, 
                        memoire_disponible_go_RAW, 
                        temps_mort_pct, 
                        temps_mort_raw, 
                        couverture_pct, 
                        couverture_raw
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s
                    )
                """, tuple(row.values()))
        log("+-- extract myreport_ram [ok]")
        conn.commit()
        cur.close()

        log("+-- transform myreport_ram ...")
        log("+-- load myreport_ram ...")

        conn.close()
        log("PostgreSQL - close")

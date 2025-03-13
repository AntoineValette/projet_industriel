import csv
import os
import psycopg2
from datetime import datetime

from core.log import log
from core.settings import Settings

def myreport_sql_general():
    filename = "/data/logServer/myreport_sql_general_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_sql_general")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)  # Passer la ligne d'en-tête si nécessaire
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
                    INSERT INTO myreport_sql_general (
                        date_heure,date_heure_raw, 
                        Connexions_user, 
                        Connexions_user_raw, 
                        Connexions, 
                        Connexions_Raw, 
                        Déconnexions, 
                        Déconnexions_raw, 
                        temp_mort, 
                        temp_mort_raw, 
                        Couverture, 
                        Couverture_raw
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )
                """, tuple(row.values()))
        log("+-- extract myreport_sql_general [ok]")
        conn.commit()
        cur.close()

        log("+-- transform myreport_sql_general ...")
        log("+-- load myreport_sql_general ...")

        conn.close()
        log("PostgreSQL - close")

import csv
import os
import psycopg2
from datetime import datetime

from core.log import log
from core.settings import Settings

def myreport_swap():
    filename = "/data/logServer/myreport_swap_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_swap")
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
                cur.execute("""INSERT INTO myreport_swap (
                        date_heure,date_heure_raw,
                        Total, 
                        Total_RAW, 
                        temps_mort_mem, 
                        temps_mort_mem_RAW,
                        couverture_mem, 
                        couverture_mem_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )""", tuple(row.values()))
        log("+-- extract myreport_swap [ok]")
        conn.commit()
        cur.close()

        # transform
        log("+-- transform myreport_swap ...")
        log("+-- load myreport_swap ...")

        conn.close()
        log("PostgreSQL - close")

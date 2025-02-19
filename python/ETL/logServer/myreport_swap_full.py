import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def import_myreport_swap_full():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(Settings.POSTGRES_URL)
    cur = conn.cursor()

    log("import de myreport_swap_full")
    filename = "/data/logServer/myreport_swap_full.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""INSERT INTO myreport_swap (
                        date_heure, 
                        date_heure_RAW, 
                        Total, 
                        Total_RAW, 
                        temps_mort_mem, 
                        temps_mort_mem_RAW,
                        couverture_mem, 
                        couverture_mem_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )
                """, tuple(row.values()))
        log("import de myreport_swap_full [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")
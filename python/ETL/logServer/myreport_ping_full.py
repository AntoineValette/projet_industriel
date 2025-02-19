import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def import_myreport_ping_full():
    filename = "/data/logServer/myreport_ping_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("extract myreport_ping_full")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)  # Passer la ligne d'en-tête si nécessaire
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""INSERT INTO myreport_ping (
                                date_heure,date_heure_raw,
                                temps_du_ping, temps_du_ping_raw, 
                                minimum, minimum_raw, maximum, maximum_raw, 
                                perte_de_paquets, perte_de_paquets_raw, temps_mort, temps_mort_raw, 
                                couverture, couverture_raw) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                            , tuple(row.values()))
        log("extract myreport_ping_full [ok]")
        conn.commit()
        cur.close()

        log("transform myreport_ping_full ...")
        log("load myreport_ping_full ...")

        conn.close()
        log("PostgreSQL - close")

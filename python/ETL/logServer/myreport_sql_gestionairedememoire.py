import csv
import os
import psycopg2

from core.log import log
from core.settings import Settings

def myreport_sql_gestionairedememoire():
    filename = "/data/logServer/myreport_sql_gestionairedememoire_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_sql_gestionairedememoire")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""
                    INSERT INTO myreport_memoire (
                        date_heure,date_heure_raw, 
                        MemConnexion, 
                        MemConnexion_RAW, 
                        MemOptimiseur, 
                        MemOptimiseur_RAW, 
                        MemTotaleServeur, 
                        MemTotaleServeur_RAW, 
                        MemServeurCible, 
                        MemServeurCible_RAW, 
                        MemeCacheSQL, 
                        MemeCacheSQL_RAW, 
                        Temps_mort_mem, 
                        Temps_mort_mem_RAW, 
                        Couverture_mem, 
                        Couverture_mem_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )""", tuple(row.values()))
        log("+-- extract myreport_sql_gestionairedememoire [ok]")
        conn.commit()
        cur.close()

        log("+-- transform myreport_sql_gestionairedememoire ...")
        log("+-- load myreport_sql_gestionairedememoire ...")

        conn.close()
        log("PostgreSQL - close")

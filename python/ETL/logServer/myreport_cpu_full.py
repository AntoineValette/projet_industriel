import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def importLogETLerror():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(
        host=Settings.POSTGRES_HOST,
        database=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
    )
    cur = conn.cursor()

    log("import de myreport_cpu_full")
    filename = "/data/logServer/myreport_cpu_full.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""
            INSERT INTO myreport_cpu (
                Date, heureDate_RAW, Somme, Somme_RAW, 
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
        log("import de myreport_cpu_full [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")
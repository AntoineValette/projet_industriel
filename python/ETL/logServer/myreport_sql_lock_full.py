import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def import_myreport_sql_lock_full():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(Settings.POSTGRES_URL)
    cur = conn.cursor()

    log("import de myreport_sql_lock_full")
    filename = "/data/logServer/myreport_sql_lock_full.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)  # Passer la ligne d'en-tête si nécessaire
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""
                    INSERT INTO myreport_sql_lock (
                        date_heure, 
                        date_heure_RAW, 
                        nombre_requetes_verrouillage, 
                        nombre_requetes_verrouillage_RAW, 
                        temps_attente_moyen, 
                        temps_attente_moyen_RAW, 
                        nombre_blocages, 
                        nombre_blocages_RAW, 
                        temps_mort, 
                        temps_mort_RAW, 
                        couverture, 
                        couverture_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )
                """, tuple(row.values()))
            log("import de myreport_sql_lock_full [ok]")
            conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")
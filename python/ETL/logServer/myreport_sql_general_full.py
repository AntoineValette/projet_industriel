import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def import_myreport_sql_general_full():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(Settings.POSTGRES_URL)
    cur = conn.cursor()


    log("import de myreport_sql_general_full")
    filename = "/data/logServer/myreport_sql_general_full.csv"
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
                    INSERT INTO myreport_sql_general (
                        date_heure, 
                        date_heure_raw, 
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
        log("import de myreport_sql_general_full [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")
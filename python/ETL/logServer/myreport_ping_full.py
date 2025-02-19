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

    log("import de myreport_ping_full")
    filename = "/data/logServer/myreport_ping_full.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)  # Passer la ligne d'en-tête si nécessaire
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("INSERT INTO myreport_ping (date_et_heure, date_et_heure_raw, temps_du_ping, temps_du_ping_raw, minimum, minimum_raw, maximum, maximum_raw, perte_de_paquets, perte_de_paquets_raw, temps_mort, temps_mort_raw, couverture, couverture_raw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
        log("import de myreport_ping_full [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")
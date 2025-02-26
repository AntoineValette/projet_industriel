import time

import psycopg2

from core.log import log
from core.settings import Settings


# Fonction pour vérifier la connexion
def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(Settings.POSTGRES_URL)
            conn.close()
            log("PostgreSQL est prêt !")
            break
        except psycopg2.OperationalError:
            log("Attente de PostgreSQL...")
            time.sleep(2)

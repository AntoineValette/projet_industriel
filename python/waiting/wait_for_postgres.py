import time

import psycopg2

from core.log import log
from core.settings import settings


# Fonction pour vérifier la connexion
def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(settings.POSTGRES_URL)
            conn.close()
            print(settings.POSTGRES_URL)
            log("PostgreSQL est prêt !")
            break
        except psycopg2.OperationalError:
            log("Attente de PostgreSQL...")
            print(settings.POSTGRES_URL)

            time.sleep(2)

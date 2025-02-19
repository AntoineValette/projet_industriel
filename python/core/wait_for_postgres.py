import psycopg2
import time
from core.settings import Settings

# Fonction pour vérifier la connexion
def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=Settings.POSTGRES_HOST,
                database=Settings.POSTGRES_DB,
                user=Settings.POSTGRES_USER,
                password=Settings.POSTGRES_PASSWORD,
            )
            conn.close()
            print("PostgreSQL est prêt !")
            break
        except psycopg2.OperationalError:
            print("Attente de PostgreSQL...")
            time.sleep(2)

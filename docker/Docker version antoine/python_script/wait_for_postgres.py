import psycopg2
import time

# Configuration de la connexion à la base de données
host = "postgres"
dbname = "postgres"
user = "supever"
password = "DORsupever2025"

# Fonction pour vérifier la connexion
def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=host,
                dbname=dbname,
                user=user,
                password=password
            )
            conn.close()
            print("PostgreSQL est prêt !")
            break
        except psycopg2.OperationalError:
            print("Attente de PostgreSQL...")
            time.sleep(2)

wait_for_postgres()


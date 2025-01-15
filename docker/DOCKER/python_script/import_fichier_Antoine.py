import psycopg2
import requests
import csv
import os
import re

# Configuration pour le premier fichier CSV
gitlab_token = os.getenv("GITLAB_ACCESS_TOKEN")
gitlab_file_url_1 = "https://gitlab-student.centralesupelec.fr/api/v4/projects/13332/repository/files/data%2F241016_LogETL.csv/raw?ref=main"

# Télécharger le premier fichier CSV
headers = {"Private-Token": gitlab_token}
response = requests.get(gitlab_file_url_1, headers=headers)
if response.status_code == 200:
    with open("data1.csv", "wb") as file:
        file.write(response.content)
else:
    print("Erreur de téléchargement du fichier CSV 1")

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="DORdatabase",
    user="supever",
    password="DORsupever2025"
)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Ouverture du fichier CSV
with open("data1.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    for row in reader:
        # Insérer la ligne dans la base de données
        cur.execute("INSERT INTO \"logOK\" (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_Id, launcher_Name, program_id,program_name, schedules_id, schedules_name, schedules_startdatetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))


# Valider les changements dans la base de données
conn.commit()

# Fermeture du curseur et de la connexion
cur.close()
conn.close()


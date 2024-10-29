import psycopg2
import csv
import os
import re

# Récupérer le mot de passe depuis la variable d'environnement
password = os.getenv('passwd')

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="DORLogETL",
    user="DORuser",
    password=password
)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()


# Création de la table si elle n'existe pas déjà
create_table_query = """
CREATE TABLE IF NOT EXISTS logs (
    Server_version VARCHAR(255),
    Client_version VARCHAR(255),
    Model VARCHAR(255),
    Type VARCHAR(255),
    Insert_mode VARCHAR(255),
    Rows_added INTEGER,
    Rows_updated INTEGER,
    Rows_deleted INTEGER,
    Rows_in_error VARCHAR(255),
    Rows_in_warning VARCHAR(255),
    Columns VARCHAR(255),
    Date DATE,
    Start_time TIME,
    End_time TIME,
    Duration VARCHAR(255),
    Machine VARCHAR(255),
    Session VARCHAR(255),
    Project_name VARCHAR(255),
    Product VARCHAR(255),
    Result VARCHAR(255),
    ETL_StartDateTime TIMESTAMP,
    Launcher_Id VARCHAR(255),
    Launcher_Name VARCHAR(255),
    Program_Id VARCHAR(255),
    Program_Name VARCHAR(255),
    Schedules_Id VARCHAR(255),
    Schedules_Name VARCHAR(255),
    Schedules_StartDateTime TIMESTAMP
);
"""
cur.execute(create_table_query)
conn.commit()

# Chemin vers le fichier CSV
csv_file_path = '241016_LogETL.csv'

# Nom de la table dans laquelle importer les données
table_name = 'logs'

# Ouverture du fichier CSV
with open(csv_file_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)

    # Remplacer les espaces dans les noms de colonnes par des underscores
    original_columns = reader.fieldnames
    columns = [re.sub(r'\s+', '_', col.strip()) for col in original_columns]

    # Mettre à jour les noms de colonnes dans le lecteur CSV
    reader.fieldnames = columns

    # Création de la requête d'insertion dynamique avec les noms de colonnes nettoyés
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

    for row in reader:
        # Obtenir les valeurs des colonnes dans l'ordre
        row_values = [row[col] for col in columns]

        # Insérer la ligne dans la base de données
        cur.execute(query, row_values)

# Valider les changements dans la base de données
conn.commit()

# Fermeture du curseur et de la connexion
cur.close()
conn.close()

print("Importation réussie")


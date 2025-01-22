import psycopg2

print("Début du script")
try:
    import pandas as pd
    print("Pandas importé avec succès")
except Exception as e:
    print(f"Erreur lors de l'importation de Pandas : {e}")
    raise


print("Tous les imports ont été effectués")

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="DORdatabase",
    user="supever",
    password="DORsupever2025"
)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

print("jusqu'ici tout va bien2")

# Charger le fichier Parquet
file_path = "./data/DashboardLogs.parquet"  # Chemin du fichier Parquet
df = pd.read_parquet(file_path)

print("jusqu'ici tout va bien3")

# Parcourir chaque ligne du DataFrame et insérer les données dans la table PostgreSQL
rows = [tuple(x) for x in df.itertuples(index=False, name=None)]
cur.executemany(
        """
        INSERT INTO DashboardLogs (
            Id,
            DatetimeLog,
            Login,
            FirstName,
            LastName,
            DashboardId,
            DashboardName,
            TabName,
            ExecutionGuid,
            IsEmbedded
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        rows
    )

print("jusqu'ici tout va bien4")

# Charger le fichier Parquet
file_path = "./data/DistributionLogs.parquet"  # Chemin du fichier Parquet
df = pd.read_parquet(file_path)

# Parcourir chaque ligne du DataFrame et insérer les données dans la table PostgreSQL
rows = [tuple(x) for x in df.itertuples(index=False, name=None)]
cur.executemany(
        """
        INSERT INTO DistributionLogs (
            Id,
            DatetimeLog,
            Login,
            FirstName,
            LastName,
            DistributionId,
            DistributionName,
            IsError,
            ScheduleId,
            ScheduleName,
            ExecutionGuid
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        rows
    )

print("jusqu'ici tout va bien5")

# Charger le fichier Parquet
file_path = "./data/FieldLogs.parquet"  # Chemin du fichier Parquet
df = pd.read_parquet(file_path)

# Parcourir chaque ligne du DataFrame et insérer les données dans la table PostgreSQL
rows = [tuple(x) for x in df.itertuples(index=False, name=None)]
cur.executemany(
        """
        INSERT INTO FieldLogs (
            Id,
            DatetimeLog,
            ModelId,
            ModelName,
            TableId,
            TableName,
            RangeAddress,
            FieldId,
            FieldName,
            Login,
            FirstName,
            LastName,
            ExecutionType,
            ExecutionGuid,
            WorkbookName,
            WorkbookPath,
            MachineName,
            DistributionId,
            DistributionName,
            ScheduleId,
            ScheduleName,
            DashboardId,
            DashboardName,
            TabName,
            IsEmbedded,
            SessionName
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        rows
    )

print("jusqu'ici tout va bien6")

# Valider les changements dans la base de données
conn.commit()

print("jusqu'ici tout va bien7")

# Fermeture du curseur et de la connexion
cur.close()
conn.close()

print("jusqu'ici tout va bien8")
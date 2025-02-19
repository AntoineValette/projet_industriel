import io
from datetime import datetime

import psycopg2
from fastparquet import ParquetFile

from core.settings import Settings


def log(message):
    """Simple fonction de logging."""
    print(f"[{datetime.now()}] {message}")

def import_parquet():
    log("Début du script")

    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        host=Settings.POSTGRES_HOST,
        database=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
    )

    print("Getting ready to load data in import_parquet")
    log("Connexion à PostgreSQL établie dans import_parquet")

    # Charger le fichier Parquet
    file_path = "/data/logParquet/DetailedDashboardLogs_sub_2411222036.parquet"  # Chemin du fichier Parquet
    pf = ParquetFile(file_path)
    pf_count = pf.count()
    print(pf_count)

    log(f"Fichier Parquet chargé : {file_path}")
    log(f"Nombre total de lignes dans le fichier : {pf.count()}")

    # Définir la taille des batches
    batch_size = 5000

    # Insérer les données en batches
    total_rows = 0
    for i in range(0, pf_count, batch_size):
        log(f"Lecture des lignes {i} à {min(i + batch_size, pf_count)}")
        # Charger les données en batch en Pandas DataFrame
        batch_df = pf.to_pandas().iloc[i:i + batch_size]

        # Convertir les données en tuples
        rows = [tuple(x) for x in batch_df.itertuples(index=False, name=None)]

        if not rows:
            log(f"Aucun enregistrement à insérer pour le batch {i}")
            continue

        # Insérer dans la base de données
        log(f"Insérer {len(rows)} lignes dans la table DashboardLogs")
        with conn.cursor() as cur:
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
        conn.commit()
        total_rows += len(rows)
        log(f"Batch inséré : {len(rows)} lignes")

    log(f"Importation terminée avec succès : {total_rows} lignes insérées")

    # Charger le fichier Parquet
    file_path = "/data/logParquet/DetailedDistributionLogs_sub_2411222036.parquet"  # Chemin du fichier Parquet
    pf = ParquetFile(file_path)
    pf_count = pf.count()
    print(pf_count)

    log(f"Fichier Parquet chargé : {file_path}")
    log(f"Nombre total de lignes dans le fichier : {pf.count()}")

    # Définir la taille des batches
    batch_size = 5000

    # Insérer les données en batches
    total_rows = 0
    for i in range(0, pf_count, batch_size):
        log(f"Lecture des lignes {i} à {min(i + batch_size, pf_count)}")
        # Charger les données en batch en Pandas DataFrame
        batch_df = pf.to_pandas().iloc[i:i + batch_size]

        # Convertir les données en tuples
        rows = [tuple(x) for x in batch_df.itertuples(index=False, name=None)]

        if not rows:
            log(f"Aucun enregistrement à insérer pour le batch {i}")
            continue

        # Insérer dans la base de données
        log(f"Insérer {len(rows)} lignes dans la table DistributionLogs")
        with conn.cursor() as cur:
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
        conn.commit()
        total_rows += len(rows)
        log(f"Batch inséré : {len(rows)} lignes")

    log(f"Importation terminée avec succès : {total_rows} lignes insérées")

    # Charger le fichier Parquet
    file_path = "/data/logParquet/DetailedFieldLogs_sub_2412021040.parquet"  # Chemin du fichier Parquet
    pf = ParquetFile(file_path)
    pf_count = pf.count()
    print(pf_count)

    log(f"Fichier Parquet chargé : {file_path}")
    log(f"Nombre total de lignes dans le fichier : {pf_count}")

    # Définir la taille des batches
    batch_size = 500000
    total_rows = 0

    # Insérer les données en utilisant COPY
    for i in range(0, pf_count, batch_size):
        log(f"Lecture des lignes {i} à {min(i + batch_size, pf_count)}")

        # Charger les données en batch en Pandas DataFrame
        batch_df = pf.to_pandas().iloc[i:i + batch_size]

        # Préparer un flux CSV en mémoire
        output = io.StringIO()
        batch_df.to_csv(output, index=False, header=False)  # Pas de header car COPY attend des données brutes
        output.seek(0)

        # Copier dans la base de données
        with conn.cursor() as cur:
            log(f"Insérer {len(batch_df)} lignes dans la table FieldLogs via COPY")
            cur.copy_expert(
                """
                COPY FieldLogs (
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
                ) FROM STDIN WITH CSV
                """,
                output
            )
        conn.commit()
        total_rows += len(batch_df)
        log(f"Batch inséré : {len(batch_df)} lignes")

    log(f"Importation terminée avec succès : {total_rows} lignes insérées")

    # Fermeture du curseur et de la connexion
    conn.close()
    log("Connexion PostgreSQL fermée")
    log("exceution import_parquet terminée")

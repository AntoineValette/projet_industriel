import io
from fastparquet import ParquetFile
import psycopg2
from datetime import datetime

def log(message):
    """Simple fonction de logging."""
    print(f"[{datetime.now()}] {message}")

log("Début du script")

# Charger le fichier Parquet
file_path = "./data/FieldLogs.parquet"  # Chemin du fichier Parquet
pf = ParquetFile(file_path)
pf_count = pf.count()
print(pf_count)

log(f"Fichier Parquet chargé : {file_path}")
log(f"Nombre total de lignes dans le fichier : {pf_count}")

# Définir la taille des batches
batch_size = 500000
total_rows = 0

# Connexion à la base de données
conn = psycopg2.connect(
    host="postgres",
    database="DORdatabase",
    user="supever",
    password="DORsupever2025"
)

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

# Fermeture de la connexion
conn.close()
log("Connexion PostgreSQL fermée")

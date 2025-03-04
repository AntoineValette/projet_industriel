import io
import os
import psycopg2
import pyarrow.parquet as pq
from core.settings import Settings
from core.log import log

def import_parquet():
    log("Début du script")

    conn = psycopg2.connect(Settings.POSTGRES_URL)
    log("Connexion à PostgreSQL établie dans import_parquet")

    parquet_files = [
        ("/data/logParquet/DetailedDashboardLogs_sub_2411222036.parquet", "DashboardLogs", [
            "Id", "DatetimeLog", "Login", "FirstName", "LastName", "DashboardId", "DashboardName",
            "TabName", "ExecutionGuid", "IsEmbedded"
        ], 5000, False),
        ("/data/logParquet/DetailedDistributionLogs_sub_2411222036.parquet", "DistributionLogs", [
            "Id", "DatetimeLog", "Login", "FirstName", "LastName", "DistributionId", "DistributionName",
            "IsError", "ScheduleId", "ScheduleName", "ExecutionGuid"
        ], 5000, False),
        ("/data/logParquet/DetailedFieldLogs_sub_2412021040.parquet", "FieldLogs", [
            "Id", "DatetimeLog", "ModelId", "ModelName", "TableId", "TableName", "RangeAddress", "FieldId",
            "FieldName", "Login", "FirstName", "LastName", "ExecutionType", "ExecutionGuid", "WorkbookName",
            "WorkbookPath", "MachineName", "DistributionId", "DistributionName", "ScheduleId", "ScheduleName",
            "DashboardId", "DashboardName", "TabName", "IsEmbedded", "SessionName"
        ], 500000, True)  # Utilisation de COPY avec un batch plus grand pour FieldLogs
    ]

    for file_path, table_name, columns, batch_size, use_copy in parquet_files:
        if os.path.isfile(file_path):
            log(f"Fichier Parquet trouvé : {file_path}")
            
            pf = pq.ParquetFile(file_path)
            log("Lecture du fichier Parquet en streaming")
            
            total_rows = 0
            
            for batch in pf.iter_batches(batch_size=batch_size):
                batch_df = batch.to_pandas()
                log(f"Lecture d'un batch de taille {len(batch_df)}")
                
                if use_copy:
                    output = io.StringIO()
                    batch_df.to_csv(output, index=False, header=False)
                    output.seek(0)

                    with conn.cursor() as cur:
                        log(f"Insertion de {len(batch_df)} lignes dans la table {table_name} via COPY")
                        cur.copy_expert(
                            f"""
                            COPY {table_name} ({', '.join(columns)})
                            FROM STDIN WITH CSV
                            """, output
                        )
                else:
                    rows = [tuple(x) for x in batch_df.itertuples(index=False, name=None)]
                    
                    if rows:
                        with conn.cursor() as cur:
                            log(f"Insertion de {len(rows)} lignes dans la table {table_name}")
                            cur.executemany(
                                f"""
                                INSERT INTO {table_name} ({', '.join(columns)})
                                VALUES ({', '.join(['%s'] * len(columns))})
                                """, rows
                            )
                
                conn.commit()
                total_rows += len(batch_df)
                log(f"Batch inséré : {len(batch_df)} lignes")

            log(f"Importation terminée avec succès : {total_rows} lignes insérées dans {table_name}")

    conn.close()
    log("Connexion PostgreSQL fermée")
    log("Exécution import_parquet terminée")

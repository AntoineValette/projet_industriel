from ETL.logETL.importLogETL import importLogETL
from ETL.logETL.importLogETLError import importLogETLerror
from ETL.logParquet.import_parquet import import_parquet
from ETL.logServer.importLogServer import import_log_server
from ETL.mergeDF.importMergeDF import importMergeDF
from core.wait_for_postgres import wait_for_postgres

if __name__ == "__main__":

    wait_for_postgres()
    # import des logETl ok et error
    importLogETL()
    importLogETLerror()

    # import des logServer
    import_log_server()

    # import du mergeDF
    importMergeDF()

    # import des logParquets
    import_parquet()

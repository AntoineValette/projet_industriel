from ETL.logParquet.import_parquet import import_parquet
from ETL.logServer.logServer import logServer
from waiting.wait_for_postgres import wait_for_postgres
from waiting.wait_for_import import wait_for_import


if __name__ == "__main__":
    # attente de postgresql
    wait_for_postgres()

    # import des logServer
    logServer()

    # import des logParquets
    import_parquet()

    # attente de l'import historique par kafka
    wait_for_import()

from core.wait_for_postgres import wait_for_postgres
from ETL.logETL.importLogETL import importLogETL
from ETL.logETL.importLogETLError import importLogETLerror
from ETL.import_csv import import_csv
from ETL.import_parquet import import_parquet

if __name__ == "__main__":

    wait_for_postgres()
    # import des logETl ok et error
    importLogETL()
    importLogETLerror()

    # import des logServer
    import_csv()

    # import des logParquets
    import_parquet()


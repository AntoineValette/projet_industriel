from ETL.logETL.logETL import logETL
from ETL.logETL.logETLError import logEtlError
from ETL.logParquet.import_parquet import import_parquet
from ETL.logServer.logServer import logServer
from ETL.mergeDF.experiment.mergeDF import mergeDF
from core.wait_for_postgres import wait_for_postgres

if __name__ == "__main__":
    # attente de postgresql
    wait_for_postgres()

    # import des logETl ok et error
    logETL()
    logEtlError()

    # import des logServer
    logServer()

    # import du mergeDF
    # mergeDF()

    # import des logParquets
    import_parquet()

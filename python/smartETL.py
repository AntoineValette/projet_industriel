from init.wait_for_postgres import wait_for_postgres
from init.import_csv import import_csv
from init.import_parquet import import_parquet

if __name__ == "__main__":

    wait_for_postgres()
    import_csv()
    import_parquet()


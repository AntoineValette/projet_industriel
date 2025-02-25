from os import rename

import pandas as pd
from sqlalchemy import create_engine

from core.log import log
from core.settings import settings
import os

# Étape 1 : Extraction des données
def extract_data(file_path):
    log("extract data" + file_path)
    data = pd.read_csv(file_path, sep=',', index_col=0)
    return data

# Étape 2 : Transformation des données
def transform_data(data):
    data.columns = (data.columns.str.strip().str.lower().str.replace(' ', '_'))
    data.columns = (data.columns.str.replace(':', ''))
    data.columns = (data.columns.str.replace('(raw)', '_raw'))

    # data = data.dropna()
    return data

# Étape 3 : Chargement des données
def load_data(data, db_connection_string, table_name):
    engine = create_engine(db_connection_string)
    data.to_sql(table_name, engine, if_exists='append', index=False, chunksize=1000)


name = "myreport_espace_disque"
table_name = f"{name}_raw"
rename_columns = []
delete_columns = []
file_path = f'../../../data/logServer/{name}_full.csv'
db_connection_string = settings.POSTGRES_URL

if os.path.exists(file_path):
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    load_data(transformed_data, db_connection_string, table_name)

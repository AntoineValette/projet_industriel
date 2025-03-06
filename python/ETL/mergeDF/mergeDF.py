import csv
import os
import psycopg2
import pandas as pd

from core.log import log
from core.settings import Settings
from core.classification_error import categorize_message

def mergeDF():
    filename = "/data/dataset_LogETL_LogServer.csv"
    if os.path.isfile(filename):
        log("Connexion à PostgreSQL établie dans import_csv")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("extract dataset_LogETL_LogServer")
        df_error = pd.read_csv('../../../data/logEtl/241016_LogETLError.csv', sep=';',
                               dtype={'Program_Id': str, 'Schedules_Id': str, 'Schedules_Name': str})
        df_error['ETL_StartDateTime'] = pd.to_datetime(df_error['ETL_StartDateTime'], format="%Y-%m-%d %H:%M:%S")

        start_date = df_error['ETL_StartDateTime'].min()
        end_date = df_error['ETL_StartDateTime'].max()

        df_error["Date et heure"] = df_error["ETL_StartDateTime"].dt.floor("h")

        df_error = df_error.assign(
            Message_Category=df_error["Message"].apply(categorize_message)
        )

        # Comptage des catégories par Date et heure
        df_cat = pd.crosstab(df_error["Date et heure"], df_error["Message_Category"])

        # Comptage des programmes par Date et heure
        df_prog = pd.crosstab(df_error["Date et heure"], df_error["Program_Name"])

        # Joindre les deux sur l'index (qui est "Date et heure" dans les 2 crosstabs)
        df_error_grouped2 = df_cat.join(df_prog, how="outer")

        # Remettre "Date et heure" en colonne si besoin
        df_error_grouped2 = df_error_grouped2.reset_index()

        df_error_grouped2.head()

        error_columns = [col for col in df_error_grouped2.columns if "Error" in col]
        df_error_grouped2["Total_Errors"] = df_error_grouped2[error_columns].sum(axis=1)



        log("dataset_LogETL_LogServer [ok]")
        conn.commit()

        cur.close()
        conn.close()
        log("fermeture de la connexion PostgreSQL")


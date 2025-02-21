import csv
import os
import psycopg2
import pandas as pd

from core.log import log
from core.settings import Settings

def myreport_swap():
    filename = "/data/logServer/myreport_swap_full.csv"
    if os.path.isfile(filename):
        log("PostgreSQL - open")
        conn = psycopg2.connect(Settings.POSTGRES_URL)
        cur = conn.cursor()

        log("+-- extract myreport_swap")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                cur.execute("""INSERT INTO myreport_swap (
                        date_heure,date_heure_raw,
                        Total, 
                        Total_RAW, 
                        temps_mort_mem, 
                        temps_mort_mem_RAW,
                        couverture_mem, 
                        couverture_mem_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s
                    )""", tuple(row.values()))
        log("+-- extract myreport_swap [ok]")
        conn.commit()
        cur.close()

        # transform
        log("+-- transform myreport_swap ...")
        tab = pd.read_sql("SELECT * FROM myreport_swap", conn)

        tab['Date et heure'] = tab["Date et heure"].str.split(" - ").str[0]
        #tab = tab.iloc[:-5]
        ## Si vous avez un format comme "JJ/MM/AAAA HH:MM:SS", vous pouvez préciser :
        #tab['Date et heure'] = pd.to_datetime(tab['Date et heure'], format="%d/%m/%Y %H:%M:%S")
        #start_date = '2024-08-24 23:32:03'
        #end_date = '2024-10-15 23:31:49'
        #tab = tab[(tab['Date et heure'] >= start_date) & (tab['Date et heure'] <= end_date)]
        ## suppression des colonnes inutiles
        #tab = tab.drop(columns=["Date et heure(RAW)"])
        #tab = tab.drop(columns=["Total"])
        #tab = tab.drop(columns=["Temps mort"])
        #tab = tab.drop(columns=["Couverture"])
        ## renommage des colonnes
        #tab.rename(columns={"Temps mort(RAW)": "swap Temps mort(%)"}, inplace=True)
        #tab.rename(columns={"Couverture(RAW)": "swap Couverture(%)"}, inplace=True)
        #tab.rename(columns={"Total(RAW)": "total swap(%)"}, inplace=True)
        #
        #tab = tab.drop(columns=["swap Temps mort(%)"])
        #tab = tab.drop(columns=["swap Couverture(%)"])
        #
        #
        ## load
        log("+-- load myreport_swap ...")
        #tab.to_sql("myreport_swap_filtered", conn, if_exists='append', index=False)

        conn.close()
        log("PostgreSQL - close")

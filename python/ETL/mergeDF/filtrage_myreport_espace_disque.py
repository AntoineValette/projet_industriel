import pandas as pd


def get_df_cpu(start_date, end_date):
    tab = pd.read_csv('../../data/logServer/myreport_espace_disque_full.csv', sep=',')
    tab["Date et heure"] = tab["Date et heure"].str.split(" - ").str[0]
    tab = tab.iloc[:-5]
    tab['Date et heure'] = pd.to_datetime(tab['Date et heure'], format="%d/%m/%Y %H:%M:%S")

    # start_date = '2024-08-24 23:32:03'
    # end_date = '2024-10-15 23:31:49'

    tab = tab[(tab['Date et heure'] >= start_date) & (tab['Date et heure'] <= end_date)]

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["Date et heure(RAW)"])
    tab = tab.drop(columns=["Somme"])
    tab = tab.drop(columns=["Octets libres C:"])
    tab = tab.drop(columns=["Espace disponible C:"])
    tab = tab.drop(columns=["Octets libres D:"])
    tab = tab.drop(columns=["Espace disponible D:"])

    tab = tab.drop(columns=["Temps mort"])
    tab = tab.drop(columns=["Couverture"])

    # renommage des colonnes
    tab.rename(columns={"Somme(RAW)": "Somme (espace disque)(Go)"}, inplace=True)
    tab.rename(columns={"Octets libres C:(RAW)": "Octets libres C:(octets)"}, inplace=True)
    tab.rename(columns={"Espace disponible C:(RAW)": "Espace disponible C:(%)"}, inplace=True)
    tab.rename(columns={"Octets libres D:(RAW)": "Octets libres D:(octets)"}, inplace=True)
    tab.rename(columns={"Espace disponible D:(RAW)": "Espace disponible D:(%)"}, inplace=True)

    tab.rename(columns={"Temps mort(RAW)": "Temps mort espace disque(%)"}, inplace=True)
    tab.rename(columns={"Couverture(RAW)": "Couverture espace disque(%)"}, inplace=True)

    # on garde tout ici

    return tab
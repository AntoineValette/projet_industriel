import pandas as pd

def get_df_cpu(start_date, end_date):
    tab = pd.read_csv('../../data/logServer/myreport_cpu_full.csv', sep=',')
    tab["Date et heure"] = tab["Date et heure"].str.split(" - ").str[0]
    tab = tab.iloc[:-5]
    tab['Date et heure'] = pd.to_datetime(tab['Date et heure'], format="%d/%m/%Y %H:%M:%S")

    #start_date = '2024-08-24 23:32:03'
    #end_date = '2024-10-15 23:31:49'
    
    tab = tab[(tab['Date et heure'] >= start_date) & (tab['Date et heure'] <= end_date)]


    # suppression des colonnes inutiles
    tab = tab.drop(columns=["Date et heure(RAW)"])
    tab = tab.drop(columns=["Somme"])
    tab = tab.drop(columns=["Processeur 1"])
    tab = tab.drop(columns=["Processeur 2"])
    tab = tab.drop(columns=["Processeur 3"])
    tab = tab.drop(columns=["Processeur 4"])
    tab = tab.drop(columns=["Processeur 5"])
    tab = tab.drop(columns=["Processeur 6"])
    tab = tab.drop(columns=["Processeur 7"])
    tab = tab.drop(columns=["Processeur 8"])
    tab = tab.drop(columns=["Temps mort"])
    tab = tab.drop(columns=["Couverture"])

    # renommage des colonnes
    tab.rename(columns={"Somme(RAW)": "Somme(%)"}, inplace=True)
    tab.rename(columns={"Processeur 1(RAW)": "Processeur 1(%)"}, inplace=True)
    tab.rename(columns={"Processeur 2(RAW)": "Processeur 2(%)"}, inplace=True)
    tab.rename(columns={"Processeur 3(RAW)": "Processeur 3(%)"}, inplace=True)
    tab.rename(columns={"Processeur 4(RAW)": "Processeur 4(%)"}, inplace=True)
    tab.rename(columns={"Processeur 5(RAW)": "Processeur 5(%)"}, inplace=True)
    tab.rename(columns={"Processeur 6(RAW)": "Processeur 6(%)"}, inplace=True)
    tab.rename(columns={"Processeur 7(RAW)": "Processeur 7(%)"}, inplace=True)
    tab.rename(columns={"Processeur 8(RAW)": "Processeur 8(%)"}, inplace=True)

    tab.rename(columns={"Temps mort(RAW)": "Temps mort cpu(%)"}, inplace=True)
    tab.rename(columns={"Couverture(RAW)": "Couverture cpu(%)"}, inplace=True)


    #on garde tout ici

    return tab
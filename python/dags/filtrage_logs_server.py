import pandas as pd

def format_datetime(tab:pd.DataFrame, colonne_datetime: str):
    """
    transformation de la colonne "date_heure" du dataframe en pd.datetime
    application d'un filtre sur les dates ==>> à supprimer pour la prod
    """
    tab[colonne_datetime] = tab[colonne_datetime].str.split(" - ").str[0]
    tab[colonne_datetime] = pd.to_datetime(tab[colonne_datetime], format="%d/%m/%Y %H:%M:%S")

    """
    start_date = '2024-08-24 23:32:03'
    end_date = '2024-10-15 23:31:49'
    tab = tab[(tab[colonne_datetime] >= start_date) & (tab[colonne_datetime] <= end_date)]
    """
    return tab


def get_cpu_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["somme"])
    tab = tab.drop(columns=["processeur_1"])
    tab = tab.drop(columns=["processeur_2"])
    tab = tab.drop(columns=["processeur_3"])
    tab = tab.drop(columns=["processeur_4"])
    tab = tab.drop(columns=["processeur_5"])
    tab = tab.drop(columns=["processeur_6"])
    tab = tab.drop(columns=["processeur_7"])
    tab = tab.drop(columns=["processeur_8"])
    tab = tab.drop(columns=["temps_mort_cpu"])
    tab = tab.drop(columns=["couverture_cpu"])

    # renommage des colonnes
    tab.rename(columns={"somme_raw": "Somme_pct"}, inplace=True)
    tab.rename(columns={"processeur_1_raw": "Processeur_1_pct"}, inplace=True)
    tab.rename(columns={"processeur_2_raw": "Processeur_2_pct"}, inplace=True)
    tab.rename(columns={"processeur_3_raw": "Processeur_3_pct"}, inplace=True)
    tab.rename(columns={"processeur_4_raw": "Processeur_4_pct"}, inplace=True)
    tab.rename(columns={"processeur_5_raw": "Processeur_5_pct"}, inplace=True)
    tab.rename(columns={"processeur_6_raw": "Processeur_6_pct"}, inplace=True)
    tab.rename(columns={"processeur_7_raw": "Processeur_7_pct"}, inplace=True)
    tab.rename(columns={"processeur_8_raw": "Processeur_8_pct"}, inplace=True)

    tab.rename(columns={"temps_mort_cpu_raw": "Temps_mort_cpu_pct"}, inplace=True)
    tab.rename(columns={"couverture_cpu_raw": "Couverture_cpu_pct"}, inplace=True)

    return tab

def get_storage_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab=tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["somme"])
    tab = tab.drop(columns=["octetlibrec"])
    tab = tab.drop(columns=["espacedisponiblec"])
    tab = tab.drop(columns=["octetlibred"])
    tab = tab.drop(columns=["espacedisponibled"])

    tab = tab.drop(columns=["temp_mort"])
    tab = tab.drop(columns=["couverture"])

    # renommage des colonnes
    tab.rename(columns={"somme_raw": "Somme_espace_disque_Go"}, inplace=True)
    tab.rename(columns={"octet-librec_raw": "Octets_libres_C_octets"}, inplace=True)
    tab.rename(columns={"espacedisponiblec_raw": "Espace_disponible_C_pct"}, inplace=True)
    tab.rename(columns={"octetlibred_raw": "Octets_libres_D_octets"}, inplace=True)
    tab.rename(columns={"espacedisponibled_raw": "Espace_disponible_D_pct"}, inplace=True)

    tab.rename(columns={"temp_mort_raw": "Temps mort espace disque(%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture espace disque(%)"}, inplace=True)

    tab = tab.drop(columns=["Temps mort espace disque(%)"])
    tab = tab.drop(columns=["Couverture espace disque(%)"])

    return tab

def get_ping_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["temps_du_ping"])
    tab = tab.drop(columns=["minimum"])
    tab = tab.drop(columns=["maximum"])
    tab = tab.drop(columns=["perte_de_paquets"])
    tab = tab.drop(columns=["temps_mort"])
    tab = tab.drop(columns=["couverture"])

    # renommage des colonnes
    tab.rename(columns={"temps_du_ping_raw": "Temps_du_ping_ms"}, inplace=True)
    tab.rename(columns={"minimum_raw": "Minimum ping (ms)"}, inplace=True)
    tab.rename(columns={"maximum_raw": "Maximum_ping_ms"}, inplace=True)
    tab.rename(columns={"perte_de_paquets_raw": "Perte_de_paquets_ping_pct"}, inplace=True)
    tab.rename(columns={"temps_mort_raw": "Temps mort ping (%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture ping(%)"}, inplace=True)

    tab = tab.drop(columns=["Couverture ping(%)"])
    tab = tab.drop(columns=["Temps mort ping (%)"])
    tab = tab.drop(columns=["Minimum ping (ms)"])

    return tab

def get_ram_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["memoire_disponible_pct"])
    tab = tab.drop(columns=["memoire_disponible_go"])
    tab = tab.drop(columns=["temps_mort_pct"])
    tab = tab.drop(columns=["couverture_pct"])

    tab.rename(columns={"memoire_disponible_pct_RAW": "Memoire_disponible_ram_pct"}, inplace=True)
    tab.rename(columns={"memoire_disponible_go_RAW": "Memoire_disponible_ram_Go"}, inplace=True)
    tab.rename(columns={"temps_mort_raw": "Temps mort ram(%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture_ram_pct"}, inplace=True)

    tab = tab.drop(columns=["Temps mort ram(%)"])

    return tab

def get_reseau_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["somme_volume"])

    tab = tab.drop(columns=["somme_debit"])
    tab = tab.drop(columns=["trafic_entrant_volume"])
    tab = tab.drop(columns=["trafic_entrant_debit"])
    tab = tab.drop(columns=["trafic_sortant_volume"])
    tab = tab.drop(columns=["trafic_sortant_debit"])

    tab = tab.drop(columns=["paquets_volume"])
    tab = tab.drop(columns=["paquets_debit"])

    tab = tab.drop(columns=["paquets_refus_volume"])
    tab = tab.drop(columns=["paquets_refus_debit"])

    tab = tab.drop(columns=["paquets_envoyes_volume"])
    tab = tab.drop(columns=["paquets_envoyes_debit"])

    tab = tab.drop(columns=["monodiffusion_entrante_volume"])
    tab = tab.drop(columns=["monodiffusion_entrante_debit"])
    tab = tab.drop(columns=["monodiffusion_sortante_volume"])
    tab = tab.drop(columns=["monodiffusion_sortante_debit"])

    tab = tab.drop(columns=["paquets_non_monodiffusion_entrants_volume"])
    tab = tab.drop(columns=["paquets_non_monodiffusion_entrants_debit"])
    tab = tab.drop(columns=["paquets_non_monodiffusion_sortants_volume"])
    tab = tab.drop(columns=["paquets_non_monodiffusion_sortants_debit"])

    tab = tab.drop(columns=["erreurs_entrantes_volume"])
    tab = tab.drop(columns=["erreurs_entrantes_debit"])
    tab = tab.drop(columns=["erreurs_sortantes_volume"])
    tab = tab.drop(columns=["erreurs_sortantes_debit"])

    tab = tab.drop(columns=["entrants_rejets_volume"])
    tab = tab.drop(columns=["entrants_rejets_debit"])
    tab = tab.drop(columns=["sortants_rejets_volume"])
    tab = tab.drop(columns=["sortants_rejets_debit"])

    tab = tab.drop(columns=["protocoles_inconnus_entrants_volume"])
    tab = tab.drop(columns=["protocoles_inconnus_entrants_debit"])

    tab = tab.drop(columns=["temps_mort"])
    tab = tab.drop(columns=["couverture"])

    # renommage des colonnes
    tab.rename(columns={"somme_volume_raw": "Somme_Volume_Mo"}, inplace=True)
    tab.rename(columns={"somme_debit_raw": "Somme_Debit_Mbit_s"}, inplace=True)

    tab.rename(columns={"trafic_entrant_volume_raw": "Trafic_entrant_Volume_o"}, inplace=True)
    tab.rename(columns={"trafic_entrant_debit_raw": "Trafic_entrant_Debit_o_s"}, inplace=True)
    tab.rename(columns={"trafic_sortant_volume_raw": "Trafic_sortant_Volume_o"}, inplace=True)
    tab.rename(columns={"trafic_sortant_debit_raw": "Trafic_sortant_Debit_o_s"}, inplace=True)

    tab.rename(columns={"paquets_volume_raw": "Paquets_Volume_o"}, inplace=True)
    tab.rename(columns={"paquets_debit_raw": "Paquets_Debit_o_s"}, inplace=True)

    tab.rename(columns={"paquets_refus_volume_raw": "Paquets_rebus_Volume_o"}, inplace=True)
    tab.rename(columns={"paquets_refus_debit_raw": "Paquets_rebus_Debit_o_s"}, inplace=True)

    tab.rename(columns={"paquets_envoyes_volume_raw": "Paquets_envoyes_Volume_o"}, inplace=True)
    tab.rename(columns={"paquets_envoyes_debit_raw": "Paquets_envoyes_Debit_o_s"}, inplace=True)

    tab.rename(columns={"monodiffusion_entrante_volume_raw": "Monodiffusion_entrante_Volume_o"}, inplace=True)
    tab.rename(columns={"monodiffusion_entrante_debit_raw": "Monodiffusion_entrante_Debit_o_s"}, inplace=True)
    tab.rename(columns={"monodiffusion_sortante_volume_raw": "Monodiffusion_sortante_Volume_o"}, inplace=True)
    tab.rename(columns={"monodiffusion_sortante_debit_raw": "Monodiffusion_sortante_Debit_o_s"}, inplace=True)

    tab.rename(columns={"paquets_non_monodiffusion_entrants_volume_raw": "Paquets_non_monodiffusion_entrants_Volume_o"},
               inplace=True)
    tab.rename(columns={"paquets_non_monodiffusion_entrants_debit_raw": "Paquets_non_monodiffusion_entrants_Debit_o_s"},
               inplace=True)
    tab.rename(columns={"paquets_non_monodiffusion_sortants_volume_raw": "Paquets_non_monodiffusion_sortants_Volume_o"},
               inplace=True)
    tab.rename(columns={"paquets_non_monodiffusion_sortants_debit_raw": "Paquets_non_monodiffusion_sortants_Debit_o_s"},
               inplace=True)

    tab.rename(columns={"entrants_rejets_volume_raw": "Entrants_rejetes_Volume_o"}, inplace=True)
    tab.rename(columns={"entrants_rejets_debit_raw": "Entrants_rejetes_Debit_o_s"}, inplace=True)

    tab.rename(columns={"couverture_raw": "Couverture_reseau_pct"}, inplace=True)

    tab = tab.drop(columns=["erreurs_entrantes_volume_raw"])
    tab = tab.drop(columns=["erreurs_entrantes_debit_raw"])

    tab = tab.drop(columns=["erreurs_sortantes_volume_raw"])
    tab = tab.drop(columns=["erreurs_sortantes_debit_raw"])

    tab = tab.drop(columns=["sortants_rejets_volume_raw"])
    tab = tab.drop(columns=["sortants_rejets_debit_raw"])

    tab = tab.drop(columns=["protocoles_inconnus_entrants_volume_raw"])
    tab = tab.drop(columns=["protocoles_inconnus_entrants_debit_raw"])

    tab = tab.drop(columns=["temps_mort_raw"])

    return tab

def get_sql_general_filetered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["connexions"])
    tab = tab.drop(columns=["déconnexions"])
    tab = tab.drop(columns=["connexions_user"])
    tab = tab.drop(columns=["temp_mort"])
    tab = tab.drop(columns=["couverture"])

    # renommage des colonnes
    tab.rename(columns={"connexions_user_raw": "Connexions_utilisateur_nb"}, inplace=True)
    tab.rename(columns={"connexions_Raw": "Connexions_s_nb"}, inplace=True)
    tab.rename(columns={"déconnexions_raw": "Deconnexions_s_nb"}, inplace=True)
    tab.rename(columns={"temp_mort_raw": "Temps mort sql general(%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture sql general(%)"}, inplace=True)

    tab = tab.drop(columns=["Temps mort sql general(%)"])
    tab = tab.drop(columns=["Couverture sql general(%)"])

    return tab

def get_memoire_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["memconnexion"])
    tab = tab.drop(columns=["memoptimiseur"])
    tab = tab.drop(columns=["memtotaleserveur"])
    tab = tab.drop(columns=["memserveurcible"])
    tab = tab.drop(columns=["memecachesql"])

    tab = tab.drop(columns=["temps_mort_mem"])
    tab = tab.drop(columns=["couverture_mem"])

    # renommage des colonnes
    tab.rename(columns={"memconnexion_raw": "Memoire_de_connexion_sql_gestmemoire_Ko"}, inplace=True)
    tab.rename(columns={"memoptimiseur_raw": "Memoire_de_l_optimiseur_sql_gestmemoire_Ko"}, inplace=True)
    tab.rename(columns={"memtotaleserveur_raw": "Memoire_totale_du_serveur_sql_gestmemoire_Ko"},
               inplace=True)
    tab.rename(columns={"memserveurcible_raw": "Mémoire du serveur cible_sql_gestmemoire(Ko)"}, inplace=True)
    tab.rename(columns={"memecachesql_raw": "Memoire_du_cache_SQL_sql_gestmemoire_Ko"}, inplace=True)

    tab.rename(columns={"temps_mort_mem_raw": "Temps mort_sql_gestmemoire(%)"}, inplace=True)
    tab.rename(columns={"couverture_mem_raw": "Couverture_sql_gestmemoire(%)"}, inplace=True)

    tab = tab.drop(columns=["Temps mort_sql_gestmemoire(%)"])
    tab = tab.drop(columns=["Couverture_sql_gestmemoire(%)"])
    tab = tab.drop(columns=["Mémoire du serveur cible_sql_gestmemoire(Ko)"])

    return tab

def get_sql_lock_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["nombre_requetes_verrouillage"])
    tab = tab.drop(columns=["temps_attente_moyen"])
    tab = tab.drop(columns=["nombre_blocages"])
    tab = tab.drop(columns=["temps_mort"])
    tab = tab.drop(columns=["couverture"])

    # renommage des colonnes
    tab.rename(columns={"nombre_requetes_verrouillage_raw": "requete_verrouillage_sql_lock_nb_s"},
               inplace=True)
    tab.rename(columns={"temps_attente_moyen_raw": "temps_attente_sql_lock_ms"}, inplace=True)
    tab.rename(columns={"nombre_blocages_raw": "nbr_blocage (sql lock)(nb/s)"}, inplace=True)
    tab.rename(columns={"temps_mort_raw": "Temps mort (sql lock)(%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture (sql lock)(%)"}, inplace=True)

    tab = tab.drop(columns=["Couverture (sql lock)(%)"])
    tab = tab.drop(columns=["Temps mort (sql lock)(%)"])
    tab = tab.drop(columns=["nbr_blocage (sql lock)(nb/s)"])

    return tab

def get_sql_statistic_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["nombre_requetes_lots"])
    tab = tab.drop(columns=["compilations_sql"])
    tab = tab.drop(columns=["recompilations_sql"])
    tab = tab.drop(columns=["temps_mort_pct"])
    tab = tab.drop(columns=["couverture_pct"])

    # renommage des colonnes
    tab.rename(columns={"nombre_requetes_lots_raw": "Nombre_de_requetes_de_lots_sql_stat"},
               inplace=True)
    tab.rename(columns={"compilations_sql_raw": "Compilations_SQL_s_sql_stat"}, inplace=True)
    tab.rename(columns={"recompilations_sql_raw": "Recompilations_SQL_s_sql_stat"}, inplace=True)
    tab.rename(columns={"temps_mort_raw": "Temps mort (sql stat)(%)"}, inplace=True)
    tab.rename(columns={"couverture_raw": "Couverture (sql stat)(%)"}, inplace=True)

    tab = tab.drop(columns=["Temps mort (sql stat)(%)"])
    tab = tab.drop(columns=["Couverture (sql stat)(%)"])

    return tab

def get_swap_filtered(tab: pd.DataFrame):
    tab=format_datetime(tab,'date_heure')

    # suppression des colonnes inutiles
    tab = tab.drop(columns=["ident"])
    tab = tab.drop(columns=["dt_insertion"])

    tab = tab.drop(columns=["date_heure_raw"])
    tab = tab.drop(columns=["total"])
    tab = tab.drop(columns=["temps_mort_mem"])
    tab = tab.drop(columns=["couverture_mem"])

    # renommage des colonnes
    tab.rename(columns={"temps_mort_mem_raw": "swap Temps mort(%)"}, inplace=True)
    tab.rename(columns={"couverture_mem_raw": "swap Couverture(%)"}, inplace=True)
    tab.rename(columns={"total": "total swap(%)"}, inplace=True)
    tab.rename(columns={"total_raw": "total_swap"}, inplace=True)

    tab = tab.drop(columns=["swap Temps mort(%)"])
    tab = tab.drop(columns=["swap Couverture(%)"])

    return tab
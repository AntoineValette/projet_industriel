import psycopg2
import csv
import os
from datetime import datetime

import psycopg2

from core.settings import Settings


def log(message):
    """Simple fonction de logging."""
    print(f"[{datetime.now()}] {message}")

def value(n):
    return ", ".join(["%s"] * n)

def import_csv():
    # Connexion à la base de données PostgreSQL

    print("Getting ready to load data in import_csv")
    log("Connexion à PostgreSQL établie dans import_csv")

    conn = psycopg2.connect(
        host=Settings.POSTGRES_HOST,
        database=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
    )


def log(message):
    """Simple fonction de logging."""
    print(f"[{datetime.now()}] {message}")

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="supever",
    password="DORsupever2025"
)

print("Getting ready to load data in import_csv")
log("Connexion à PostgreSQL établie dans import_csv")

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Ouverture du fichier CSV
with open("/data/logETL/241016_LogETL.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    for row in reader:
        # Insérer la ligne dans la base de données
        #print(row)
        cur.execute("INSERT INTO logOK (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_Id, launcher_Name, program_id,program_name, schedules_id, schedules_name, schedules_startdatetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
log("241016_LogETL.csv - ok")
conn.commit()

# Ouverture du fichier CSV
with open("/data/logETL/241016_LogETLError.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    for row in reader:
        # Insérer la ligne dans la base de données
        #print(row)
        cur.execute("INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
log("241016_LogETLError.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_ping_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        #print(reader.fieldnames)
        if not row[reader.fieldnames[2]]:
            #print(row[reader.fieldnames[0]])
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("INSERT INTO myreport_ping (date_et_heure, date_et_heure_raw, temps_du_ping, temps_du_ping_raw, minimum, minimum_raw, maximum, maximum_raw, perte_de_paquets, perte_de_paquets_raw, temps_mort, temps_mort_raw, couverture, couverture_raw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))
log("241016_LogETLError.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_cpu_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print(row[reader.fieldnames[0]])
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
    INSERT INTO myreport_cpu (
        Date, heureDate_RAW, Somme, Somme_RAW, 
        Processeur_1, Processeur_1_RAW, Processeur_2, Processeur_2_RAW, 
        Processeur_3, Processeur_3_RAW, Processeur_4, Processeur_4_RAW, 
        Processeur_5, Processeur_5_RAW, Processeur_6, Processeur_6_RAW, 
        Processeur_7, Processeur_7_RAW, Processeur_8, Processeur_8_RAW, 
        Temps_mort_cpu, Temps_mort_cpu_RAW, Couverture_cpu, Couverture_cpu_RAW
    ) VALUES (
        %s, %s, %s, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s
    )
    """, tuple(row.values()))
log("myreport_cpu_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_ram_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
           # print(row[reader.fieldnames[0]])
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_ram (
                date_heure, 
                date_heure_raw, 
                memoire_disponible_pct, 
                memoire_disponible_pct_RAW, 
                memoire_disponible_go, 
                memoire_disponible_go_RAW, 
                temps_mort_pct, 
                temps_mort_raw, 
                couverture_pct, 
                couverture_raw
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s
            )
        """, tuple(row.values()))
log("myreport_ram_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_reseau_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        if any("Sommes" in value for value in row.values()):
            #print(f'Ligne ignorée (somme détectée) : {row}')
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        #print("Nombre de valeurs :", len(tuple(row.values())))
        cur.execute("""INSERT INTO myreport_reseau (
                Date,
                heureDate_RAW,
                Somme_Volume,
                Somme_Volume_RAW, 
                Somme_Debit,
                Somme_Debit_RAW,
                Trafic_Entrant_Volume,
                Trafic_Entrant_Volume_RAW,
                Trafic_Entrant_Debit,
                Trafic_Entrant_Debit_RAW,
                Trafic_Sortant_Volume,
                Trafic_Sortant_Volume_RAW,
                Trafic_Sortant_Debit,
                Trafic_Sortant_Debit_RAW,
                Paquets_Volume,
                Paquets_Volume_RAW,
                Paquets_Debit,
                Paquets_Debit_RAW,
                Paquets_Refus_Volume,
                Paquets_Refus_Volume_RAW,
                Paquets_Refus_Debit,
                Paquets_Refus_Debit_RAW,
                Paquets_Envoyes_Volume,
                Paquets_Envoyes_Volume_RAW,
                Paquets_Envoyes_Debit,
                Paquets_Envoyes_Debit_RAW,
                Monodiffusion_entrante_Volume,
                Monodiffusion_entrante_Volume_RAW,
                Monodiffusion_entrante_Debit,
                Monodiffusion_entrante_Debit_RAW,
                Monodiffusion_sortante_Volume,
                Monodiffusion_sortante_Volume_RAW,
                Monodiffusion_sortante_Debit,
                Monodiffusion_sortante_Debit_RAW,
                Paquets_non_monodiffusion_entrants_Volume,
                Paquets_non_monodiffusion_entrants_Volume_RAW,
                Paquets_non_monodiffusion_entrants_Debit,
                Paquets_non_monodiffusion_entrants_Debit_RAW,
                Paquets_non_monodiffusion_sortants_Volume,
                Paquets_non_monodiffusion_sortants_Volume_RAW,
                Paquets_non_monodiffusion_sortants_Debit,
                Paquets_non_monodiffusion_sortants_Debit_RAW,
                Erreurs_entrantes_Volume,
                Erreurs_entrantes_Volume_RAW,
                Erreurs_entrantes_Debit,
                Erreurs_entrantes_Debit_RAW,
                Erreurs_sortantes_Volume,
                Erreurs_sortantes_Volume_RAW,
                Erreurs_sortantes_Debit,
                Erreurs_sortantes_Debit_RAW,
                Entrants_rejets_Volume,
                Entrants_rejets_Volume_RAW,
                Entrants_rejets_Debit,
                Entrants_rejets_Debit_RAW,
                Sortants_rejets_Volume,
                Sortants_rejets_Volume_RAW,
                Sortants_rejets_Debit,
                Sortants_rejets_Debit_RAW,
                Protocoles_inconnus_entrants_Volume,
                Protocoles_inconnus_entrants_Volume_RAW,
                Protocoles_inconnus_entrants_Debit,
                Protocoles_inconnus_entrants_Debit_RAW,
                Temps_mort,
                Temps_mort_RAW,
                Couverture,
                Couverture_RAW
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s
            )
        """, tuple(row.values()))
log("myreport_reseau_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_espace_disque_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_memoire (
                Date, 
                heureDate_RAW, 
                MemConnexion, 
                MemConnexion_RAW, 
                MemOptimiseur, 
                MemOptimiseur_RAW, 
                MemTotaleServeur, 
                MemTotaleServeur_RAW, 
                MemServeurCible, 
                MemServeurCible_RAW, 
                MemeCacheSQL, 
                MemeCacheSQL_RAW, 
                Temps_mort_mem, 
                Temps_mort_mem_RAW, 
                Couverture_mem, 
                Couverture_mem_RAW
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_espace_disque_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_sql_lock_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_sql_lock (
                date_heure, 
                date_heure_RAW, 
                nombre_requetes_verrouillage, 
                nombre_requetes_verrouillage_RAW, 
                temps_attente_moyen, 
                temps_attente_moyen_RAW, 
                nombre_blocages, 
                nombre_blocages_RAW, 
                temps_mort, 
                temps_mort_RAW, 
                couverture, 
                couverture_RAW
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_sql_lock_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_swap_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
           # print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""INSERT INTO myreport_swap (
                date_heure, 
                date_heure_RAW, 
                Total, 
                Total_RAW, 
                temps_mort_mem, 
                temps_mort_mem_RAW,
                couverture_mem, 
                couverture_mem_RAW
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_swap_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_sql_statistic_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            #print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
           # print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_sql_statistic (
                date_heure, 
                date_heure_raw, 
                nombre_requetes_lots, 
                nombre_requetes_lots_raw, 
                compilations_sql, 
                compilations_sql_raw, 
                recompilations_sql, 
                recompilations_sql_raw, 
                temps_mort_pct, 
                temps_mort_raw, 
                couverture_pct, 
                couverture_raw
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_sql_statistic_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_espace_disque_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
           # print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_espace_disque (
                date_heure, 
                date_heure_raw, 
                somme, 
                somme_RAW, 
                octetLibreC, 
                octetLibreC_Raw, 
                espaceDisponibleC, 
                espaceDisponibleC_raw, 
                octetLibreD, 
                octetLibreD_Raw, 
                espaceDisponibleD, 
                espaceDisponibleD_raw, 
                temp_mort, 
                temp_mort_raw, 
                Couverture, 
                Couverture_raw
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_espace_disque_full.csv - ok")
conn.commit()

# Ouverture du fichier CSV et insertion des données
with open("/data/logServer/myreport_sql_general_full.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
           # print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            #print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        #print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("""
            INSERT INTO myreport_sql_general (
                date_heure, 
                date_heure_raw, 
                Connexions_user, 
                Connexions_user_raw, 
                Connexions, 
                Connexions_Raw, 
                Déconnexions, 
                Déconnexions_raw, 
                temp_mort, 
                temp_mort_raw, 
                Couverture, 
                Couverture_raw
            ) VALUES (
                %s, %s, %s, %s, 
                %s, %s, %s, %s, 
                %s, %s, %s, %s
            )
        """, tuple(row.values()))
log("myreport_sql_general_full.csv - ok")
conn.commit()

################################################################
with open("/data/dataset_LogETL_LogServer.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        # Debug print (optional)
        #print(values)
        cur.execute("""
              INSERT INTO dataset (
                  Date_et_heure,
                  Column_Name_Error,
                  Connection_Timeout_Error,
                  Create_TABLE_Error,
                  Date_Format_Error,
                  Field_Size_Error,
                  Guidez_Atelier_Error,
                  Index_Error,
                  Object_Reference_Error,
                  Other_Error,
                  Pre_Login_Error,
                  Primary_Key_Error,
                  SQL_Invalid_Query_Error,
                  SQL_Query_Timeout_Error,
                  Time_Format_Error,
                  Unique_Index_Error,
                  Value_DIV0_Error,
                  Value_NAME_Error,
                  Value_REF_Error,
                  Value_VALUE_Error,
                  Web_Service_Error,
                  ETL_Achats,
                  ETL_BEXT,
                  ETL_Chargement_PJ,
                  ETL_GLPI,
                  ETL_Heures_Chauffeurs,
                  ETL_JIRA,
                  ETL_KPI_ALDI,
                  ETL_Taxation,
                  ETL_Vue_Heures_Agregees,
                  ETL_sur_ordre,
                  ETL_API_JWT,
                  Tous_les_jours,
                  Toutes_les_semaines_le_dimanche,
                  Total_Errors,
                  nb_operations,
                  rows_added,
                  rows_updated,
                  rows_deleted,
                  Somme_Volume_Mo,
                  Somme_Debit_Mbit_s,
                  Trafic_entrant_Volume_o,
                  Trafic_entrant_Debit_o_s,
                  Trafic_sortant_Volume_o,
                  Trafic_sortant_Debit_o_s,
                  Paquets_Volume_o,
                  Paquets_Debit_o_s,
                  Paquets_rebus_Volume_o,
                  Paquets_rebus_Debit_o_s,
                  Paquets_envoyes_Volume_o,
                  Paquets_envoyes_Debit_o_s,
                  Monodiffusion_entrante_Volume_o,
                  Monodiffusion_entrante_Debit_o_s,
                  Monodiffusion_sortante_Volume_o,
                  Monodiffusion_sortante_Debit_o_s,
                  Paquets_non_monodiffusion_entrants_Volume_o,
                  Paquets_non_monodiffusion_entrants_Debit_o_s,
                  Paquets_non_monodiffusion_sortants_Volume_o,
                  Paquets_non_monodiffusion_sortants_Debit_o_s,
                  Entrants_rejetes_Volume_o,
                  Entrants_rejetes_Debit_o_s,
                  Couverture_reseau_pct,
                  Nombre_de_requetes_de_lots_sql_stat,
                  Compilations_SQL_s_sql_stat,
                  Recompilations_SQL_s_sql_stat,
                  requete_verrouillage_sql_lock_nb_s,
                  temps_attente_sql_lock_ms,
                  Connexions_utilisateur_nb,
                  Connexions_s_nb,
                  Deconnexions_s_nb,
                  Temps_du_ping_ms,
                  Maximum_ping_ms,
                  Perte_de_paquets_ping_pct,
                  Somme_espace_disque_Go,
                  Octets_libres_C_octets,
                  Espace_disponible_C_pct,
                  Octets_libres_D_octets,
                  Espace_disponible_D_pct,
                  total_swap_pct,
                  Memoire_de_connexion_sql_gestmemoire_Ko,
                  Memoire_de_l_optimiseur_sql_gestmemoire_Ko,
                  Memoire_totale_du_serveur_sql_gestmemoire_Ko,
                  Memoire_du_cache_SQL_sql_gestmemoire_Ko,
                  Memoire_disponible_ram_pct,
                  Memoire_disponible_ram_Go,
                  Couverture_ram_pct,
                  Somme_pct,
                  Processeur_1_pct,
                  Processeur_2_pct,
                  Processeur_3_pct,
                  Processeur_4_pct,
                  Processeur_5_pct,
                  Processeur_6_pct,
                  Processeur_7_pct,
                  Processeur_8_pct,
                  Temps_mort_cpu_pct,
                  Couverture_cpu_pct
              ) VALUES (
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s
              )
          """, tuple(row.values()))
log("dataset_LogETL_LogServer.csv - ok")
conn.commit()

# Valider les changements dans la base de données
#conn.commit()
"""on le fait a chaque .csv finalement"""

# Fermeture du curseur et de la connexion
cur.close()
conn.close()
log("Connexion PostgreSQL fermée")
log("exceution import_csv terminée")



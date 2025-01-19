import psycopg2
import csv


# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="DORdatabase",
    user="supever",
    password="DORsupever2025"
)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Ouverture du fichier CSV
with open("./data/logOK.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    for row in reader:
        # Insérer la ligne dans la base de données
        cur.execute("INSERT INTO logOK (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_Id, launcher_Name, program_id,program_name, schedules_id, schedules_name, schedules_startdatetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))

# Ouverture du fichier CSV
with open("./data/logERR.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    for row in reader:
        # Insérer la ligne dans la base de données
        cur.execute("INSERT INTO logERR (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_ping.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        print(reader.fieldnames)
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
        # Insérer la ligne dans la table
        cur.execute("INSERT INTO myreport_ping (date_et_heure, date_et_heure_raw, temps_du_ping, temps_du_ping_raw, minimum, minimum_raw, maximum, maximum_raw, perte_de_paquets, perte_de_paquets_raw, temps_mort, temps_mort_raw, couverture, couverture_raw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row.values()))

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_cpu.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_ram.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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


# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_reseau.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
        # Insérer la ligne dans la table
        print("Nombre de valeurs :", len(tuple(row.values())))
        cur.execute("""INSERT INTO myreport_reseau (
                Date, heureDate_RAW, Somme_Volume, Somme_Volume_RAW, 
                Somme_Debit, Somme_Debit_RAW, Trafic_Entrant_Volume, Trafic_Entrant_Volume_RAW,
                Trafic_Entrant_Debit, Trafic_Entrant_Debit_RAW, Trafic_Sortant_Volume, Trafic_Sortant_Volume_RAW,
                Trafic_Sortant_Debit, Trafic_Sortant_Debit_RAW, Paquets_Volume, Paquets_Volume_RAW,
                Paquets_Debit, Paquets_Debit_RAW, Paquets_Refus_Volume, Paquets_Refus_Volume_RAW,
                Paquets_Refus_Debit, Paquets_Refus_Debit_RAW, Paquets_Envoyes_Volume, Paquets_Envoyes_Volume_RAW,
                Paquets_Envoyes_Debit, Paquets_Envoyes_Debit_RAW, Monodiffusion_entrante_Volume, Monodiffusion_entrante_Volume_RAW,
                Monodiffusion_entrante_Debit, Monodiffusion_entrante_Debit_RAW, Monodiffusion_sortante_Volume, Monodiffusion_sortante_Volume_RAW,
                Monodiffusion_sortante_Debit, Monodiffusion_sortante_Debit_RAW, Paquets_non_monodiffusion_entrants_Volume, Paquets_non_monodiffusion_entrants_Volume_RAW,
                Paquets_non_monodiffusion_entrants_Debit, Paquets_non_monodiffusion_entrants_Debit_RAW, Paquets_non_monodiffusion_sortants_Volume, Paquets_non_monodiffusion_sortants_Volume_RAW,
                Paquets_non_monodiffusion_sortants_Debit, Paquets_non_monodiffusion_sortants_Debit_RAW, Erreurs_entrantes_Volume, Erreurs_entrantes_Volume_RAW,
                Erreurs_entrantes_Debit, Erreurs_entrantes_Debit_RAW, Erreurs_sortantes_Volume, Erreurs_sortantes_Volume_RAW,
                Erreurs_sortantes_Debit, Erreurs_sortantes_Debit_RAW, Entrants_rejets_Volume, Entrants_rejets_Volume_RAW,
                Entrants_rejets_Debit, Entrants_rejets_Debit_RAW, Sortants_rejets_Volume, Sortants_rejets_Volume_RAW,
                Sortants_rejets_Debit, Sortants_rejets_Debit_RAW, Protocoles_inconnus_entrants_Volume, Protocoles_inconnus_entrants_Volume_RAW,
                Protocoles_inconnus_entrants_Debit, Protocoles_inconnus_entrants_Debit_RAW, Temps_mort_cpu, Temps_mort_cpu_RAW,
                Couverture_cpu, Couverture_cpu_RAW
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
                %s, %s, %s, %s
            )
        """, tuple(row.values()))

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_memoire.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_sql_lock.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_swap.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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

# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_sql_statistic.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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


# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_espace_disque.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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


# Ouverture du fichier CSV et insertion des données
with open("./data/myreport_sql_general.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Passer la ligne d'en-tête si nécessaire
    for row in reader:
        if not row[reader.fieldnames[2]]:
            print("ligne ignorée")
            continue
        if any("Moyennes" in value for value in row.values()):
            print(f"Ligne ignorée (moyenne détectée) : {row}")
            continue
        print(tuple(row.values()))
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


# Valider les changements dans la base de données
conn.commit()

# Fermeture du curseur et de la connexion
cur.close()
conn.close()


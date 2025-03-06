-- Create the role 'supever' with the specified password
-- CREATE ROLE supever WITH LOGIN PASSWORD 'DORsupever2025';

-- Optionally, if you need superuser privileges:
-- ALTER ROLE supever WITH SUPERUSER;

-- create the table logOK;
CREATE TABLE IF NOT EXISTS logOK (
	ident BIGSERIAL, -- champs autoincrement
	dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
	server_version VARCHAR(255),
	client_version VARCHAR(255),
	model VARCHAR(255),
	type_log VARCHAR(255),
	insert_mode VARCHAR(255),
	rows_added REAL,
	rows_updated INTEGER,
	rows_deleted INTEGER,
	rows_in_error VARCHAR(255),
	rows_in_warning VARCHAR(255),
	colonne VARCHAR(255),
	dt_log DATE,
	start_time TIME,
	end_time TIME,
	duration VARCHAR(255),
	machine VARCHAR(255),
	session_log VARCHAR(255),
	project_name VARCHAR(255),
	product VARCHAR(255),
	resultat VARCHAR(255),
	etl_startdatetime TIMESTAMP,
	launcher_Id VARCHAR(255),
	launcher_Name VARCHAR(255),
	program_id VARCHAR(255),
	program_name VARCHAR(255),
	schedules_id VARCHAR(255),
	schedules_name VARCHAR(255),
	schedules_startdatetime TIMESTAMP
);

-- create the table logERR;
CREATE TABLE IF NOT EXISTS logERR (
	ident BIGSERIAL, -- champs autoincrement
	dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
	server_version VARCHAR(255),
	client_version VARCHAR(255),
	product VARCHAR(255),
	project_name VARCHAR(255),
	model VARCHAR(255),
	log_date DATE,
	log_time TIME,
	row_num INT,
	log_type VARCHAR(255),
	log_message TEXT,
	etl_start_datetime TIMESTAMP,
	launcher_id VARCHAR(255),
	launcher_name VARCHAR(255),
	machine VARCHAR(255),
	program_id VARCHAR(255),
	program_name VARCHAR(255),
	schedules_id VARCHAR(255),
	schedules_name VARCHAR(255),
	schedules_start_datetime TIMESTAMP,
    type_error TEXT
);

-- create the table myreport_ping;
CREATE TABLE IF NOT EXISTS myreport_ping (
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
	temps_du_ping varchar(255),
	temps_du_ping_raw decimal,
	minimum VARCHAR(255),
	minimum_raw decimal,
	maximum VARCHAR(255),
    	maximum_raw decimal,
    	perte_de_paquets VARCHAR(255),
    	perte_de_paquets_raw decimal,
    	temps_mort VARCHAR(255),
    	temps_mort_raw decimal,
    	couverture VARCHAR(255),
    	couverture_raw decimal
);

-- création de la table myreport_cpu
CREATE TABLE IF NOT EXISTS myreport_cpu
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    Somme VARCHAR(255),
    Somme_RAW REAL,
    Processeur_1 VARCHAR(255),
    Processeur_1_RAW REAL,
    Processeur_2 VARCHAR(255),
    Processeur_2_RAW REAL,
    Processeur_3 VARCHAR(255),
    Processeur_3_RAW REAL,
    Processeur_4 VARCHAR(255),
    Processeur_4_RAW REAL,
    Processeur_5 VARCHAR(255),
    Processeur_5_RAW REAL,
    Processeur_6 VARCHAR(255),
    Processeur_6_RAW REAL,
    Processeur_7 VARCHAR(255),
    Processeur_7_RAW REAL,
    Processeur_8 VARCHAR(255),
    Processeur_8_RAW REAL,
    Temps_mort_cpu VARCHAR(255),
    Temps_mort_cpu_RAW REAL,
    Couverture_cpu VARCHAR(255),
    Couverture_cpu_RAW REAL
);


-- création de la table myreport_ram
CREATE TABLE IF NOT EXISTS myreport_ram
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    memoire_disponible_pct VARCHAR(255),
    memoire_disponible_pct_RAW REAL,
    memoire_disponible_go VARCHAR(255),
    memoire_disponible_go_RAW REAL,
    temps_mort_pct VARCHAR(255),
    temps_mort_raw REAL,
    couverture_pct VARCHAR(255),
    couverture_raw REAL
);

-- création de la table myreport_reseau
CREATE TABLE IF NOT EXISTS myreport_reseau
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    Somme_Volume VARCHAR(255),
    Somme_Volume_RAW REAL,
    Somme_Debit VARCHAR(255),
    Somme_Debit_RAW REAL,
    Trafic_Entrant_Volume VARCHAR(255),
    Trafic_Entrant_Volume_RAW REAL,
    Trafic_Entrant_Debit VARCHAR(255),
    Trafic_Entrant_Debit_RAW REAL,
    Trafic_Sortant_Volume VARCHAR(255),
    Trafic_Sortant_Volume_RAW REAL,
    Trafic_Sortant_Debit VARCHAR(255),
    Trafic_Sortant_Debit_RAW REAL,
    Paquets_Volume VARCHAR(255),
    Paquets_Volume_RAW REAL,
    Paquets_Debit VARCHAR(255),
    Paquets_Debit_RAW REAL,
    Paquets_Refus_Volume VARCHAR(255),
    Paquets_Refus_Volume_RAW REAL,
    Paquets_Refus_Debit VARCHAR(255),
    Paquets_Refus_Debit_RAW REAL,
    Paquets_Envoyes_Volume VARCHAR(255),
    Paquets_Envoyes_Volume_RAW REAL,
    Paquets_Envoyes_Debit VARCHAR(255),
    Paquets_Envoyes_Debit_RAW REAL,
    Monodiffusion_entrante_Volume VARCHAR(255),
    Monodiffusion_entrante_Volume_RAW REAL,
    Monodiffusion_entrante_Debit VARCHAR(255),
    Monodiffusion_entrante_Debit_RAW REAL,
    Monodiffusion_sortante_Volume VARCHAR(255),
    Monodiffusion_sortante_Volume_RAW REAL,
    Monodiffusion_sortante_Debit VARCHAR(255),
    Monodiffusion_sortante_Debit_RAW REAL,
    Paquets_non_monodiffusion_entrants_Volume VARCHAR(255),
    Paquets_non_monodiffusion_entrants_Volume_RAW REAL,
    Paquets_non_monodiffusion_entrants_Debit VARCHAR(255),
    Paquets_non_monodiffusion_entrants_Debit_RAW REAL,
    Paquets_non_monodiffusion_sortants_Volume VARCHAR(255),
    Paquets_non_monodiffusion_sortants_Volume_RAW REAL,
    Paquets_non_monodiffusion_sortants_Debit VARCHAR(255),
    Paquets_non_monodiffusion_sortants_Debit_RAW REAL,
    Erreurs_entrantes_Volume VARCHAR(255),
    Erreurs_entrantes_Volume_RAW REAL,
    Erreurs_entrantes_Debit VARCHAR(255),
    Erreurs_entrantes_Debit_RAW REAL,
    Erreurs_sortantes_Volume VARCHAR(255),
    Erreurs_sortantes_Volume_RAW REAL,
    Erreurs_sortantes_Debit VARCHAR(255),
    Erreurs_sortantes_Debit_RAW REAL,
    Entrants_rejets_Volume VARCHAR(255),
    Entrants_rejets_Volume_RAW REAL,
    Entrants_rejets_Debit VARCHAR(255),
    Entrants_rejets_Debit_RAW REAL,
    Sortants_rejets_Volume VARCHAR(255),
    Sortants_rejets_Volume_RAW REAL,
    Sortants_rejets_Debit VARCHAR(255),
    Sortants_rejets_Debit_RAW REAL,
    Protocoles_inconnus_entrants_Volume VARCHAR(255),
    Protocoles_inconnus_entrants_Volume_RAW REAL,
    Protocoles_inconnus_entrants_Debit VARCHAR(255),
    Protocoles_inconnus_entrants_Debit_RAW REAL,
    Temps_mort VARCHAR(255),
    Temps_mort_RAW REAL,
    Couverture VARCHAR(255),
    Couverture_RAW REAL
);

-- création de la table myreport_memoire
CREATE TABLE IF NOT EXISTS myreport_memoire
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    MemConnexion VARCHAR(255),
    MemConnexion_RAW REAL,
    MemOptimiseur VARCHAR(255),
    MemOptimiseur_RAW REAL,
    MemTotaleServeur VARCHAR(255),
    MemTotaleServeur_RAW REAL,
    MemServeurCible VARCHAR(255),
    MemServeurCible_RAW REAL,
    MemeCacheSQL VARCHAR(255),
    MemeCacheSQL_RAW REAL,
    Temps_mort_mem VARCHAR(255),
    Temps_mort_mem_RAW REAL,
    Couverture_mem VARCHAR(255),
    Couverture_mem_RAW REAL
);

-- création de la table myreport_sql_lock
CREATE TABLE IF NOT EXISTS myreport_sql_lock
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    nombre_requetes_verrouillage VARCHAR(255),
    nombre_requetes_verrouillage_RAW REAL,
    temps_attente_moyen VARCHAR(255),
    temps_attente_moyen_RAW REAL,
    nombre_blocages VARCHAR(255),
    nombre_blocages_RAW REAL,
    temps_mort VARCHAR(255),
    temps_mort_RAW REAL,
    couverture VARCHAR(255),
    couverture_RAW REAL
);

-- création de la table myreport_swap
CREATE TABLE IF NOT EXISTS myreport_swap
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    Total VARCHAR(255),
    Total_RAW REAL,
    Temps_mort_mem VARCHAR(255),
    Temps_mort_mem_RAW REAL,
    Couverture_mem VARCHAR(255),
    Couverture_mem_RAW REAL
);

-- création de la table myreport_sql_statistic
CREATE TABLE IF NOT EXISTS myreport_sql_statistic
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    nombre_requetes_lots VARCHAR(255),
    nombre_requetes_lots_raw REAL,
    compilations_sql VARCHAR(255),
    compilations_sql_raw REAL,
    recompilations_sql VARCHAR(255),
    recompilations_sql_raw REAL,
    temps_mort_pct VARCHAR(255),
    temps_mort_raw REAL,
    couverture_pct VARCHAR(255),
    couverture_raw REAL
);


-- création de la table myreport_espace_disque
CREATE TABLE IF NOT EXISTS myreport_espace_disque
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
 	date_heure VARCHAR(255),
    date_heure_raw REAL,
    somme VARCHAR(255),
    somme_RAW REAL,
    octetLibreC VARCHAR(255),
    octetLibreC_Raw REAL,
    espaceDisponibleC VARCHAR(255),
    espaceDisponibleC_raw REAL,
    octetLibreD VARCHAR(255),
    octetLibreD_Raw REAL,
    espaceDisponibleD VARCHAR(255),
    espaceDisponibleD_raw REAL,
    temp_mort VARCHAR(255),
    temp_mort_raw REAL,
    Couverture VARCHAR(255),
    Couverture_raw REAL
);

-- création de la table myreport_sql_general
CREATE TABLE IF NOT EXISTS myreport_sql_general
(
	ident BIGSERIAL, -- champs autoincrement
    dt_insertion timestamp DEFAULT now(), -- champs watermark / windowed
	date_heure VARCHAR(255),
    date_heure_raw REAL,
    Connexions_user VARCHAR(255),
    Connexions_user_raw REAL,
    Connexions VARCHAR(255),
    Connexions_Raw REAL,
    Déconnexions VARCHAR(255),
    Déconnexions_raw REAL,
    temp_mort VARCHAR(255),
    temp_mort_raw REAL,
    Couverture VARCHAR(255),
    Couverture_raw REAL
);

-- création de la table DashboardLogs
CREATE TABLE IF NOT EXISTS DashboardLogs
(
	ident BIGSERIAL, -- champs autoincrement
    Id REAL,
	DatetimeLog VARCHAR(255),
    Login VARCHAR(255),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DashboardId VARCHAR(255),
    DashboardName VARCHAR(255),
    TabName VARCHAR(255),
    ExecutionGuid VARCHAR(255),
    IsEmbedded REAL
);

-- création de la table DistributionLogs
CREATE TABLE IF NOT EXISTS DistributionLogs
(
	ident BIGSERIAL, -- champs autoincrement
    Id REAL,
	DatetimeLog VARCHAR(255),
    Login VARCHAR(255),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DistributionId VARCHAR(255),
    DistributionName VARCHAR(255),
    IsError REAL,
    ScheduleId VARCHAR(255),
    ScheduleName VARCHAR(255),
    ExecutionGuid VARCHAR(255)
);

-- création de la table FieldLogs
CREATE TABLE IF NOT EXISTS FieldLogs
(
	ident BIGSERIAL, -- champs autoincrement
    Id REAL,
	DatetimeLog VARCHAR(255),
    ModelId VARCHAR(255),
    ModelName VARCHAR(255),
    TableId VARCHAR(255),
    TableName VARCHAR(255),
    RangeAddress VARCHAR(255),
    FieldId VARCHAR(255),
    FieldName VARCHAR(255),
    Login VARCHAR(255),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    ExecutionType VARCHAR(255),
    ExecutionGuid VARCHAR(255),
    WorkbookName VARCHAR(255),
    WorkbookPath VARCHAR(255),
    MachineName VARCHAR(255),
    DistributionId VARCHAR(255),
    DistributionName VARCHAR(255),
    ScheduleId VARCHAR(255),
    ScheduleName VARCHAR(255),
    DashboardId VARCHAR(255),
    DashboardName VARCHAR(255),
    TabName VARCHAR(255),
    IsEmbedded REAL,
    SessionName VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dataset
(
    date_and_heure TIMESTAMP,
    ColumnName_Error REAL,
    ConnectionTimeout_Error REAL,
    CreateTABLE_Error REAL,
    DateFormat_Error REAL,
    FieldSize_Error REAL,
    GuidezAtelier_Error REAL,
    IndexErrorSimilarToUniqueIndex_Error REAL,
    ObjectReference_Error REAL,
    Other_Error REAL,
    PreLogin_Error REAL,
    PrimaryKey_Error REAL,
    SQLQueryTimeout_Error REAL,
    TimeFormat_Error REAL,
    UniqueIndex_Error REAL,
    ValueDivBy0_Error REAL,
    ValueNAME_Error REAL,
    ValueREF_Error REAL,
    ValueVALUE_Error REAL,
    WebService_Error REAL,
    SQLInvalidQuery_Error REAL,
    ValueNA_Error REAL,
    DAILY REAL,

    ETL_API_JWT REAL,
    ETL_Achats REAL,
    ETL_BEXT REAL,
    ETL_Chargement_PJ REAL,
    ETL_GLPI REAL,
    ETL_Heures_Chauffeurs REAL,
    ETL_JIRA REAL,
    ETL_KPI_ALDI REAL,
    ETL_SUR_ORDRE REAL,
    ETL_TAXATION REAL,
    ETL_VUE_HEURE_AGG REAL,
    WEEKLY_SUNDAY REAL,
    PROG_INCONNU REAL,
    Total_Errors REAL,
    nb_operations REAL,
    rows_added REAL,
    rows_updated REAL,
    rows_deleted REAL,
    Somme_Volume_Mo REAL,
    Somme_Debit_Mbit_s REAL,

    Trafic_entrant_Volume_o REAL,
    Trafic_entrant_Debit_o_s REAL,
    Trafic_sortant_Volume_o REAL,
    Trafic_sortant_Debit_o_s REAL,
    Paquets_Volume_o REAL,
    Paquets_Debit_o_s REAL,
    Paquets_rebus_Volume_o REAL,
    Paquets_rebus_Debit_o_s REAL,
    Paquets_envoyes_Volume_o REAL,
    Paquets_envoyes_Debit_o_s REAL,
    Monodiffusion_entrante_Volume_o REAL,
    Monodiffusion_entrante_Debit_o_s REAL,
    Monodiffusion_sortante_Volume_o REAL,
    Monodiffusion_sortante_Debit_o_s REAL,
    Paquets_non_monodiffusion_entrants_Volume_o REAL,
    Paquets_non_monodiffusion_entrants_Debit_o_s REAL,
    Paquets_non_monodiffusion_sortants_Volume_o REAL,
    Paquets_non_monodiffusion_sortants_Debit_o_s REAL,
    Entrants_rejetes_Volume_o REAL,
    Entrants_rejetes_Debit_o_s REAL,
    Couverture_reseau_pct REAL,
    Nombre_de_requetes_de_lots_sql_stat REAL,
    Compilations_SQL_s_sql_stat REAL,
    Recompilations_SQL_s_sql_stat REAL,

    requete_verrouillage_sql_lock_nb_s REAL,
    temps_attente_sql_lock_ms REAL,
    Connexions_utilisateur_nb REAL,
    connexions_raw REAL,
    Deconnexions_s_nb REAL,
    Temps_du_ping_ms REAL,
    Maximum_ping_ms REAL,
    Perte_de_paquets_ping_pct REAL,
    Somme_espace_disque_Go REAL,
    octetlibrec_raw REAL,
    Espace_disponible_C_pct REAL,
    Octets_libres_D_octets REAL,
    Espace_disponible_D_pct REAL,
    total_swap REAL,
    Memoire_de_connexion_sql_gestmemoire_Ko REAL,
    Memoire_de_l_optimiseur_sql_gestmemoire_Ko REAL,
    Memoire_totale_du_serveur_sql_gestmemoire_Ko REAL,
    Memoire_du_cache_SQL_sql_gestmemoire_Ko REAL,
    memoire_disponible_pct_raw REAL,
    memoire_disponible_go_raw REAL,
    Couverture_ram_pct REAL,
    Somme_pct REAL,
    Processeur_1_pct REAL,
    Processeur_2_pct REAL,
    Processeur_3_pct REAL,
    Processeur_4_pct REAL,
    Processeur_5_pct REAL,
    Processeur_6_pct REAL,
    Processeur_7_pct REAL,
    Processeur_8_pct REAL,
    Temps_mort_cpu_pct REAL,
    Couverture_cpu_pct REAL
);

-- postgres est une base par défaut définie dans .env)
--création d'une base pour airflow
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO admin;

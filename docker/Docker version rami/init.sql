-- create the table "logOK";
CREATE TABLE logOK (
	ident BIGSERIAL, 
	dt_insertion timestamp, 
	server_version VARCHAR(255),
	client_version VARCHAR(255),
	model VARCHAR(255),
	type_log VARCHAR(255),
	insert_mode VARCHAR(255),
	rows_added INTEGER,
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

-- create the table "logERR";
CREATE TABLE logERR (
	ident BIGSERIAL,
	date_insertion TIMESTAMP, 
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
	schedules_start_datetime TIMESTAMP
);

-- create the table "myreport_ping";
CREATE TABLE myreport_ping (
	ident BIGSERIAL,
	date_et_heure varchar(255),
	date_et_heure_raw decimal,
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
	ident BIGSERIAL,
    Date VARCHAR(255),--il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
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
	ident BIGSERIAL,
	date_heure VARCHAR(30),
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
    ident BIGSERIAL,
    Date VARCHAR(255),--il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
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
	ident BIGSERIAL,
    Date VARCHAR(255), --il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
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
    ident BIGSERIAL,
	date_heure VARCHAR(255),
    date_heure_RAW REAL,
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
	ident BIGSERIAL,
    date_heure VARCHAR(255), --il y aura un traitement à faire sur les données
    date_heure_RAW REAL,
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
	ident BIGSERIAL,
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
	ident BIGSERIAL,
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
	ident BIGSERIAL,
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
	ident BIGSERIAL,
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
	ident BIGSERIAL,
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
	ident BIGSERIAL,
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
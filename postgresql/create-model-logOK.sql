-- author : Leyla - Manon
-- version : 0.1
-- contrib : 
-- description : script de creation de la table des log corrects 

-- delete the table if exist; 
drop table if exists "logOK" CASCADE;  

-- creation de la table
CREATE TABLE "logOK" (
	ident 						BIGSERIAL, 
	dt_insertion 				timestamp, 
	server_version 				VARCHAR(255),
	client_version 				VARCHAR(255),
	model 						VARCHAR(255),
	type_log 					VARCHAR(255),
	insert_mode 				VARCHAR(255),
	rows_added 					INTEGER,
	rows_updated 				INTEGER,
	rows_deleted 				INTEGER,
	rows_in_error 				VARCHAR(255),
	rows_in_warning 			VARCHAR(255),
	colonne 					VARCHAR(255),
	dt_log 						DATE,
	start_time 					TIME,
	end_time 					TIME,
	duration 					VARCHAR(255),
	machine 					VARCHAR(255),
	session_log 				VARCHAR(255),
	project_name 				VARCHAR(255),
	product 					VARCHAR(255),
	resultat 					VARCHAR(255),
	etl_startdatetime 			TIMESTAMP,
	launcher_Id 				VARCHAR(255),
	launcher_Name 				VARCHAR(255),
	program_id 					VARCHAR(255),
	program_name 				VARCHAR(255),
	schedules_id 				VARCHAR(255),
	schedules_name 				VARCHAR(255),
	schedules_startdatetime 	TIMESTAMP
);





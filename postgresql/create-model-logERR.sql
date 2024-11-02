-- author : Leyla - Manon
-- version : 0.1
-- contrib :
-- description : script de création de la table des logs erronés

-- delete the table if exists;
DROP TABLE IF EXISTS "logERR";

-- create the table "logERR";
CREATE TABLE "logERR" (
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
	log_message VARCHAR(255),
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
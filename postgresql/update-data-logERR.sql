-- author : Leyla - Manon
-- version : 0.1
-- contrib :
-- description : script d'update des logs erronés

-- delete the table if exists;

DROP TABLE IF EXISTS "logERR_tmp";

-- create the table "logERR_tmp";

CREATE TABLE "logERR_tmp" (
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

-- BEGIN FIX AREA
-- on insert les données dans la table temporaire

COPY "logERR_tmp" (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime)
FROM '../data/241016_LogETLError.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8'

-- QUOTE '\"'
-- ESCAPE ";"
;
-- END FIX AREA --


-- BEGIN TODO AREA
-- on effectue des transformations


-- END TODO AREA

-- on transfert les données dans la table finale

INSERT INTO "logERR" (server_version, client_version, product, project_name, model, 
log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, 
launcher_name, machine, program_id, program_name, schedules_id, schedules_name, 
schedules_start_datetime)

SELECT * FROM "logERR_tmp" ;

-- on efface la table temporaire
-- DROP TABLE "logERR_tmp"

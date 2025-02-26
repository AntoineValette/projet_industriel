-- Create the role 'supever' with the specified password
CREATE ROLE supever WITH LOGIN PASSWORD 'DORsupever2025';

-- Optionally, if you need superuser privileges:
ALTER ROLE supever WITH SUPERUSER;

-- create the table "logOK";
CREATE TABLE logOK (
	ident BIGSERIAL, 
	dt_insertion timestamp, 
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
	schedules_start_datetime TIMESTAMP,
	type_error TEXT
);

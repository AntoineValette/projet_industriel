-- author : Leyla - Manon
-- version : 0.1
-- contrib : 
-- description : script d'update des log corrects 

-- delete the table if exist; 
drop table if exists "logOK_tmp"; 

-- creation de la table
CREATE TABLE "logOK_tmp" (
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

-- BEGIN FIX AREA -- 
-- on insert les données dans la table temporaire
copy "logOK_tmp" (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime) 
FROM '../data/241016_LogETL.csv' 
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
insert into "logOK" (server_version, client_version, model, type_log, insert_mode, rows_added, 
rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, 
duration, machine, session_log, project_name, product, resultat, etl_startdatetime, launcher_id, 
launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime) 
select * from "logOK_tmp" ;


-- on efface la table temporaire 
-- DROP TABLE "logOK_tmp"



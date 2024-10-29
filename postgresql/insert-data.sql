-- delete the table if exist; 
drop table if exists 'logERR';  

-- creation de la table
CREATE TABLE logOK (
    Server_version VARCHAR(255),
    Client_version VARCHAR(255),
    Model VARCHAR(255),
    Type VARCHAR(255),
    Insert_mode VARCHAR(255),
    Rows_added INTEGER,
    Rows_updated INTEGER,
    Rows_deleted INTEGER,
    Rows_in_error VARCHAR(255),
    Rows_in_warning VARCHAR(255),
    Columns VARCHAR(255),
    Date DATE,
    Start_time TIME,
    End_time TIME,
    Duration VARCHAR(255),
    Machine VARCHAR(255),
    Session VARCHAR(255),
    Project_name VARCHAR(255),
    Product VARCHAR(255),
    Result VARCHAR(255),
    ETL_StartDateTime TIMESTAMP,
    Launcher_Id VARCHAR(255),
    Launcher_Name VARCHAR(255),
    Program_Id VARCHAR(255),
    Program_Name VARCHAR(255),
    Schedules_Id VARCHAR(255),
    Schedules_Name VARCHAR(255),
    Schedules_StartDateTime TIMESTAMP
);

-- copy des fichier

copy logERR (server_version,client_version,model,"type",
insert_mode,rows_added,rows_updated,rows_deleted,rows_in_error,
rows_in_warning,"columns", "date", 
start_time,end_time,duration,machine,"session",project_name,product,"result",etl_startdatetime,
launcher_id,launcher_name,program_id,program_name,schedules_id,schedules_name,schedules_startdatetime)

from '../data/241016_LogETL.csv' 
delimiter ';'
DELIMITER ';' CSV HEADER ENCODING 'UTF8' QUOTE '\"' ESCAPE "";""
csv HEADER ;
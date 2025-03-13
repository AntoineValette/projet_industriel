
INSERT INTO logerr (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error)
SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now(), launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))
ORDER BY RANDOM()
LIMIT 20; 

INSERT INTO logerr (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error)
SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))
ORDER BY RANDOM()
LIMIT 20; 

INSERT INTO logerr (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error)
SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR')) 
ORDER BY RANDOM()
LIMIT 20; 


INSERT INTO logok (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime)
SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now(), launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))
ORDER BY RANDOM()
LIMIT 200;  

INSERT INTO logok (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime)
SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))
ORDER BY RANDOM()
LIMIT 200; 

INSERT INTO logok (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime)
SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok where model not in (select model from logok 
where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))
ORDER BY RANDOM()
LIMIT 200; 

select * from logok 
where dt_insertion > NOW() - INTERVAL '1 HOUR'

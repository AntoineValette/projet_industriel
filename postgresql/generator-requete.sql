-- injection dans logERR
INSERT INTO logerr (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error)
(SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now(), launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT 10)
UNION (SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT 10)
UNION (SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT 10);

-- model in (select model from logok where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))

-- injection dans logOK
INSERT INTO logok (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime)
(SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now(), launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok ORDER BY RANDOM() LIMIT 200)
UNION (SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok ORDER BY RANDOM() LIMIT 200)
UNION (SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok where 1=1 ORDER BY RANDOM() LIMIT 200); 

select count(*) from logok 
where etl_start_datetime > NOW() - INTERVAL '1 HOUR'

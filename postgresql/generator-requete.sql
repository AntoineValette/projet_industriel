-- injection dans logERR
INSERT INTO logerr (server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, etl_start_datetime, launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error)
(SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now(), launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT (SELECT (random() * 9 + 1)::integer))
UNION (SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT (SELECT (random() * 9 + 1)::integer))
UNION (SELECT server_version, client_version, product, project_name, model, log_date, log_time, row_num, log_type, log_message, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, machine, program_id, program_name, schedules_id, schedules_name, schedules_start_datetime, type_error
FROM logerr ORDER BY RANDOM() LIMIT (SELECT (random() * 9 + 1)::integer));

-- model in (select model from logok where etl_start_datetime > (NOW() - INTERVAL '1 HOUR'))

-- injection dans logOK
INSERT INTO logok (server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, etl_start_datetime, launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime)
(SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now(), launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok ORDER BY RANDOM() LIMIT 200)
UNION (SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() + INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok ORDER BY RANDOM() LIMIT 200)
UNION (SELECT server_version, client_version, model, type_log, insert_mode, rows_added, rows_updated, rows_deleted, rows_in_error, rows_in_warning, colonne, dt_log, start_time, end_time, duration, machine, session_log, project_name, product, resultat, now() - INTERVAL '1 HOUR', launcher_id, launcher_name, program_id, program_name, schedules_id, schedules_name, schedules_startdatetime
FROM logok where 1=1 ORDER BY RANDOM() LIMIT 200); 

-- requete inject 
INSERT INTO myreport_cpu (
    date_heure, date_heure_raw, somme, somme_raw, processeur_1, processeur_1_raw,
    processeur_2, processeur_2_raw, processeur_3, processeur_3_raw, processeur_4,
    processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
    processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
    temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
)
(
(SELECT
    date_trunc('minute', now()), date_heure_raw, somme, somme_raw, processeur_1,
    processeur_1_raw, processeur_2, processeur_2_raw, processeur_3, processeur_3_raw,
    processeur_4, processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
    processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
    temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
FROM  myreport_cpu ORDER BY RANDOM() LIMIT 1)
UNION 
(SELECT
    date_trunc('minute', now() - interval '1 minute'), date_heure_raw, somme, somme_raw, processeur_1,
    processeur_1_raw, processeur_2, processeur_2_raw, processeur_3, processeur_3_raw,
    processeur_4, processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
    processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
    temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
FROM  myreport_cpu ORDER BY RANDOM() LIMIT 1
)
UNION 
(SELECT
    date_trunc('minute', now() - interval '2 minute'), date_heure_raw, somme, somme_raw, processeur_1,
    processeur_1_raw, processeur_2, processeur_2_raw, processeur_3, processeur_3_raw,
    processeur_4, processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
    processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
    temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
FROM  myreport_cpu ORDER BY RANDOM() LIMIT 1
)UNION 
(SELECT
    date_trunc('minute', now() - interval '3 minute'), date_heure_raw, somme, somme_raw, processeur_1,
    processeur_1_raw, processeur_2, processeur_2_raw, processeur_3, processeur_3_raw,
    processeur_4, processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
    processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
    temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
FROM  myreport_cpu ORDER BY RANDOM() LIMIT 1
)
)
;


do $$
declare
    start   timestamp:='2023-03-14 03:12:20';
    stop    timestamp:=now();
    step    interval :='40 minutes';
    counter timestamp;
begin
    for counter in select generate_series(start,stop,step) loop
        raise notice 'counter: %', counter;
		
		INSERT INTO myreport_cpu (
            date_heure, date_heure_raw, somme, somme_raw, processeur_1, processeur_1_raw,
            processeur_2, processeur_2_raw, processeur_3, processeur_3_raw, processeur_4,
            processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
            processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
            temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
        )
        SELECT
            current_time, date_heure_raw, somme, somme_raw, processeur_1,
            processeur_1_raw, processeur_2, processeur_2_raw, processeur_3, processeur_3_raw,
            processeur_4, processeur_4_raw, processeur_5, processeur_5_raw, processeur_6, processeur_6_raw,
            processeur_7, processeur_7_raw, processeur_8, processeur_8_raw, temps_mort_cpu,
            temps_mort_cpu_raw, couverture_cpu, couverture_cpu_raw
        FROM
            myreport_cpu
        ORDER BY
            RANDOM()
        LIMIT 1;

		
    end loop;
end $$;
        





select count(*) as "NbError" from logERR 
where etl_start_datetime > NOW() - INTERVAL '1 HOUR'

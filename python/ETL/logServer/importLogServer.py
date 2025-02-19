from ETL.logServer.myreport_cpu_full import import_myreport_cpu_full
from ETL.logServer.myreport_espace_disque_full import import_myreport_espace_disque_full
from ETL.logServer.myreport_ping_full import import_myreport_ping_full
from ETL.logServer.myreport_ram_full import import_myreport_ram_full
from ETL.logServer.myreport_reseau_full import import_myreport_reseau_full
from ETL.logServer.myreport_sql_general_full import import_myreport_sql_general_full
from ETL.logServer.myreport_sql_gestionairedememoire_full import import_myreport_sql_gestionairedememoire_full
from ETL.logServer.myreport_sql_lock_full import import_myreport_sql_lock_full
from ETL.logServer.myreport_sql_statistic_full import import_myreport_sql_statistic_full
from ETL.logServer.myreport_swap_full import import_myreport_swap_full

def import_log_server():
    import_myreport_cpu_full()
    import_myreport_espace_disque_full()
    import_myreport_ping_full()
    import_myreport_ram_full()
    import_myreport_reseau_full()
    import_myreport_sql_general_full()
    import_myreport_sql_gestionairedememoire_full()
    import_myreport_sql_lock_full()
    import_myreport_sql_statistic_full()
    import_myreport_swap_full()
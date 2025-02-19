from ETL.logServer.myreport_cpu_full import importMyreport_cpu_full
from ETL.logServer.myreport_espace_disque_full import importMyreport_espace_disque_full
from ETL.logServer.myreport_ping_full import importMyreport_ping_full
from ETL.logServer.myreport_ram_full import importMyreport_ram_full
from ETL.logServer.myreport_reseau_full import importMyreport_reseau_full
from ETL.logServer.myreport_sql_general_full import importMyreport_sql_general_full
from ETL.logServer.myreport_sql_gestionairedememoire_full import importMyreport_sql_gestionairedememoire_full
from ETL.logServer.myreport_sql_lock_full import importMyreport_sql_lock_full
from ETL.logServer.myreport_sql_statistic_full import importMyreport_sql_statistic_full
from ETL.logServer.myreport_swap_full import importMyreport_swap_full

def importLogServer():
    importMyreport_cpu_full()
    importMyreport_espace_disque_full()
    importMyreport_ping_full()
    importMyreport_ram_full()
    importMyreport_reseau_full()
    importMyreport_sql_general_full()
    importMyreport_sql_gestionairedememoire_full()
    importMyreport_sql_lock_full()
    importMyreport_sql_statistic_full()
    importMyreport_swap_full()
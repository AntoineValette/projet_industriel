from ETL.logServer.myreport_cpu import myreport_cpu
from ETL.logServer.myreport_espace_disque import myreport_espace_disque
from ETL.logServer.myreport_ping import myreport_ping
from ETL.logServer.myreport_ram import myreport_ram
from ETL.logServer.myreport_reseau import myreport_reseau
from ETL.logServer.myreport_sql_general import myreport_sql_general
from ETL.logServer.myreport_sql_gestionairedememoire import myreport_sql_gestionairedememoire
from ETL.logServer.myreport_sql_lock import myreport_sql_lock
from ETL.logServer.myreport_sql_statistic import myreport_sql_statistic
from ETL.logServer.myreport_swap import myreport_swap

def logServer():
    myreport_cpu()
    myreport_espace_disque()
    myreport_ping()
    myreport_ram()
    myreport_reseau()
    myreport_sql_general()
    myreport_sql_gestionairedememoire()
    myreport_sql_lock()
    myreport_sql_statistic()
    myreport_swap()

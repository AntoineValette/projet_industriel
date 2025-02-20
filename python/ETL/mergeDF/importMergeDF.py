import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def importMergeDF():
    log("Connexion à PostgreSQL établie dans import_csv")
    conn = psycopg2.connect(Settings.POSTGRES_URL)
    cur = conn.cursor()

    log("import de dataset_LogETL_LogServer")
    filename = "/data/dataset_LogETL_LogServer.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                cur.execute("""
                      INSERT INTO dataset (
                          time,
                          Column_Name_Error,
                          Connection_Timeout_Error,
                          Create_TABLE_Error,
                          Date_Format_Error,
                          Field_Size_Error,
                          Guidez_Atelier_Error,
                          Index_Error,
                          Object_Reference_Error,
                          Other_Error,
                          Pre_Login_Error,
                          Primary_Key_Error,
                          SQL_Invalid_Query_Error,
                          SQL_Query_Timeout_Error,
                          Time_Format_Error,
                          Unique_Index_Error,
                          Value_DIV0_Error,
                          Value_NAME_Error,
                          Value_REF_Error,
                          Value_VALUE_Error,
                          Web_Service_Error,
                          ETL_Achats,
                          ETL_BEXT,
                          ETL_Chargement_PJ,
                          ETL_GLPI,
                          ETL_Heures_Chauffeurs,
                          ETL_JIRA,
                          ETL_KPI_ALDI,
                          ETL_Taxation,
                          ETL_Vue_Heures_Agregees,
                          ETL_sur_ordre,
                          ETL_API_JWT,
                          Tous_les_jours,
                          Toutes_les_semaines_le_dimanche,
                          Total_Errors,
                          nb_operations,
                          rows_added,
                          rows_updated,
                          rows_deleted,
                          Somme_Volume_Mo,
                          Somme_Debit_Mbit_s,
                          Trafic_entrant_Volume_o,
                          Trafic_entrant_Debit_o_s,
                          Trafic_sortant_Volume_o,
                          Trafic_sortant_Debit_o_s,
                          Paquets_Volume_o,
                          Paquets_Debit_o_s,
                          Paquets_rebus_Volume_o,
                          Paquets_rebus_Debit_o_s,
                          Paquets_envoyes_Volume_o,
                          Paquets_envoyes_Debit_o_s,
                          Monodiffusion_entrante_Volume_o,
                          Monodiffusion_entrante_Debit_o_s,
                          Monodiffusion_sortante_Volume_o,
                          Monodiffusion_sortante_Debit_o_s,
                          Paquets_non_monodiffusion_entrants_Volume_o,
                          Paquets_non_monodiffusion_entrants_Debit_o_s,
                          Paquets_non_monodiffusion_sortants_Volume_o,
                          Paquets_non_monodiffusion_sortants_Debit_o_s,
                          Entrants_rejetes_Volume_o,
                          Entrants_rejetes_Debit_o_s,
                          Couverture_reseau_pct,
                          Nombre_de_requetes_de_lots_sql_stat,
                          Compilations_SQL_s_sql_stat,
                          Recompilations_SQL_s_sql_stat,
                          requete_verrouillage_sql_lock_nb_s,
                          temps_attente_sql_lock_ms,
                          Connexions_utilisateur_nb,
                          Connexions_s_nb,
                          Deconnexions_s_nb,
                          Temps_du_ping_ms,
                          Maximum_ping_ms,
                          Perte_de_paquets_ping_pct,
                          Somme_espace_disque_Go,
                          Octets_libres_C_octets,
                          Espace_disponible_C_pct,
                          Octets_libres_D_octets,
                          Espace_disponible_D_pct,
                          total_swap_pct,
                          Memoire_de_connexion_sql_gestmemoire_Ko,
                          Memoire_de_l_optimiseur_sql_gestmemoire_Ko,
                          Memoire_totale_du_serveur_sql_gestmemoire_Ko,
                          Memoire_du_cache_SQL_sql_gestmemoire_Ko,
                          Memoire_disponible_ram_pct,
                          Memoire_disponible_ram_Go,
                          Couverture_ram_pct,
                          Somme_pct,
                          Processeur_1_pct,
                          Processeur_2_pct,
                          Processeur_3_pct,
                          Processeur_4_pct,
                          Processeur_5_pct,
                          Processeur_6_pct,
                          Processeur_7_pct,
                          Processeur_8_pct,
                          Temps_mort_cpu_pct,
                          Couverture_cpu_pct
                      ) VALUES (
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s
                      )
                  """, tuple(row.values()))
        log("dataset_LogETL_LogServer [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")


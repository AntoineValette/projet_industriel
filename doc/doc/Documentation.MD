
````
├── README.md
├── conf
│   ├── airflow
│   │   └── plugins
│   ├── grafana
│   │   ├── dashboards
│   │   │   ├── Dashboard Analytics des ETL.json
│   │   │   ├── ETL - jour vs. heure.json
│   │   │   ├── Modèle en erreur.json
│   │   │   ├── MyReport Synthèse.json
│   │   │   ├── myreport_cpu.json
│   │   │   ├── myreport_espace_disque.json
│   │   │   ├── myreport_memoire.json
│   │   │   ├── myreport_ping.json
│   │   │   ├── myreport_ram.json
│   │   │   ├── myreport_reseau.json
│   │   │   ├── myreport_sql_general.json
│   │   │   ├── myreport_sql_lock.json
│   │   │   ├── myreport_sql_statistic.json
│   │   │   └── myreport_swap.json
│   │   └── provisioning
│   │       ├── alerting
│   │       │   ├── alertrule.yaml
│   │       │   └── contactpoints.yaml
│   │       ├── dashboards
│   │       │   └── dashboards.yaml
│   │       └── datasources
│   │           └── datasource.yaml
│   └── postgresql
│       └── servers.json
├── data
│   ├── logETL
│   │   ├── 241016_LogETL.csv
│   │   ├── 241016_LogETLError.csv
│   │   └── LogETLError_20250130.csv
│   ├── logParquet
│   │   ├── DetailedDistributionLogs_sub_2411222036.parquet
│   │   ├── DetailedFieldLogs_sub_2412021040.parquet
│   │   └── LogETL_20250130.csv_sub_2501301744.parquet
│   └── logServer
│       ├── myreport_cpu_full.csv
│       ├── myreport_espace_disque_full.csv
│       ├── myreport_ping_full.csv
│       ├── myreport_ram_full.csv
│       ├── myreport_reseau_full.csv
│       ├── myreport_sql_general_full.csv
│       ├── myreport_sql_gestionairedememoire_full.csv
│       ├── myreport_sql_lock_full.csv
│       ├── myreport_sql_statistic_full.csv
│       └── myreport_swap_full.csv
├── doc
│   ├── presentation-intermediaire
│   │   ├── P2025_PROJET07_Rapport-étape-v1.docx
│   │   ├── P2025_PROJET07_Rapport-étape.pdf
│   │   └── PPT Point d'étape - Projet Industriel - v3.pptx
│   └── schemas
│       ├── AMDEC.xlsx
│       ├── Schéma Contexte Primever drawio.drawio.png
│       ├── schema-composants.drawio
│       └── schemas-powerpoint.pptx
├── docker
│   ├── airflow
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── requirements.txt
│   ├── kafka
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── python
│       ├── Dockerfile
│       └── requirements.txt
├── docker-compose.yml
├── notebook
│   ├── experiment
│   │   ├── Leyla_logERR.ipynb
│   │   └── test-manon.ipynb
│   ├── fusion
│   │   ├── fusion_log-logerror.ipynb
│   │   └── log_fusion_analyse.ipynb
│   ├── logEtl
│   │   ├── ML_logs.ipynb
│   │   └── old
│   │       ├── EDA_logs.ipynb
│   │       ├── EDA_logs_erreur.ipynb
│   │       ├── EDA_mixte.ipynb
│   │       ├── EDA_mixte_V2.ipynb
│   │       └── LogETLError_20250130.ipynb
│   ├── logParquet
│   │   ├── ActivityLog_20250130.csv_sub_2501301739.ipynb
│   │   ├── DetailedDashboardLogs_sub_2411222036.ipynb
│   │   ├── DetailedDistributionLogs_sub_2411222036.ipynb
│   │   ├── DetailedFieldLogs_sub_2412021040.ipynb
│   │   ├── LogETL_20250130.csv_sub_2501301744.ipynb
│   │   └── LogExpedition_20250130.csv_sub_2501301751.ipynb
│   └── logServer
│       ├── myreport_cpu_full.ipynb
│       ├── myreport_espace_disque_full.ipynb
│       ├── myreport_ping_full.ipynb
│       ├── myreport_ram_full.ipynb
│       ├── myreport_reseau_full.ipynb
│       ├── myreport_sql_general_full.ipynb
│       ├── myreport_sql_gestionairedememoire_full.ipynb
│       ├── myreport_sql_lock_full.ipynb
│       ├── myreport_sql_statistic_full.ipynb
│       └── myreport_swap_full.ipynb
├── postgresql
│   ├── generator-requete.sql
│   ├── init.sql
│   ├── logETL
│   │   ├── create-logERR.sql
│   │   └── create-logOK.sql
│   ├── mergedDF
│   │   └── mergedDF.sql
│   └── myReport
│       ├── myreport_cpu.sql
│       ├── myreport_cpu_full.sql
│       ├── myreport_espace_disque_full.sql
│       ├── myreport_ram_full.sql
│       ├── myreport_reseau_full.sql
│       ├── myreport_sql_general_full.sql
│       ├── myreport_sql_gestionnairedememoire_full.sql
│       ├── myreport_sql_lock_full.sql
│       ├── myreport_sql_statistic_full.sql
│       └── myreport_swap_full.sql
├── python
│   ├── ETL
│   │   ├── logETL
│   │   │   ├── logETL.py
│   │   │   └── logETLError.py
│   │   ├── logParquet
│   │   │   └── import_parquet.py
│   │   ├── logServer
│   │   │   ├── logServer.py
│   │   │   ├── myreport_cpu.py
│   │   │   ├── myreport_espace_disque.py
│   │   │   ├── myreport_ping.py
│   │   │   ├── myreport_ram.py
│   │   │   ├── myreport_reseau.py
│   │   │   ├── myreport_sql_general.py
│   │   │   ├── myreport_sql_gestionairedememoire.py
│   │   │   ├── myreport_sql_lock.py
│   │   │   ├── myreport_sql_statistic.py
│   │   │   └── myreport_swap.py
│   │   ├── mergeDF
│   │   │   └── mergeDF.py
│   │   └── myReport
│   │       └── myReport.py
│   ├── consumer.py
│   ├── core
│   │   ├── classification_error.py
│   │   ├── log.py
│   │   └── settings.py
│   ├── dags
│   │   ├── classification_error.py
│   │   ├── db_utils.py
│   │   ├── filtrage_logs_server.py
│   │   ├── fusion_dag.py
│   │   └── test_dag.py
│   ├── kfk
│   │   ├── consumer
│   │   │   └── consumer.py
│   │   └── producer
│   │       └── producer.py
│   ├── producer.py
│   ├── smartETL.py
│   └── waiting                     
│       ├── wait_for_import.py
│       ├── wait_for_kafka.py
│       └── wait_for_postgres.py
├── requirements.txt
└── ruff.toml                       -> configuration des linter python 
````
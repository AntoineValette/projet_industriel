-- author : Antoine
-- version : 0.1
-- contrib :
-- description : script de création de la table CPU

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_cpu;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_cpu
(
	ident BIGSERIAL,
    Date VARCHAR(255),--il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
    Somme VARCHAR(255),
    Somme_RAW REAL,
    Processeur_1 VARCHAR(255),
    Processeur_1_RAW REAL,
    Processeur_2 VARCHAR(255),
    Processeur_2_RAW REAL,
    Processeur_3 VARCHAR(255),
    Processeur_3_RAW REAL,
    Processeur_4 VARCHAR(255),
    Processeur_4_RAW REAL,
    Processeur_5 VARCHAR(255),
    Processeur_5_RAW REAL,
    Processeur_6 VARCHAR(255),
    Processeur_6_RAW REAL,
    Processeur_7 VARCHAR(255),
    Processeur_7_RAW REAL,
    Processeur_8 VARCHAR(255),
    Processeur_8_RAW REAL,
    Temps_mort_cpu VARCHAR(255),
    Temps_mort_cpu_RAW REAL,
    Couverture_cpu VARCHAR(255),
    Couverture_cpu_RAW REAL
);

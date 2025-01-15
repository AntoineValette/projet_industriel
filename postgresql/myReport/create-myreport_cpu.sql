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
    Somme REAL,
    Somme_RAW REAL,
    Processeur_1 REAL,
    Processeur_1_RAW REAL,
    Processeur_2 REAL,
    Processeur_2_RAW REAL,
    Processeur_3 REAL,
    Processeur_3_RAW REAL,
    Processeur_4 REAL,
    Processeur_4_RAW REAL,
    Processeur_5 REAL,
    Processeur_5_RAW REAL,
    Processeur_6 REAL,
    Processeur_6_RAW REAL,
    Processeur_7 REAL,
    Processeur_7_RAW REAL,
    Processeur_8 REAL,
    Processeur_8_RAW REAL,
    Temps_mort_cpu REAL,
    Temps_mort_cpu_RAW REAL,
    Couverture_cpu REAL,
    Couverture_cpu_RAW REAL
);

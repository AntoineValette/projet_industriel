-- author : Antoine
-- version : 0.1
-- contrib :
-- description : script de création de la table swap_full

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_swap_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_swap_full
(
	ident BIGSERIAL,
    Date VARCHAR(255), --il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
    Total VARCHAR(255),
    Total_RAW REAL,
    Temps_mort_mem VARCHAR(255),
    Temps_mort_mem_RAW REAL,
    Couverture_mem VARCHAR(255),
    Couverture_mem_RAW REAL
);

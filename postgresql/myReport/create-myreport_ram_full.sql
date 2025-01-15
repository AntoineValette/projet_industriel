-- author : Leyla
-- version : 0.1
-- contrib :
-- description : script de création de la table de la RAM pleine (RAM full)

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_ram_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_ram_full
(
	ident BIGSERIAL,
	date_heure VARCHAR(30),
    date_heure_raw REAL,
    memoire_disponible_pct REAL,
    memoire_disponible_pct_RAW REAL
    memoire_disponible_go REAL,
    memoire_disponible_go_RAW REAL,
    temps_mort_pct REAL,
    temps_mort_raw REAL,
    couverture_pct REAL,
    couverture_raw REAL
);

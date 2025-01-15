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
    date_insertion TIMESTAMP DEFAULT now(), -- modification pour fix bug 
	date_heure VARCHAR(30),
    date_heure_raw VARCHAR(30),
    memoire_disponible_pct VARCHAR(25),
    memoire_disponible_pct_raw VARCHAR(50),
    memoire_disponible_go VARCHAR(30),
    memoire_disponible_raw VARCHAR(30),
    temps_mort_pct VARCHAR(20),
    temps_mort_raw VARCHAR(20),
    couverture_pct VARCHAR(15),
    couverture_raw VARCHAR(50)
);

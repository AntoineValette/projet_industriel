-- author : Leyla
-- version : 0.1
-- contrib : 
-- description : script de création de la table des performances des verrouillages SQL

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_sql_lock_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_sql_lock_full
(
    ident BIGSERIAL,
	date_insertion TIMESTAMP DEFAULT now(), -- modification pour fix bug
	date_heure VARCHAR(40),
    date_heure_raw VARCHAR(30),
    nombre_requetes_verrouillage VARCHAR(40),
    nombre_requetes_verrouillage_raw VARCHAR(45),
    temps_attente_moyen VARCHAR(25),
    temps_attente_moyen_raw VARCHAR(27),
    nombre_blocages VARCHAR(20),
    nombre_blocages_raw VARCHAR(25),
    temps_mort_pct VARCHAR(20),
    temps_mort_raw VARCHAR(20),
    couverture_pct VARCHAR(15),
    couverture_raw VARCHAR(15)
);

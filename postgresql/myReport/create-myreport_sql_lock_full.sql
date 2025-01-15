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
	date_heure VARCHAR(255),
    date_heure_RAW REAL,
    nombre_requetes_verrouillage REAL,
    nombre_requetes_verrouillage_RAW REAL,
    temps_attente_moyen REAL,
    temps_attente_moyen_RAW REAL,
    nombre_blocages REAL,
    nombre_blocages_RAW REAL,
    temps_mort REAL,
    temps_mort_RAW REAL,
    couverture REAL,
    couverture_RAW REAL
);

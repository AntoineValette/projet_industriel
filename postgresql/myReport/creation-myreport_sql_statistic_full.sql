-- author : Leyla
-- version : 0.1
-- contrib : 
-- description : script de création de la table des statistiques détaillées des performances SQL

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_sql_statistic_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_sql_statistic_full
(
	ident BIGSERIAL,
    date_heure VARCHAR(255),
    date_heure_raw REAL,
    nombre_requetes_lots REAL,
    nombre_requetes_lots_raw REAL,
    compilations_sql REAL,
    compilations_sql_raw REAL,
    recompilations_sql REAL,
    recompilations_sql_raw REAL,
    temps_mort_pct REAL,
    temps_mort_raw REAL,
    couverture_pct REAL,
    couverture_raw REAL
);
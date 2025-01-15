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
    date_heure_raw VARCHAR(20),
    nombre_requetes_lots VARCHAR(35),
    nombre_requetes_lots_raw VARCHAR(40),
    compilations_sql VARCHAR(25),
    compilations_sql_raw VARCHAR(30),
    recompilations_sql VARCHAR(30),
    recompilations_sql_raw VARCHAR(35),
    temps_mort_pct VARCHAR(20),
    temps_mort_raw VARCHAR(20),
    couverture_pct VARCHAR(20),
    couverture_raw VARCHAR(20)
);
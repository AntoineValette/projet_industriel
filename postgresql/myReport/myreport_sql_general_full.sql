-- author : manon
-- version : 0.1
-- contrib :
-- description : espace disque full

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_sql_general_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_sql_general_full
(
	ident BIGSERIAL,
	date_heure VARCHAR(255),
    date_heure_raw REAL,
    Connexions_user VARCHAR(255),
    Connexions_user_raw REAL,
    Connexions VARCHAR(255),
    Connexions_Raw REAL,
    Déconnexions VARCHAR(255),
    Déconnexions_raw REAL,
    temp_mort VARCHAR(255),
    temp_mort_raw REAL,
    Couverture VARCHAR(255),
    Couverture_raw REAL
);

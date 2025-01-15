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
    date_insertion TIMESTAMP DEFAULT now(),
	date_heure VARCHAR(30),
    date_heure_raw VARCHAR(30),
    Connexions_user VARCHAR(50),
    Connexions_user_raw VARCHAR(50),
    Connexions VARCHAR(50),
    Connexions_Raw VARCHAR(50),
    Déconnexions VARCHAR(50),
    Déconnexions_raw VARCHAR(50),
    temp_mort VARCHAR(50),
    temp_mort_raw VARCHAR(50),
    Couverture VARCHAR(50),
    Couverture_raw VARCHAR(50),

);

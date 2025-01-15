-- author : manon
-- version : 0.1
-- contrib :
-- description : espace disque full

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_espace_disque_full;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_espace_disque_full
(
	ident BIGSERIAL,
	date_heure VARCHAR(255),
    date_heure_raw REAL,
    somme VARCHAR(255),
    somme_RAW REAL,
    octetLibreC VARCHAR(255),
    octetLibreC_Raw REAL,
    espaceDisponibleC VARCHAR(255),
    espaceDisponibleC_raw REAL,
    octetLibreD VARCHAR(255),
    octetLibreD_Raw REAL,
    espaceDisponibleD VARCHAR(255),
    espaceDisponibleD_raw REAL,
    temp_mort VARCHAR(255),
    temp_mort_raw REAL,
    Couverture VARCHAR(255),
    Couverture_raw REAL
);

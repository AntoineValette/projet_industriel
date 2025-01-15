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
    date_insertion TIMESTAMP DEFAULT now(),
	date_heure VARCHAR(30),
    date_heure_raw VARCHAR(30),
    somme VARCHAR(50),
    somme_RAW VARCHAR(50),
    octetLibreC VARCHAR(40),
    octetLibreC_Raw VARCHAR(50),
    espaceDisponibleC VARCHAR(50),
    espaceDisponibleC_raw VARCHAR(50),
    octetLibreD VARCHAR(50),
    octetLibreD_Raw VARCHAR(50),
    espaceDisponibleD VARCHAR(50),
    espaceDisponibleD_raw VARCHAR(50),
    temp_mort VARCHAR(50),
    temp_mort_raw VARCHAR(50),
    Couverture VARCHAR(50),
    Couverture_raw VARCHAR(50),

);

-- author : Antoine
-- version : 0.1
-- contrib :
-- description : script de création de la table gestionnairedememoire

-- suppression de la table si elle existe
DROP TABLE IF EXISTS myreport_memoire;

-- création de la table
CREATE TABLE IF NOT EXISTS myreport_memoire
(
	ident BIGSERIAL,
    Date VARCHAR(255), --il y aura un traitement à faire sur les données
    heureDate_RAW REAL,
    MemConnexion VARCHAR(255),
    MemConnexion_RAW REAL,
    MemOptimiseur VARCHAR(255),
    MemOptimiseur_RAW REAL,
    MemTotaleServeur VARCHAR(255),
    MemTotaleServeur_RAW REAL,
    MemServeurCible VARCHAR(255),
    MemServeurCible_RAW REAL,
    MemeCacheSQL VARCHAR(255),
    MemeCacheSQL_RAW REAL,
    Temps_mort_mem VARCHAR(255),
    Temps_mort_mem_RAW REAL,
    Couverture_mem VARCHAR(255),
    Couverture_mem_RAW REAL
);

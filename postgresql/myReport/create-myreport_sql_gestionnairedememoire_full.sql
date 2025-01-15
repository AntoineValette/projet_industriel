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
    MemConnexion REAL,
    MemConnexion_RAW REAL,
    MemOptimiseur REAL,
    MemOptimiseur_RAW REAL,
    MemTotaleServeur REAL,
    MemTotaleServeur_RAW REAL,
    MemServeurCible REAL,
    MemServeurCible_RAW REAL,
    MemeCacheSQL REAL,
    MemeCacheSQL_RAW REAL,
    Temps_mort_mem REAL,
    Temps_mort_mem_RAW REAL,
    Couverture_mem REAL,
    Couverture_mem_RAW REAL
);

-- "Server version";"Client version";"Product";"Project name";"Model";"Date";"Time";"Row number";"Type";"Message";"ETL_StartDateTime";"Launcher_Id";"Launcher_Name";"Machine";"Program_Id";"Program_Name";"Schedules_Id";"Schedules_Name";"Schedules_StartDateTime"
-- "6.0.2";"6.0.2";"MyReport Server BE";"MySystem BE";"TMS/MF_Factures";"2024-08-25";"1:15:41.6121442";"0";"Erreur";"Impossible d'ouvrir la requête SQL sur la connexion TMS Le délai d'attente a été dépassé  Requête SQL SELECT DISTINCT     TMS_T_FACTURE."IDFacture" AS IDFACTURE_0,     TMS_T_FACTUREDETAIL."IDFactureDetail" AS IDFACTUREDETAIL_1,     CASE WHEN NOT (TMS_T_FACTUREDETAIL."IDOrdreTaxationTiers" IS NULL) THEN TMS_T_FACTUREDETAIL."IDOrdreTaxationTiers" ELSE TMS_T_FACTUREDETAIL."IDOrdreTaxationTiersReprise" END AS CALC_2,     TMS_T_FACTUREDETAIL."IdTourneeMoyen" AS IDTOURNEEMOYEN_3,     DBO_TMS_T_TOURNEEMOYEN."IDTournee" AS IDTOURNEE_4,     TMS_T_FACTUREDETAIL."LigneFacture" AS LIGNEFACTURE_5,     TMS_T_FACTURE."NumFacture" AS NUMFACTURE_6,     TMS_T_FACTUREDETAIL."ReferenceCommande" AS REFERENCECOMMANDE_7,     TMS_T_FACTURE."DateHeureCreation" AS DATEHEURECREATION_8,     TMS_T_FACTURE."DateHeureModif" AS DATEHEUREMODIF_9,     TMS_T_FACTUREDETAIL."DateHeureModif" AS DATEHEUREMODIF_10,     TMS_T_FACTUREDETAIL."DateHeureCreation" AS DATEHEURECREATION_11,     TMS_T_FACTURE."Date (...+7337 caractères)";"2024-08-24 23:32:03";"";"Serveur (programmation)";"VDRREPORTFRONT";"ETL_3a685d15-3172-4faf-92e5-4b0918f6b315";"Tous les jours";"ETLPROGRAMMATIONCYZ21D";"ETL Jour 23h30";"2024-08-24 23:31:51"

-- delete the table if exist; 
drop table if exists 'logERR';  

-- https://www.postgresql.org/docs/14/datatype.html
create table logERR (
	id integer  -- id autoincrement with index 
	




)
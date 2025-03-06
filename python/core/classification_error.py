dorErrorDict = {
    # requete complexe à detecter en premier
    "SQLQueryTimeout_Error": ["Impossible d\'ouvrir la requête SQL sur la connexion"],  # en number 1
    "ColumnName_Error": ["Le nom de colonne", "n'existe pas dans la table ou la vue cible"],
    "SQLInvalidQuery_Error": ["impossible d'ouvrir la requête"],
    "DateFormat_Error": ["Not a legal OleAut date.", "La date"],
    # requetes simple
    "GuidezAtelier_Error" : ["Guidez Atelier" ,"Guidez Social"],
    "FieldSize_Error": ["La taille du champ"],
    "PreLogin_Error": ["an error occurred during the pre-login handshake."],
    "TimeFormat_Error": ["pas convertible en Heure"],
    "WebService_Error": ["connexion au web service impossible"],
    "ObjectReference_Error" : ["Object reference not set to an instance of an object."],
    "ValueREF_Error": ["La valeur #REF!"],
    "ValueVALUE_Error": ["La valeur #VALUE!"],
    "ValueNA_Error": ["La valeur #N/A!"],
    "ValueDivBy0_Error" : ["La valeur #DIV/0!"],
    "ValueNAME_Error": ["La valeur #NAME?"],
    "ConnectionTimeout_Error" : ["Connection Timeout Expired.  The timeout period elapsed during the post-login phase."],
    "UniqueIndex_Error" : ["L'instruction CREATE UNIQUE INDEX a été interrompue, car une clé dupliquée a été trouvée pour l'objet"],
    "CreateTABLE_Error" : ["Impossible de créer la table"],
    "PrimaryKey_Error": ["utilisé dans la clé primaire, sa valeur ne doit pas être vide"],
    "IndexErrorSimilarToUniqueIndex_Error" : ["Échec de l'opération car un index ou des statistiques portant le nom"],
    # cas non conforme
    # ancien code mis en commentaire par auteur d'origine
    # "SQL Delete Filter Error" -> "Le filtre de suppression n'est pas compatible SQL"
    # "SQL Other Error" -> "impossible d'ouvrir la requête sql"
    #
    "Other_Error" : [],
}

def categorize_message(message):
    message = message.lower()
    for key, values in dorErrorDict.items():
        for value in values:
            if value.lower() in message:
                return key
    return "Other_Error"

dorProgrammDict = {
    "ETL_Achats" : "ETL Achats",
    "ETL_API_JWT" : "ETL_API_JWT",
    "ETL_BEXT" : "ETL BEXT",
    "ETL_Chargement PJ" : "ETL Chargement PJ",
    "ETL_GLPI" : "ETL GLPI",
    "ETL_Heures_Chauffeurs" : "ETL Heures Chauffeurs",
    "ETL_JIRA" : "ETL JIRA",
    "ETL_KPI_ALDI" : "ETL KPI ALDI",
    "ETL_SUR_ORDRE" : "ETL sur ordre",
    "ETL_TAXATION" : "ETL Taxation",
    "ETL_VUE_HEURE_AGG" : "ETL Vue Heures Agrégées",
    "DAILY" : "Tous les jours",
    "WEEKLY_SUNDAY" : "Toutes les semaines, le dimanche",
    "INCONNU":"",
}

def categorize_programm(message):
    for key, value in dorProgrammDict.items():
        message = message.lower()
        if value.lower() in message:
            return key
    return "INCONNU"
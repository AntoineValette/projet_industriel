

def categorize_message(message):
    message = message.lower()
    if "Guidez Atelier".lower() in message or "Guidez Social".lower()  in message:
        return "Guidez Atelier Error"
    elif "La taille du champ".lower()  in message:
        return "Field Size Error" 
    elif "Un incident est survenu Object reference not set to an instance of an object.".lower()  in message:
        return "Object Reference Error"
    elif "La valeur #REF!".lower()  in message:
        return "Value #REF! Error"
    elif "La valeur #VALUE!".lower()  in message:
        return "Value #VALUE! Error"
    elif "La valeur #N/A!".lower()  in message:
        return "Value #N/A! Error"
    elif "La valeur #DIV/0!".lower()  in message:
        return "Value #DIV/0! Error"
    elif "La valeur #NAME?".lower()  in message:
        return "Value #NAME? Error"
    elif "Connection Timeout Expired.  The timeout period elapsed during the post-login phase.".lower()  in message:
        return "Connection Timeout Error"
    elif "an error occurred during the pre-login handshake.".lower()  in message:
        return "Pre-Login Error"
    elif "Un incident est survenu L'instruction CREATE UNIQUE INDEX a été interrompue, car une clé dupliquée a été trouvée pour l'objet".lower()  in message:
        return "Unique Index Error"
    elif "Impossible de créer la table".lower()  in message:
        return "Create TABLE Error"
    elif "Un incident est survenu Échec de l'opération car un index ou des statistiques portant le nom".lower()  in message:
        return "Index Error (similar to unique index error)"
    elif "utilisé dans la clé primaire, sa valeur ne doit pas être vide".lower()  in message:
        return "Primary Key Error"
    elif "pas convertible en Heure".lower()  in message:
        return "Time Format Error"
    elif "Not a legal OleAut date.".lower()  in message or ("La date".lower()  in message and "est pas valide".lower()  in message):
        return "Date Format Error"
    elif "connexion au web service impossible".lower()  in message:
        return "Web Service Error"
    elif "impossible d'ouvrir la requête".lower()  in message and "Un incident est survenu".lower()  in message and "non valide".lower()  in message:
        return "SQL Invalid Query Error"
    elif "Impossible d\'ouvrir la requête SQL sur la connexion".lower()  in message and "Le délai d\'attente a été dépassé".lower()  in message:
        return "SQL Query Timeout Error"
    elif "Le nom de colonne".lower()  in message and "n'existe pas dans la table ou la vue cible".lower()  in message:
        return "Column Name Error"
    else:
        return "Other Error"
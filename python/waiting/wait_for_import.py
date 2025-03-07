import os
import time

def wait_for_import():
    signal_file_1 = "/shared/historique_import_complete_LogETL.txt"
    signal_file_2 = "/shared/historique_import_complete_LogETLError.txt"

    while not (os.path.exists(signal_file_1) and os.path.exists(signal_file_2)):
        print("En attente de la fin de l'importation de l'historique pour les deux fichiers...")
        time.sleep(10)

    print("Importation de l'historique terminée pour les deux fichiers. Lancement de create_dataset...")
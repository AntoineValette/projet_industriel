import asyncio
from kafka import KafkaProducer
import json
import csv
import sys
from datetime import datetime
from classification_error import categorize_message


def log(msg):
    print(f"[{datetime.now()}] {msg}", flush=True)
    sys.stdout.flush()


# Configuration de KafkaProducer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


async def stream_file(filepath, topic):
    """Lit un fichier en continu et l'envoie à Kafka en mode tail -f"""
    last_line_number = 0  # Compteur pour suivre la dernière ligne lue

    # Lecture initiale du fichier
    f = await asyncio.to_thread(open, filepath, 'r', encoding='utf-8-sig')
    reader = list(csv.DictReader(f, delimiter=';'))  # Lire tout le fichier dans une liste
    f.close()  # Fermer après lecture initiale

    log(f"Lecture complète de {filepath} depuis le début...")

    # Envoyer toutes les lignes existantes au démarrage
    for i, row in enumerate(reader):
        if topic == "logERR_topic":
            print('yes')
            row['type_error'] = categorize_message(row['Message'])
            print(row['type_error'])
            producer.send(topic, row)
        else:
            producer.send(topic, row)
        log(f"[{filepath}] Ligne envoyée : {row}")
        last_line_number = i + 1  # Mémoriser la dernière ligne lue

    log(f"Fin de la lecture initiale de {filepath}. Passage en mode suivi (tail -f)...")

    # Passer en mode suivi des nouvelles lignes
    while True:
        f = await asyncio.to_thread(open, filepath, 'r', encoding='utf-8-sig')
        reader = list(csv.DictReader(f, delimiter=';'))  # Lire tout le fichier
        f.close()  # Fermer après lecture

        # Vérifier si de nouvelles lignes ont été ajoutées
        if len(reader) > last_line_number:
            new_rows = reader[last_line_number:]  # Récupérer les nouvelles lignes

            for row in new_rows:
                if topic == "logERR_topic":
                    print('yes')
                    row['type_error'] = categorize_message(row['Message'])
                    print(row['type_error'])
                    producer.send(topic, row)
                else:
                    producer.send(topic, row)
                log(f"[{filepath}] Nouvelle ligne envoyée : {row}")

            last_line_number = len(reader)  # Mettre à jour le dernier numéro de ligne

        await asyncio.sleep(1)  # Pause async pour éviter de bloquer la boucle


async def main():
    # Liste des fichiers à surveiller et leurs topics Kafka associés
    files_to_watch = [
        ("/data/logETL/241016_LogETL.csv", "logOK_topic"),
        ("/data/logETL/241016_LogETLError.csv", "logERR_topic")
    ]

    # Lancer chaque tâche de surveillance en parallèle
    tasks = [stream_file(filepath, topic) for filepath, topic in files_to_watch]
    await asyncio.gather(*tasks)  # Exécuter toutes les tâches en parallèle


# Démarrer le programme
asyncio.run(main())
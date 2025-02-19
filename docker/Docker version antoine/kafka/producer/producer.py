import time
from kafka import KafkaProducer
import json
import csv
import threading

def log(message):
    """Affiche un message horodaté"""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# Configuration de KafkaProducer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def stream_file(filepath, topic):
    """Lit un fichier en continu avec csv.DictReader et l'envoie à Kafka"""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        # Lire tout le fichier au démarrage
        log(f"Lecture complète de {filepath} depuis le début...")
        for row in reader:
            producer.send(topic, row)
            log(f"[{filepath}] Ligne envoyée : {row}")

        # Suivre les nouvelles lignes (mode tail -f)
        log(f"Fin de la lecture initiale de {filepath}. Passage en mode suivi (tail -f)...")
        while True:
            line = f.readline()
            if line:
                try:
                    # Parser la nouvelle ligne avec un nouveau DictReader
                    new_line_reader = csv.DictReader([line], delimiter=';')
                    for row in new_line_reader:
                        producer.send(topic, row)
                        log(f"[{filepath}] Nouvelle ligne envoyée : {row}")
                except Exception as e:
                    log(f"Erreur de parsing de la ligne : {line} - {e}")
            else:
                time.sleep(1)

# Liste des fichiers à suivre et des topics associés
files_to_watch = [
    ("/data/logETL/241016_LogETL.csv", "logOK_topic"),
    ("/data/logETL/241016_LogETLError.csv", "logERR_topic")
]

# Lancer un thread par fichier
threads = []
for filepath, topic in files_to_watch:
    t = threading.Thread(target=stream_file, args=(filepath, topic))
    t.start()
    threads.append(t)

# Attendre que tous les threads se terminent (ce qui n'arrivera jamais si les fichiers sont toujours alimentés)
for t in threads:
    t.join()

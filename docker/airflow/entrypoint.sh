#!/usr/bin/env bash
set -e

# Attente de PostgreSQL
echo "Attente de la disponibilité de PostgreSQL sur ${POSTGRES_HOST}:${POSTGRES_PORT}..."
while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
  sleep 1
done
echo "PostgreSQL est disponible !"

# Initialisation de la base de métadonnées Airflow
echo "Initialisation de la base de métadonnées Airflow..."
airflow db init

# Création de l'utilisateur admin
echo "Création de l'utilisateur admin..."
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin || true

# Définition dynamique de START_DATE au lancement
export START_DATE=$(date '+%Y-%m-%dT%H:00:00')
echo "START_DATE définie à : $START_DATE"

# Démarrage du scheduler Airflow en tâche de fond
echo "Démarrage du scheduler Airflow en tâche de fond..."
airflow scheduler &

# Démarrage du webserver Airflow
echo "Démarrage du webserver Airflow..."
exec airflow webserver

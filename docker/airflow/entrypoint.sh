#!/usr/bin/env bash
set -e

echo "Attente de la disponibilité de PostgreSQL sur ${POSTGRES_HOST}:${POSTGRES_PORT}..."
while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
  sleep 1
done
echo "PostgreSQL est disponible !"

echo "Initialisation de la base de métadonnées Airflow..."
airflow db init

# Cette ligne est à supprimer ou commenter car elle n'est plus supportée :
# echo "Création des connexions par défaut..."
# airflow connections create-default-connections

echo "Création de l'utilisateur admin..."
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin || true

echo "Démarrage du scheduler Airflow en tâche de fond..."
airflow scheduler &

echo "Démarrage du webserver Airflow..."
exec airflow webserver
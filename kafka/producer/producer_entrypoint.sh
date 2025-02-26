#!/bin/bash
echo "Attente de PostgreSQL avant de lancer le producer Kafka..."
python /app/wait_for_postgres.py

echo "Attente de Kafka..."
python /app/wait_for_kafka.py

echo "Lancement du producer Kafka..."
python /app/kafka/producer/producer.py

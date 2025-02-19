#!/bin/bash
echo "Attente de PostgreSQL avant de lancer le consumer Kafka..."
python /app/wait_for_postgres.py

echo "Attente de Kafka..."
python /app/wait_for_kafka.py

echo "Lancement du consumer Kafka..."
python /app/kafka/consumer/consumer.py

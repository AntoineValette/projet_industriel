FROM python:3.11-slim

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
RUN pip install psycopg2 kafka-python

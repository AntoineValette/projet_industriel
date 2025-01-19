FROM python:3.11-slim

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
RUN pip install psycopg2 requests

WORKDIR /script

# Copie le script Python
COPY import_csv.py .
COPY wait_for_postgres.py .
COPY entrypoint.sh .

# Définit le point d'entrée
ENTRYPOINT ["./entrypoint.sh"]


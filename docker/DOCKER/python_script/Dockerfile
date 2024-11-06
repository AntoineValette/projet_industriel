FROM python:3.11-slim

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
RUN pip install psycopg2 requests

WORKDIR /script

# Copie le script Python
COPY import_csv1.py .
COPY import_csv2.py .
COPY wait_for_postgres.py .

# Définit le point d'entrée
ENTRYPOINT ["sh", "-c", "python wait_for_postgres.py && python import_csv1.py && python import_csv2.py"]


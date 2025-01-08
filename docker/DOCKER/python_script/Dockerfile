FROM python:3.12

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
# RUN pip install psycopg2 requests
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /script

# Copie le script Python
COPY import_csv1.py .
COPY import_csv2.py .

# Définit le point d'entrée
ENTRYPOINT ["sh", "-c", "python import_csv1.py && python import_csv2.py"]


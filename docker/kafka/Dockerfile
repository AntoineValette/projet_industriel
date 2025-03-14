FROM python:3.9

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

# COPY ./docker/kafka/requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
RUN pip install psycopg2 kafka-python

COPY ../../python /app

WORKDIR /app




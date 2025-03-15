FROM python:3.9 AS builder

# sources
# https://fastapi.tiangolo.com/deployment/docker/#docker-cache
# https://docs.docker.com/go/dockerfile-user-best-practices/
# https://darekdari.com/how-to-optimize-dockerfile-for-python/

# on declare le repertoire courant
WORKDIR /app

# variables d'environnements
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && \
    apt upgrade -y && \
    apt install -y libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Installe psycopg2 et requests pour interagir avec PostgreSQL et GitLab
RUN pip install psycopg2 kafka-python

# on construit une image docker plus legere à partir du build
FROM python:3.9-slim  AS runner
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# on est quand meme obligé de faire un update à cause de psycopg2
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# variables d'environnements
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ../../python .


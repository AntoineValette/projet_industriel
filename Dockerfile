FROM python:3.12

# sources
# https://fastapi.tiangolo.com/deployment/docker/#docker-cache
# https://docs.docker.com/go/dockerfile-user-best-practices/

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH="${PYTHONPATH}:/code:/code/python/import:/code/python/core:/code/python/ETL"

# Installer les dépendances système nécessaires pour psycopg2
RUN apt update && apt install -y libpq-dev gcc

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code

# Copie le script Python
COPY ./python/ ./python/
COPY ./scripts/entrypoint.sh ./scripts/

# Définit le point d'entrée
ENTRYPOINT ["/code/scripts/entrypoint.sh", "-f","./python/import/import_csv.py"]

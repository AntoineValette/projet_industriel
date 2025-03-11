FROM apache/airflow:2.5.1

# Passer en mode root pour installer netcat-openbsd
USER root
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Changer l'utilisateur pour installer le package via pip
USER airflow

# COPY ./docker/airflow/requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install --upgrade psycopg2-binary pytz

# Revenir en root pour copier et rendre le script exécutable
USER root
COPY ./docker/airflow/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Retourner à l'utilisateur airflow pour l'exécution
USER airflow
ENTRYPOINT ["/entrypoint.sh"]

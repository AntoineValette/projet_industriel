#!/bin/bash 

# download images of postgresql in 14.13 version
docker pull postgres:14.13
docker pull postgres:16.4

# create a volume to make persistant data when we stop or destroy container 
docker volume create pgsql14
docker volume create pgsql16

# this command run the container like a deamon in the background 
docker run --name postgresDB-14 \
            -e POSTGRES_PASSWORD=Azerty01 \
            -e POSTGRES_DB=postgres \
            -e POSTGRES_USER=postgres \
            -p 5432:5432 \
            -v pgsql14:/var/lib/postgresql/data \
            -d postgres:14.13

# this command run the container like a deamon in the background
docker run --name postgresDB-16 \
            -e POSTGRES_PASSWORD=Azerty01 \
            -e POSTGRES_DB=postgres \
            -e POSTGRES_USER=postgres \
            -p 5433:5432 \
            -v pgsql16:/var/lib/postgresql/data \
            -d postgres:16.4


# 



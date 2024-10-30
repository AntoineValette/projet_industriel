#!/bin/bash 

# download images of postgresql in 14.13 version
docker pull postgresql:14.13

# create a volume to make persistant data when we stop or destroy container 
docker volume create pgsl14

# this command run the container like a deamon in the background 
docker run --name postgresDB \
            -e POSTGRES_PASSWORD=Azerty01 \
            -e POSTGRES_DB=postgres \
            -e POSTGRES_USER=postgres \
            -p 5432:5432 \
            -v pgsql:/var/lib/postgresql/data \
            -d postgres

# 



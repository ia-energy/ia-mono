# Postgres
We'll be using an official docker [postgress image](https://hub.docker.com/_/postgres). It's going to be a little hacky until I can look back on this later

1. Pull the docker image using a tagged version

         docker pull postgres:11.5

2. Run the docker images

        docker run --name ia-postgres -e POSTGRES_PASSWORD=5SY8aFtPm4_change_for_prod -d postgres

3. Bash into the image 

        docker exec -it ia-postgres /bin/bash 

4. Become the postgres user

        su - postgres

5. Setup the iadb

        psql -c 'create database iadb;';
        psql -c "create user ia with encrypted password 'r9kLwMrdph_change_for_prod';";
        psql -c'grant all privileges on database iadb to ia;';

6. Exit

        exit
    	exit




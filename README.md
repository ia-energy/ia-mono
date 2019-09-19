# IA Mono
One monolithic repo to rule them all. This repo will be used to house anything directly interacting with the main IA website.

## Product Overview 
![Sequence diagram](https://github.com/ia-energy/ia-mono/blob/master/docs/overview/Analytics_Service_sequence_diagram.png "Sequence diagram")

## Repo Structure
Besides the docs directory each high level directory should represent a deployable product. There should be a README describing the product and how to develop or deploy the product. 

## Developer and Productions tools
* [Linux bash](https://devhints.io/bash) Default Linux OS command line and scripting language
* [Docker](https://www.docker.com/) The default Dockerfile should be for development. A Dockerfile_prod is also advisable.
* [Python](https://python.org) Scripting language that is data science friendly
* [Node/NPM](https://www.npmjs.com/get-npm) Scripting language mostly for managing javascript and css builds
* [Vuejs.org](https://nodejs.org) JavaScript Framework 
* [Bootstrap](https://getbootstrap.com/) CSS Framework 
* [Postgres](https://www.postgresql.org/) SQL and non-sql database

## Docker compose
Idealy the easy way of getting a development instance up and going:
`docker-compose up`

Containers by port number
* 8080 VueJs
* 5000 Flask
* 5432 Postgres
* 8081 Airflow

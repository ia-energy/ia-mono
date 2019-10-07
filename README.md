# IA Mono
One monolithic repo to rule them all. This repo will be used to house anything
directly interacting with the core IA product.

## Product Overview
![Sequence diagram][1]

## Repo Structure
Besides the docs directory each high level directory should represent a
deployable product. There should be a README describing the product and how to
develop or deploy the product.

## Developer and Productions tools
* [Apache Airflow](https://airflow.apache.org/) Monitor and schedule workflows
  with python scripts
* [Auth0](https://auth0.com/) Authentication software as a service
* [Bash (Linux shell)](https://devhints.io/bash) Default Linux OS command line and
  scripting language
* [Bootstrap](https://getbootstrap.com/) CSS Framework
* [BootstrapVue](https://bootstrap-vue.js.org/)
* [Docker](https://www.docker.com/) The default Dockerfile should be for
  development. A Dockerfile_prod is also advisable.
* [D3](https://d3js.org/) JavaScript library to create Data driven
  documents(graphs) in HTML
* [Flask](https://flask.palletsprojects.com) Lightweight web application
  framework.
* [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)  Extension
  for Flask that adds support for quickly building REST APIs
* [Node/NPM](https://www.npmjs.com/get-npm) Scripting language mostly for
  managing JavaScript and CSS builds
* [Postgres](https://www.postgresql.org/) SQL and non-SQL database
* [Python](https://python.org) Scripting language that is data science friendly
* [SQLAlchemy](https://www.sqlalchemy.org/) Python SQL Toolkit and Object
    Relational Mapper
* [Vuejs.org](https://nodejs.org) JavaScript Framework

## Docker compose
The easy way of getting a development instance up and going:
* `docker-compose up`
* see [/flask/README.md](/flask#database-change-management) for datebase setup

Containers by port number
* 8080 VueJs
* 5000 Flask
* 5432 Postgres
* 8081 Airflow

[1]: https://github.com/ia-energy/ia-mono/blob/master/docs/overview/Analytics_Service_sequence_diagram.png

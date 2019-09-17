# Vue-3
Client side Javascript framework general learning:

* JavaScript Framework [vuejs.org](https://vuejs.org)
* CSS Framework [Bootstrap](https://getbootstrap.com/)
* Container for dev and deploy [Docker](https://www.docker.com)
* Authenication [Auth0](https://auth0.com)

## Dependencies
* (Docker install) https://docs.docker.com/install/

and/or 

* (Node/NPM) https://nodejs.org/en/download/
note: there is a HOST env issue with OSX please run `unset HOST` if server doesn't start

## Configuration
* auth_config.json - Auth0 [configuration](https://auth0.com/docs/quickstart/spa/vuejs/01-login)

## Starting
* Docker
	* **Development** docker ([source](https://mherman.org/blog/dockerizing-a-vue-app/))
		* build `docker build -t vue-ia-app:dev .`
		* start server `docker run --name ia-vue -v ${PWD}:/app -v /app/node_modules -p 8080:8080 --rm vue-ia-app:dev` note: {PWD} may not work on Windows. See [this](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10) Stack Overflow question for more info.  
	* **Production** docker ([source](https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html)) 
		* build `docker build -f Dockerfile_prod -t vuejs-ia-prod-app/dockerize-vuejs-app .`
		* start server `docker run -it -p 8081:8080 --rm --name vuejs-ia-prod-app-1 vuejs-ia-prod-app/dockerize-vuejs-app` 

or

* Quick dev start: `npm run serve`

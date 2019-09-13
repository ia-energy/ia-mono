# Vue-3
Client side Javascript framework general learning:

* JavaScript Framework [vuejs.org](https://vuejs.org)
* CSS Framework [Bootstrap](https://getbootstrap.com/)
* Container for dev and deploy [Docker](https://www.docker.com)

## Dependencies
* (Docker install) https://docs.docker.com/install/

and/or 

* (Node/NPM) https://nodejs.org/en/download/
note: there is a HOST env issue with OSX please run `unset HOST` if server doesn't start


## Starting
* Docker
	* **Development** docker ([source](https://mherman.org/blog/dockerizing-a-vue-app/))
		* build `docker build -t vue-ia-app:dev .`
		* start server `docker run -v ${PWD}:/app -v /app/node_modules -p 8081:8080 --rm vue-ai-app:dev` note: {PWD} may not work on Windows. See [this](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10) Stack Overflow question for more info.  
	* **Production** docker ([source](https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html)) 
		* build `docker build -f Dockerfile_prod -t vuejs-ia-prod-app/dockerize-vuejs-app .`
		* start server `docker run -it -p 8081:8080 --rm --name vuejs-ia-prod-app-1 vuejs-ia-prod-app/dockerize-vuejs-app` 

or

* Quick dev start: `npm run serve`
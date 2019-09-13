# Flask

## Dev docker
* `docker build -t ia-flask:latest .`
* `docker run --name ia-flask -v ${PWD}:/app -d -p 5000:5000 ia-flask` note: {PWD} may not work on Windows. See [this](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10) Stack Overflow question for more info.

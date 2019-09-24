# Flask

## Dev docker
* `docker build -t ia-flask:latest .`
* `docker run --name ia-flask --restart unless-stopped -v ${PWD}:/working_dir -d -p 5000:5000 ia-flask` note: {PWD} may not work on Windows. See [this](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10) Stack Overflow question for more info.

## Running test 
* `python manage.py test`

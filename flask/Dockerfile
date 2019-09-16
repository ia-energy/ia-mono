# base image
# choosen from https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.7-slim-buster

# set working directory
WORKDIR /app


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

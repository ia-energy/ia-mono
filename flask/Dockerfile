# base image
# choosen from https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.7-slim-buster

# set working directory
WORKDIR /working_dir


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /working_dir/requirements.txt

RUN pip install -r requirements.txt

COPY . /working_dir

ENTRYPOINT [ "python" ]

CMD [ "manage.py" ]

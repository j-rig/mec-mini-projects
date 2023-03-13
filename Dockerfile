FROM python:3.7-slim-buster
RUN apt-get -y update
RUN apt-get -y install build-essential
RUN pip install --upgrade pip
RUN pip install wheel
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install python-dotenv

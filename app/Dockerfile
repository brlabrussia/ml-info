FROM python:3.8-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /usr/src/app/
RUN mkdir /usr/src/app/{static,media}
WORKDIR /usr/src/app/

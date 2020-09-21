FROM python:3.8-buster

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# used in entrypoint to wait for db
RUN apt update
RUN apt install -y netcat

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

COPY entrypoint.sh /usr/src/app/

COPY . /usr/src/app/
# RUN mkdir -p /usr/src/app/{static,media,fixtures}

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

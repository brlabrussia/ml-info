#!/bin/bash

while ! nc -z postgres 5432; do sleep 1; done
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"

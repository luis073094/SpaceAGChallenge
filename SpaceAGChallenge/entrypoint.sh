#!/bin/sh
cd SpaceAGChallenge

python manage.py migrate FieldWorker --no-input

python manage.py collectstatic --no-input

gunicorn SpaceAGChallenge.wsgi:application --bind 0.0.0.0:8000
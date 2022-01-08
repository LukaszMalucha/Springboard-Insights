#!/bin/sh

set -e
python manage.py wait_for_db
#python manage.py migrate
gunicorn springboard_analytics.asgi:application --workers 4 -k uvicorn.workers.UvicornWorker --bind :8000
#python manage.py runserver 0.0.0.0:8000


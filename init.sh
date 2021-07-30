#!/usr/bin/env bash

set -ex

#django run migrations
python manage.py makemigrations
python manage.py migrate

#Collect static files
#echo "yes" | python manage.py collectstatic

# Run server
python manage.py runserver 0.0.0.0:8000
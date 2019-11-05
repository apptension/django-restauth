#!/usr/bin/env bash

echo 'Hello'
./wait-for-it.sh db:5432
python manage.py migrate
python manage.py runserver 0:8080

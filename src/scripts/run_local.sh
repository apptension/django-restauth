#!/usr/bin/env sh

set -x

python manage.py migrate
python manage.py runserver 0.0.0.0:8000 --settings=settings.configs --configuration=Local
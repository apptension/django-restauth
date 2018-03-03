#!/usr/bin/env sh

set -x

python manage.py check --deploy
python manage.py migrate
uwsgi --ini $APP_DIR/uwsgi.ini
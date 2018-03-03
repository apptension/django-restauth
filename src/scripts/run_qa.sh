#!/usr/bin/env sh

set -x

python manage.py check --deploy
python manage.py migrate

# Custom scripts for example for creating fake users, data etc.

uwsgi --ini $APP_DIR/uwsgi.ini
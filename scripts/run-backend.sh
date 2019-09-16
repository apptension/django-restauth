#!/usr/bin/env bash

set -e

python manage.py migrate --no-input
uwsgi --ini uwsgi.ini

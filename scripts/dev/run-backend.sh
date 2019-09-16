#!/usr/bin/env bash

set -e

. $(dirname "$0")/install_localstack_fixtures.sh

# wait untill secretsmanager become ready
wait_for_secretsmanager
echo "Secrets manager is up"

# install all localstack fixtures
{
    install_db_secret &&
    echo "DB secrets set"
} || {
    echo "DB secrets NOT set"
}

python ./scripts/dev/wait_for_postgres.py &&
  ./manage.py migrate &&
  ./manage.py runserver 0.0.0.0:8000

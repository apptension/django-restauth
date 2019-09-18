#!/usr/bin/env bash

set -e

function wait_for_secretsmanager {
  until aws --no-sign-request --endpoint-url="$SECRET_MANAGER_ENDPOINT_URL" secretsmanager list-secrets; do
    >&2 echo "Secretsmanager is unavailable - sleeping"
    sleep 1
  done
}

function install_db_secret {
  SECRET_STRING="{\"host\": \"db\", \"username\": \"$POSTGRES_USER\", \"password\": \"$POSTGRES_PASSWORD\", \"port\": $POSTGRES_PORT}"

  aws --endpoint-url="$SECRET_MANAGER_ENDPOINT_URL" secretsmanager create-secret \
      --name "$DB_SECRET_ARN" \
      --secret-string "$SECRET_STRING"
}

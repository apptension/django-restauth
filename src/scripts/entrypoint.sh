#!/usr/bin/env bash
set -e
cmd="$@"

postgres_ready() {
    python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_DB",
                            user="$POSTGRES_USER",
                            password="$POSTGRES_PASSWORD",
                            host="$POSTGRES_HOST",
                            port="$POSTGRES_PORT")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    >&2 echo $POSTGRES_DB $POSTGRES_USER $POSTGRES_PASSWORD $POSTGRES_HOST $POSTGRES_PORT
    sleep 1
done

>&2 echo "PostgreSQL is up - continuing..."

export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_USER
exec $cmd
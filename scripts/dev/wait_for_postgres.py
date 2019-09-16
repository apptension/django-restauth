import os
import logging
from time import time, sleep
import psycopg2
import boto3
import json

secrets_manager = boto3.client(
    'secretsmanager', endpoint_url=os.environ.get('SECRET_MANAGER_ENDPOINT_URL', None))

db_secret_arn = os.environ['DB_SECRET_ARN']

db_secret_value = secrets_manager.get_secret_value(SecretId=db_secret_arn)
# contains host, username, password and port
db_connection_config = json.loads(db_secret_value.get('SecretString'))

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
config = {
    "dbname": os.getenv("POSTGRES_DB", "postgres"),
    "user": db_connection_config.get('username'),
    "password": db_connection_config.get('password'),
    "host": db_connection_config.get('host'),
}

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def pg_isready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**vars())
            logger.info("Postgres is ready! ✨ 💅")
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(f"Postgres isn't ready. Waiting for {check_interval} {interval_unit}...")
            sleep(check_interval)

    logger.error(f"We could not connect to Postgres within {check_timeout} seconds.")
    return False


pg_isready(**config)

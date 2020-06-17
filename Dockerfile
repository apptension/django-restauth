##
# Chamber installation stage
##

FROM segment/chamber:2 AS chamber

##
# App build stage
##

FROM python:3.8-slim-buster AS backend

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR off


RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client ca-certificates jq \
  && update-ca-certificates \
  && pip install --no-cache-dir setuptools pipenv==2018.11.26 gunicorn \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY --from=chamber /chamber /bin/chamber

WORKDIR /app
COPY Pipfile* /app/

RUN pipenv install --dev --system --deploy

COPY . /app/
RUN chmod +x /app/scripts/*.sh


ENV DB_CONNECTION='{}' \
    HASHID_FIELD_SALT='' \
    DJANGO_PARENT_HOST=''

RUN python manage.py collectstatic --no-input

CMD ["./scripts/run.sh"]

FROM python:3.6-alpine

ENV APP_DIR /app/backend

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps build-base gcc linux-headers make python3-dev musl-dev postgresql-dev

# Available choices: base, prod, qa, test, local
ARG ENV_NAME

COPY requirements $APP_DIR/requirements
RUN pip install --no-cache-dir -r requirements/${ENV_NAME}.txt && \
    apk --purge del .build-deps

COPY src $APP_DIR

ENTRYPOINT ["sh", "/app/backend/scripts/entrypoint.sh"]

EXPOSE 8000

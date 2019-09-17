FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add bash \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add build-base linux-headers pcre-dev \
    && apk add gettext

RUN pip install awscli

EXPOSE 3031
WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --dev
COPY . /app

CMD ["/app/scripts/run-backend.sh"]

# 🍔 django-restauth

[![Build Status](https://travis-ci.org/apptension/django-restauth.svg?branch=master)](https://travis-ci.org/apptension/django-restauth)


## Runing on DigitalOcean
```
Here we use a database on a pod to avoid paying for managed database.
Normally a managed database should be used to run on DigitalOcean.
```
#### Create pods and services
```
kubectl apply -f kubernetes
```
#### Create a database on a pod
```
kubectl exec db bash
su postgres
psql
create database dev;
```
#### Run migrations
```
kubectl exec [dev pod name] bash
./manage.py migrate
./manage.py runserver 0:8000
```
### Test deployment
```
curl http://[load balancer external IP]:8080
```

## Running

```
pip install pipenv
pipenv install
pipenv run python manage.py runserver
```

## Usage

* Modify your settings

```python
LANGUAGE_CODE = 'error_codes'

# ..

AUTH_USER_MODEL = 'restauth.User'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER': 'restauth.jwt.encode_handler',
}

HASHID_FIELD_SALT = ''
```

* Generate `HASHID_FIELD_SALT`

`from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`

* Modify `urls.py`

## Features

- [x] Register user with profile in single API call
- [x] Login endpoint to return JWT token
- [x] User account activation endpoint
- [x] User profile endpoint
- [x] HashID for User primary key
- [x] Password reset & change endpoints
- [x] Add Swagger for API documentation
- [x] Ability to set user notification implementation
- [ ] Add lean docker-compose w/ Postgres
- [ ] Add a way to communicate settings, urls, etc to a higher order project

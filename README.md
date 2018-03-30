# 🍔 django-restauth

[![Build Status](https://travis-ci.org/apptension/django-restauth.svg?branch=master)](https://travis-ci.org/apptension/django-restauth)

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
- [x] Remove user away from change password endpoint
- [x] Change user to email on auth confirm endpoint
- [x] Add endpoint to change profile
- [x] Review password reset confirm endpoint

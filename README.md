# REST User Boilerplate :sparkles:

* Modify your settings

```
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
- Register user with profile in single API call
- Login endpoint to return JWT token
- User account activation endpoint
- User profile endpoint
- HashID for User primary key
- Password reset & change endpoints
- Add Swagger for API documentation
- Ability to set user notification implementation

## TODO
- Add lean docker-compose w/ Postgres
- Add a way to communicate settings, urls, etc to a higher order project

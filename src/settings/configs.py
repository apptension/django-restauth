from . import base
from . import security

from configurations import values


class Prod(security.Security, base.Base):
    pass


class QA(security.Security, base.Base):
    pass


class Local(base.Base):
    SECRET_KEY = values.Value('secretkey')
    HASHID_FIELD_SALT = values.Value('hashidfieldsalt')


class Test(base.Base):
    DEBUG = False
    TEMPLATE_DEBUG = False
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',  # Use fast password hasher so tests run faster
    ]
    CACHES = {
        "default": {
            "BACKEND": 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
    SECRET_KEY = values.Value('SECRET_KEY')
    HASHID_FIELD_SALT = values.Value('HASHID_FIELD_SALT')


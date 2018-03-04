from configurations import values


class Security:
    SECURE_HSTS_SECONDS = values.IntegerValue(60)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_PRELOAD = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    CSRF_COOKIE_SECURE = values.BooleanValue(True)
    CSRF_COOKIE_HTTPONLY = values.BooleanValue(True)
    X_FRAME_OPTIONS = values.Value('DENY')

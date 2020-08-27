"""
"""
from .base import *

try:
    from .oscar_settings import *
except ImportError:
    pass


DEBUG = True
AUTH_PASSWORD_VALIDATORS = [
]

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!",
)


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int(  # noqa: F405
    "CONN_MAX_AGE", default=60
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = str(BASE_DIR / 'static')
MEDIA_ROOT = str(BASE_DIR / 'media')
STATICFILES_DIRS = (
    str(BASE_DIR / 'gs_static'),
)

EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND",
                    default='django.core.mail.backends.smtp.EmailBackend')





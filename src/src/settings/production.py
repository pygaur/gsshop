"""
"""
from .base import *

try:
    from .oscar_settings import *
except ImportError:
    pass


def get_list(text):
    return [item.strip() for item in text.split(",")]


DEBUG = False
ALLOWED_HOSTS = get_list(os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1"))
ADMIN_URL = env("DJANGO_ADMIN_URL")

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"] = env.db("DATABASE_URL")  # noqa: F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa: F405
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


EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND")


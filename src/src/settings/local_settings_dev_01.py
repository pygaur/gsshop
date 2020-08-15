"""
"""
from .base import *

try:
    from .oscar_settings import *
except ImportError:
    pass


AUTH_PASSWORD_VALIDATORS = [
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}


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

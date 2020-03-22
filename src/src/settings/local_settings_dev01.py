from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@ah5t@mfy$@j9wn%fnl9=3+m!fca2_5r)3mzurf=1vlu+*)206'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Use a Sqlite database by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'USER': None,
        'PASSWORD': None,
        'HOST':  None,
        'PORT': None,
        'ATOMIC_REQUESTS': True
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
"""
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}
"""


AUTH_PASSWORD_VALIDATORS = []   # ONLY FOR DEVELOPMENT

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(CWR, 'static')
MEDIA_ROOT = 'media'

STATICFILES_DIRS = (
    os.path.join(CWR, 'gs_static'),
)


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('en', 'English'),
    ('hi', 'Hindi'),
)

try:
    from .oscar_settings import *
except ImportError:
    pass

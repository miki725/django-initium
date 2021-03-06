"""
Checklist for production-ready settings:
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

This is a base for production settings without including
any sensitive information. Include all sensitive information
in ``prod.py`` settings file which should not be committed
to version-control.
"""
from __future__ import unicode_literals, print_function
from .base import *


DEBUG = False

ADMINS = (
    # e.g. ('name', 'email@example.com'),
)

ALLOWED_HOSTS = [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

EMAIL_SUBJECT_PREFIX = '[Django {{ project_name }}] '
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GEVENT_ADDR_PORT = ''
GEVENT_POOL_SIZE = 100

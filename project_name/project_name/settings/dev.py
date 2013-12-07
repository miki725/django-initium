from __future__ import unicode_literals, print_function
from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{ project_name }}.sqlite',
    }
}

ALLOWED_HOSTS = [
    '*',
]

SECRET_KEY = '{{ secret_key }}'

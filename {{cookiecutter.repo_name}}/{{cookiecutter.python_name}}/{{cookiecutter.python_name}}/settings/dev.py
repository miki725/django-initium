# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from .base import Base


class Dev(Base):
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '{{ cookiecutter.python_name }}.sqlite',
        }
    }

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'django_extensions',
    ]

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    SECRET_KEY = '<dev-secret-key>'

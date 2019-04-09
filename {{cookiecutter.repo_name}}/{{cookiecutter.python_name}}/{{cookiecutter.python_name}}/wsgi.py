"""
WSGI config for fdr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os

from configurations.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.python_name}}.settings.dev")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')


application = get_wsgi_application()

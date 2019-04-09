"""
Django settings for {{ cookiecutter.project_name }} project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os

from configurations import Configuration

from ..utils import abspath
from .mixins.pipeline import PipelineConfigurationMixin


class Base(PipelineConfigurationMixin,
           Configuration):
    # where manage.py is located
    PROJECT_PATH = abspath(__file__, '..', '..', '..')
    # project name - name of PROJECT_PATH inside project root
    PROJECT_NAME = os.path.basename(abspath(__file__, '..', '..'))

    INSTALLED_APPS = [
        # project apps
        'user',

        'braces',
        'crispy_forms',
        'django_auxilium',
        'pipeline',
        'vanilla',

        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
    ]

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django_auxilium.middleware.html.MinifyHTMLMiddleware',
    ]

    ALLOWED_HOSTS = ['*']

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/New_York'
    USE_I18N = False
    USE_L10N = False
    USE_TZ = True

    # Media files
    MEDIA_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, 'media')
    MEDIA_URL = '/media/'

    # Static files
    STATIC_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, 'all_static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(PROJECT_PATH, PROJECT_NAME, 'static'),
    ]
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'pipeline.finders.PipelineFinder',
    ]
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

    TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, PROJECT_NAME, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                '{{ cookiecutter.python_name }}.context_processors.now',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    }]

    AUTH_USER_MODEL = 'user.User'

    # URLs
    ROOT_URLCONF = '{{ cookiecutter.python_name }}.urls'
    LOGIN_URL = '/login/'
    LOGOUT_URL = '/logout/'
    LOGIN_REDIRECT_URL = '/'
    WSGI_APPLICATION = '{{ cookiecutter.python_name }}.wsgi.application'

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    EMAIL_SUBJECT_PREFIX = '[{{ cookiecutter.project_name }}] '

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s '
                          '%(levelname)s '
                          '%(name)s '
                          '%(message)s',
            },
            'simple': {
                'format': '%(levelname)s '
                          '%(name)s '
                          '%(message)s',
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'null': {
                'level': 'INFO',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
            '{{ cookiecutter.python_name }}': {
                'level': 'INFO',
                'handlers': ['console'],
            },
        }
    }

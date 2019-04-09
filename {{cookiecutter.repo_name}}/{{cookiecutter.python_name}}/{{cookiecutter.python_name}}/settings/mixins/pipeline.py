# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os


class PipelineConfigurationMixin(object):
    PIPELINE_COMPILERS = (
        'pipeline.compilers.less.LessCompiler',
    )

    PIPELINE_CSS = {
        'bootstrap': {
            'source_filenames': [
                'lib/node_modules/bootstrap/less/bootstrap.less',
            ],
            'output_filename': 'lib/bootstrap.css',
            'extra_context': {
                'media': 'screen',
            },
        },
        'login': {
            'source_filenames': [
                'account/less/login.less',
            ],
            'output_filename': 'account/login.css',
            'extra_context': {
                'media': 'screen',
            },
        },
        'errors': {
            'source_filenames': [
                'errors/less/errors.less',
            ],
            'output_filename': 'errors/errors.css',
            'extra_context': {
                'media': 'screen',
            },
        },
    }

    PIPELINE_JS = {
        'bootstrap': {
            'source_filenames': [
                'lib/node_modules/jquery/dist/jquery.min.js',
                'lib/django/django-csrf.js',
                'lib/node_modules/bootstrap/js/affix.js',
                'lib/node_modules/bootstrap/js/alert.js',
                'lib/node_modules/bootstrap/js/button.js',
                'lib/node_modules/bootstrap/js/carousel.js',
                'lib/node_modules/bootstrap/js/collapse.js',
                'lib/node_modules/bootstrap/js/dropdown.js',
                'lib/node_modules/bootstrap/js/modal.js',
                'lib/node_modules/bootstrap/js/tooltip.js',
                'lib/node_modules/bootstrap/js/popover.js',
                'lib/node_modules/bootstrap/js/scrollspy.js',
                'lib/node_modules/bootstrap/js/tab.js',
                'lib/node_modules/bootstrap/js/transition.js',
            ],
            'output_filename': 'lib/bootstrap.js',
        },
        'ie': {
            'source_filenames': [
                'lib/node_modules/html5shiv/dist/html5shiv.min.js',
                'lib/node_modules/respond.js/dest/respond.min.js',
            ],
            'output_filename': 'lib/ie.js',
        },
    }

    @property
    def PIPELINE_LESS_ARGUMENTS(self):
        return '--include-path="{}"'.format(
            ':'.join([os.path.dirname(i) for i in self.STATICFILES_DIRS])
        )

    @property
    def PIPELINE(self):
        return {
            'COMPILERS': self.PIPELINE_COMPILERS,
            'STYLESHEETS': self.PIPELINE_CSS,
            'JAVASCRIPT': self.PIPELINE_JS,
            'LESS_ARGUMENTS': self.PIPELINE_LESS_ARGUMENTS,
        }

# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.utils.timezone import now as django_now


def now(request):
    return {'now': django_now()}

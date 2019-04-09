# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from user.admin import UserAdmin
from user.models import User


class AdminSite(AdminSite):
    site_title = '{{ cookiecutter.project_name }} Admin'
    site_header = '{{ cookiecutter.project_name }} Admin'
    index_title = '{{ cookiecutter.project_name }} Admin'


site = AdminSite()

site.register(User, UserAdmin)
site.register(Group, GroupAdmin)

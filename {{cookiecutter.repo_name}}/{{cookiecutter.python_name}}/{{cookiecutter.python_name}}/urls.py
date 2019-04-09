# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.views.static import serve
from vanilla import TemplateView

from .admin import site


urlpatterns = [
    # url(r'^', include('project_app', namespace='app')),

    # login/logout
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html',
                               'next_page': '/'}, name='logout'),

    # admin
    url(r'^admin/', include(site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'400/$', TemplateView.as_view(template_name='400.html')),
        url(r'403/$', TemplateView.as_view(template_name='403.html')),
        url(r'404/$', TemplateView.as_view(template_name='404.html')),
        url(r'500/$', TemplateView.as_view(template_name='500.html')),
        url(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]),
            serve, {'document_root': settings.MEDIA_ROOT}),
    ]

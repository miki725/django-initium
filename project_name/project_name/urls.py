from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',

    # login/logout
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html',
                               'next_page': '/'}, name='logout'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

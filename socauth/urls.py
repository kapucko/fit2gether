from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
app_name = 'socauth'

urlpatterns = patterns('',
    url(r'^$', 'socauth.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^email-sent/', 'socauth.views.validation_sent'),
    url(r'^login/$', 'socauth.views.home'),
    url(r'^logout/$', 'socauth.views.logout'),
    url(r'^done/$', 'socauth.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'socauth.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'socauth.views.require_email', name='require_email'),
)

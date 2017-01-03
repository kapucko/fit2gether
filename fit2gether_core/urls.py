from django.conf.urls import url

from . import views as core_views
from django.contrib.auth import views as auth_views
from .forms import  LoginForm


app_name = 'fit2gether_core'
urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^location/(?P<slug>[-\w]+)/$', core_views.LocationDetail.as_view(), name='location_detail'),
    url(r'^login/$', auth_views.login, {'template_name': 'fit2gether_core/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
]

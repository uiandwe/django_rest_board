__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url
from user_manager.views import login, login_validate



urlpatterns = patterns('',
                       url(r'^login/$', login),
                       url(r'^login/validate/$', login_validate),


                       )

__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url
from user_manager.views import login, login_validate, join_page



urlpatterns = patterns('',
                       url(r'^login/$', login),
                       url(r'^login/validate/$', login_validate),
                       url(r'^join/$', join_page),


                       )

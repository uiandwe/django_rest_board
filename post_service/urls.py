__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url
from post_service.views import post_list, login, login_validate



urlpatterns = patterns('',
                       url(r'^$', post_list),
                       url(r'^login/$', login),
                       url(r'^login/validate/$', login_validate),


                       )

__author__ = 'shibly'

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<poll_id>\d+)/$', views.detail, name="detail"),
                       url(r'^(?P<poll_id>\d+)/result/$', views.results, name="result"),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name="vote"))
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),

                       # Load URLconf from polls.url module if the url starts with /polls
                       url(r'^polls/', include('polls.urls', namespace='polls')),

                       # Examples:
                       # url(r'^$', 'sites.views.home', name='home'),
                       # url(r'^sites/', include('sites.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
)

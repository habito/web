from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),
    url(r'^browse/$', 'website.views.browse', name='browse'),  
    url(r'^sign_up/$', 'website.views.sign_up', name='sign_up'),
)

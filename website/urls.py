from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),
    url(r'^browse/$', 'website.views.browse', name='browse'),  
    url(r'^register/$', 'website.views.register', name='register'),
    url(r'^login/$', 'website.views.login_user', name='login_user'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^me/$', 'website.views.me', name='me'),
    url(r'^post/$', 'website.views.post', name='post'),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),
    url(r'^browse/$', 'listings.views.browse', name='browse'),  
    url(r'^register/$', 'user_profile.views.register', name='register'),
    url(r'^login/$', 'user_profile.views.login_user', name='login_user'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^me/$', 'user_profile.views.me', name='me'),
    url(r'^post/$', 'listings.views.post', name='post'),
)

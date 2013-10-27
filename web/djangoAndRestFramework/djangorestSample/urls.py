from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.models import User, Group

from django.contrib.auth import views as auth_views
from django import forms

from blogpost.views import UserViewSet,BlogPostViewSet,CategoryViewSet
from rest_framework import routers






router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("blogpost",BlogPostViewSet)
router.register("category",CategoryViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^logout/$',auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),   #required to explicitly define logout link otherwise facebook/example won't work
    # Examples:
    # url(r'^$', 'djangorestSample.views.home', name='home'),
    # url(r'^djangorestSample/', include('djangorestSample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))


)

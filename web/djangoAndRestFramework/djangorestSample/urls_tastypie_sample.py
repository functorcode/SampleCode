from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.models import User, Group

from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.validation import FormValidation

#from tastypie.authentication import SessionAuthentication
from blogpost.models import BlogPost,Category
from django.contrib.auth import views as auth_views
from tastypie import fields
from django import forms

class blogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','textData','category']

class UsersResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields=['username','first_name','last_name']
        resource_name = 'users'
        authorization = Authorization()

class CategoryResource(ModelResource):
    class Meta:
        queryset=Category.objects.all()
        resource_name='category'
        authorization=Authorization()

class BlogPostResource(ModelResource):
    createdBy=fields.ForeignKey(UsersResource,'createdBy',full=False)
    category=fields.ForeignKey(CategoryResource,'category',full=False)
    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = 'blogpost'
        authorization = Authorization()
        validation = FormValidation(form_class=blogPostForm)
    #    authentication= SessionAuthentication()


    def hydrate(self, bundle):

        if not bundle.data.has_key('createdBy') :
            bundle.data['createdBy']="/api/v1/users/"+str(bundle.request.user.pk)+"/"
        else:
            if not bundle.data['createdBy']=="/api/v1/users/"+str(bundle.request.user.pk)+"/":
                raise Unauthorized("Unauthorized access.")
            bundle.data['createdBy']=="/api/v1/users/"+str(bundle.request.user.pk)+"/"
        return bundle
        #authentication= SessionAuthentication()
      #  authentication= SessionAuthentication()


v1_api = Api(api_name='v1')
v1_api.register(UsersResource())
v1_api.register(BlogPostResource())
v1_api.register(CategoryResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^logout/$',auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
    # Examples:
    # url(r'^$', 'djangorestSample.views.home', name='home'),
    # url(r'^djangorestSample/', include('djangorestSample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))


)

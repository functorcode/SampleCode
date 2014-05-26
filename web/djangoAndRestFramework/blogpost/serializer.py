
from django.contrib.auth.models import User
from blogpost.models import BlogPost,Category
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','first_name','last_name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    category=serializers.SlugRelatedField(slug_field='title')

    class Meta:
        model=BlogPost
        fields=('url','title','textData','category','createdBy')
        read_only_fields=('createdBy',)  # logged in user will be assigned from pre_save() method of view set on POST method
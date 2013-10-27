# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets,routers
from blogpost.models import BlogPost,Category
from blogpost.serializer import UserSerializer,BlogPostSerializer,CategorySerializer
import django_filters

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class BlogPostFilters(django_filters.FilterSet):
    class Meta:
        model=BlogPost
        fields=['category__title','createdBy','title','postedDate']
        order_by =True  #apply order by on fields of filter


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **blogposts**.

    Following filters are available:

    1)By category : category__title=categoryname

    2)By author : createdBy =authorId

    3)Order by postedDate

    Sample:

     [By news]:(?category__title=news)

    1. [?category__title=news](?category__title=news)
    2. [?category__title=news&createdBy=2](?category__title=news&createdBy=2)

    You can sort by on all above field.For example, **?o=(+/-)fieldname**

    1.For ASC,  [?o=postedDate](?o=postedDate)

    2.For DESC,  [?o=-postedDate](?o=-postedDate)

    """



    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
   # filter_fields=("category__title","createdBy","title")
    filter_class=BlogPostFilters

    def pre_save(self,obj):
        obj.createdBy=self.request.user

Django and rest framework sample code

**Functionality included**


1. REST api usage and documentation sample (blogpost/views.py:BlogPostViewSet)

2. Facebook integration using django_facebook

3. Foreign key in serializer 

4. django_filters : (blogpost/views.py:BlogPostFilters)

  4.1 filter on Foreign key field (category__title)

  4.2 Order by 

5. Hyperlinked Serializer and viewset

**Run:**

1. Sync database : python manage.py syncdb

2. Load fixtures : python manage.py loaddata  fixtureData.json

3. Run server    : python manage.py runserver 8080


**Django and REST Framework in nutshell**


1. Create models
2. Create serializers to define fields you want to expose as api for each model.You can also add validation and derived field <http://django-rest-framework.org/api-guide/fields.html#serializermethodfield>
3. Create viewset and assign  serializer to it.
4. Create router and  register viewset 

To export data from database:

python manage.py dumpdata --indent 4 > fixtureData.json

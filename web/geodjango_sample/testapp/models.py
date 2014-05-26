#from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class NGO(models.Model):
    name=  models.CharField(max_length=30)
    location=models.PointField(srid=4326)
    object= models.GeoManager()

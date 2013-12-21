"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from testapp.models import NGO
from django.contrib.gis.geos import fromstr
#from django.contrib.gis.measure import D

class DistQueryTestCase(TestCase):
    def setUp(self):
        #sector-2 location
        pnt=fromstr('POINT(23.201868 72.637089)',srid=4326)
        NGO.object.create(name="sect-2",location=pnt)
    def test_lte_distance(self):

        sector3=fromstr('POINT(23.206996 72.633355)',srid=4326)
        kobacircle=fromstr('POINT(23.140676 72.630688)',srid=4326)
        #find ngo which are within range of  1000 m of sector 3
        result1=NGO.object.filter(location__distance_lte=(sector3,1000))
        #find ngo which are within  range of 1000 m of kobacircle
        result2=NGO.object.filter(location__distance_lte=(kobacircle,1000))
        #sector 2 is with in 8km range
        result3=NGO.object.filter(location__distance_lte=(kobacircle,8000))

        self.assertNotEqual(len(result1), 0)
        self.assertEqual(len(result2),0)
        self.assertNotEqual(len(result3),0,msg="sector2 is within 8 km range of kobacircle")

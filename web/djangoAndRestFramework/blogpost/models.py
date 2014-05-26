from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=10)


class BlogPost(models.Model):

    title=models.CharField(max_length=30)
    textData=models.TextField()
    createdBy=models.ForeignKey(User)
    postedDate=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category)

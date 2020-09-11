from django.db import models

# Create your models here.
from django.db.models import ImageField


class Destination(models.Model):

     name = models.CharField(max_length=50)
     image = models.ImageField(upload_to='pics')
     desc = models.CharField(max_length=500)
     price =  models.IntegerField()
     offer = models.BooleanField(default=False)
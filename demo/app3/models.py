from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

class Register(models.Model):
    name=models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=50)
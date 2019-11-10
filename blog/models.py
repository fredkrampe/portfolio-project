from django.db import models
from django.utils.timezone import now


# Create your models here.

class Blog(models.Model):

     image = models.ImageField(upload_to='images/')
     Title = models.CharField(max_length=100)
     publicationDate = models.DateField(default=now)
     body = models.TextField()


from django.db import models
from django.utils.timezone import now


# Create your models here.

class Blog(models.Model):

     image = models.ImageField(upload_to='images/')
     title = models.CharField(max_length=100)
     publicationDate = models.DateField(default=now)
     body = models.TextField()

     def __str__(self):
          return self.title
          
     def summary(self):
          return self.body[:100]
     
     def pub_date(self):
          return self.publicationDate.strftime('%b %e %Y')
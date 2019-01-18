from django.db import models

# Create your models here.
class Contingent(models.Model):

    number = models.IntegerField()
    college = models.CharField(max_length=200)
    
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)

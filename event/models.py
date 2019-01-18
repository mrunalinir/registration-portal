from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, blank=True, null=True)
    college = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    mode = models.CharField(max_length=10, null=True)

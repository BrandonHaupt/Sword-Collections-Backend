from django.db import models

# Create your models here.
class Swords(models.Model):
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    origin = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
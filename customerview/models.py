from django.db import models
from places.fields import PlacesField

# Create your models here.
class MyLocationModel(models.Model):
    location = PlacesField()
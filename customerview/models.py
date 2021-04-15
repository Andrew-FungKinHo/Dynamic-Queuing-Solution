from django.db import models
from places.fields import PlacesField

# Create your models here.
class MyLocationModel(models.Model):
    location = PlacesField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    currentLocation = models.CharField(max_length=100)

class Merchant(models.Model):
    name = models.CharField(max_length=20)
    profilePic = models.URLField(null=True)
    numberOfLikes = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('Dine In', 'Dine-in'),
        ('Takeaway', 'Take-away'),
        ('Delivery', 'Delivery'),
    ]
    orderType = models.CharField(max_length=8, choices=ORDER_TYPE_CHOICES)
    totalPrice = models.FloatField(null=True)
    startTime = models.DateField(max_length=20)
    endTime = models.DateField(max_length=20)
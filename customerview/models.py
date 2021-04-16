from django.db import models
from places.fields import PlacesField

# Create your models here.
class MyLocationModel(models.Model):
    location = PlacesField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    currentLocation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Merchant(models.Model):
    name = models.CharField(max_length=20)
    profilePic = models.URLField(null=True)
    numberOfLikes = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('Dine In', 'Dine-in'),
        ('Takeaway', 'Take-away'),
        ('Delivery', 'Delivery'),
    ]
    customerConcerned = models.ForeignKey('Customer',null=True,on_delete=models.SET_NULL)
    merchantConcerned = models.ForeignKey('Merchant',null=True,on_delete=models.SET_NULL)
    orderType = models.CharField(max_length=8, choices=ORDER_TYPE_CHOICES)
    totalPrice = models.FloatField(null=True)
    orderCreated = models.TimeField(auto_now=True) 
    eta = models.FloatField(default=-1)

    def __str__(self):
        return self.orderType

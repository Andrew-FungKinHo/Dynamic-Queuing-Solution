from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import googlemaps
from datetime import datetime
from django.conf import settings

# Create your views here.

# return the ETA in seconds. incorrect name will return -1
def getETA(origin, destination):
    gmaps = googlemaps.Client(key=settings.PLACES_MAPS_API_KEY)

    # Request directions via public transit
    now = datetime.now()

    directions_result = gmaps.directions(origin,
                                        destination,
                                        mode="transit",
                                        departure_time=now)
    try:
        return (directions_result[0]['legs'][0]['duration']['value'])/ 60
    except :
        return -1

def home(request):
    return render(request,'customerview/home.html')

def customer(request):
    return render(request,'customerview/customer.html')

def merchant(request):
    return render(request,'customerview/merchant.html')

def delivery(request):
    return render(request,'customerview/delivery.html')

def order(request):
    # orders = Order.save)
    # first_Order = Order.objects.get(id=1)

    # customerLocation = Order.objects.get(id=)
    # merchantLocation = Order.objects.get(id=)
    # eta = getETA(customerLocation,merchantLocation)

    for order in Order.objects.all():
        # order = Order.objects.get(id=i)
        # print(order.customerConcerned)
        customerLocation = order.customerConcerned.currentLocation
        merchantLocation = order.merchantConcerned.address
        eta = getETA(customerLocation,merchantLocation)
        order.eta = eta
        order.save()

    context = {
        'orders': Order.objects.all()
    }
    return render(request,'customerview/orderList.html',context)
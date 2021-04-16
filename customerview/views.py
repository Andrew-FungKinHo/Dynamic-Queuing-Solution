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




def dineInHomepage(request):
    return render(request,'customerview/dine-in-homepage.html')

def takeOutHomepage(request):
    return render(request,'customerview/take-out-homepage.html')

def customerReview1(request):
    return render(request,'customerview/customer-review-1.html')

def customerReview2(request):
    return render(request,'customerview/customer-review-2.html')
    
def deliveryCheckout(request):
    return render(request,'customerview/delivery-checkout.html')

def deliveryHomepage(request):
    return render(request,'customerview/delivery-homepage.html')

def deliveryOrderConfirmation(request):
    return render(request,'customerview/delivery-order-confirmation.html')

def deliveryRestaurant(request):
    return render(request,'customerview/delivery-restaurant.html')
    
def dineInCheckout(request):
    return render(request,'customerview/dine-in-checkout.html')

def dineInOrderConfirmation(request):
    return render(request,'customerview/dine-in-order-confirmation.html')

def reservationComplete(request):
    return render(request,'customerview/reservation-complete.html')
    
def reserveForLater(request):
    return render(request,'customerview/reserve-for-later.html')

def reserveForLaterComplete(request):
    return render(request,'customerview/reserve-for-later-complete.html')

def reserveForNowNoPo(request):
    return render(request,'customerview/reserve-for-now-no-po.html')

def reserveForNowPo(request):
    return render(request,'customerview/reserve-for-now-po.html')

def takeOutCheckout(request):
    return render(request,'customerview/take-out-checkout.html')

def takeOutOrderConfirmation(request):
    return render(request,'customerview/take-out-order-confirmation.html')

def takeOutRestaurant(request):
    return render(request,'customerview/take-out-restaurant.html')
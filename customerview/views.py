from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'customerview/home.html')

def customer(request):
    return render(request,'customerview/customer.html')

def merchant(request):
    return render(request,'customerview/merchant.html')

def delivery(request):
    return render(request,'customerview/delivery.html')

def order(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request,'customerview/orderList.html',context)
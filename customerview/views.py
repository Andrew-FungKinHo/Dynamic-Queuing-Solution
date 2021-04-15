from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'customerview/home.html')

def customer(request):
    return render(request,'customerview/customer.html')

def merchant(request):
    return render(request,'customerview/merchant.html')

def delivery(request):
    return render(request,'customerview/delivery.html')

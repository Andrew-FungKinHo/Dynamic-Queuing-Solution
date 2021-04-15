from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer),
    path('merchant/', views.merchant),
    path('delivery/', views.delivery),
    path('order/', views.order),
]
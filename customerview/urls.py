from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer),
    path('merchant/', views.merchant),
    path('delivery/', views.delivery),
    path('order/', views.order),


    
    path('dine-in-homepage/', views.dineInHomepage),
    path('take-out-homepage/', views.takeOutHomepage),
    path('customer-review-1/', views.customerReview1),
    path('customer-review-2/', views.customerReview2),
    path('delivery-checkout/', views.deliveryCheckout),
    path('delivery-homepage/', views.deliveryHomepage),
    path('delivery-order-confirmation/', views.deliveryOrderConfirmation),
    path('delivery-restaurant/', views.deliveryRestaurant),
    path('dine-in-checkout/', views.dineInCheckout),
    path('dine-in-order-confirmation/', views.dineInOrderConfirmation),
    path('reservation-complete/', views.reservationComplete),
    path('reserve-for-later/', views.reserveForLater),
    path('reserve-for-later-complete/', views.reserveForLaterComplete),
    path('reserve-for-now-no-po/', views.reserveForNowNoPo),
    path('reserve-for-now-po/', views.reserveForNowPo),
    path('take-out-checkout/', views.takeOutCheckout),
    path('take-out-order-confirmation/', views.takeOutOrderConfirmation),
    path('take-out-restaurant/', views.takeOutRestaurant),
 
]
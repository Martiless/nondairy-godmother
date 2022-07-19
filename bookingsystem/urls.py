# This file contains all the URLs for the booking site
from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('menus/', views.Menus.as_view(), name='menus'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    path('my_bookings/', views.ListBookingView.as_view(), name='my_bookings'),
    path('edit_bookings.html/', views.EditBookingsView.as_view(), name='edit_bookings'),
]

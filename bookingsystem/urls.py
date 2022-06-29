from . import views
from .views import BookingForm
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', BookingForm.as_view(), name='bookings'),
    path('menus/', views.Menus.as_view(), name='menus'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    path('edit_bookings', views.editBooking.as_view(), name='edit_bookings'),
]

from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.BookingForm, name='booking')
]
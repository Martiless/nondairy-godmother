from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home, name='home'),
    path('', views.BookingForm, name='booking'),
    path('', views.Menus, name='menus'),
    path('', views.Login, name='login'),
]
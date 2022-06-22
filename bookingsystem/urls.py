from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingForm.as_view(), name='booking'),
    path('menus/', views.Menus.as_view(), name='menus'),
    #path('login/', views.Login.as_view(), name='login'),
]
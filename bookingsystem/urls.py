from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', views.BookingForm.as_view(), name='booking'),
    path('', views.Menus.as_view(), name='menus'),
    path('', views.Login.as_view(), name='login'),
]
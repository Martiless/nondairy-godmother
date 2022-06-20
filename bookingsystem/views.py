from django.shortcuts import render
from django.views import generic
from .models import Booking

class Home(generic.DetailView):
    template_name = 'index.html'

class BookingForm(generic.FormView):
    form = Booking
    template_name = 'bookings.html'

class Menus(generic.DetailView):
    template_name = 'menus.html'

class Login(generic.DetailView):
    template_name = 'login.html'

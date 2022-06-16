from django.shortcuts import render
from django.views import generic
from .models import Booking

class BookingForm(generic.FormView):
    form = Booking
    template_name = 'book_a_table.html'

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Booking


class Home(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
          return render(request, 'index.html')


class BookingForm(generic.DetailView):
    form = Booking
    template_name = 'bookings.html'

    def get(self, request):
          return render(request, 'bookings.html')


class Menus(generic.DetailView):
    template_name = 'menus.html'

    def get(self, request):
          return render(request, 'menus.html')


class Sign_in(generic.DetailView):

    def login_view(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            return render(request, 'login.html')


#class BookingList(generic.ListView)

class editBooking(generic.DetailView):
    template_name = 'edit_bookings.html'

    def get(self, request):
        return render(request, 'edit_bookings.html')

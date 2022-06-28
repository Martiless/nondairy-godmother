from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import FormView
from .forms import OnlineForm


class Home(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
          return render(request, 'index.html')


class BookingForm(FormView):
    form_class = OnlineForm()
    args = {}
    def booking_view(self, request):
        if request.method == 'POST':
            form = OnlineForm(request.POST)
        
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
            return render(request, 'login.html')


#class BookingList(generic.ListView)

class editBooking(generic.DetailView):
    template_name = 'edit_bookings.html'

    def get(self, request):
        return render(request, 'edit_bookings.html')

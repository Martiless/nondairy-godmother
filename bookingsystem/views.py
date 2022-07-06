from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
from .forms import OnlineForm, EditBookingForm
from django.contrib import messages
from django.urls import reverse_lazy



class Home(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
          return render(request, 'index.html')


class BookingForm(FormView):
    template_name = 'bookings.html'
    form_class = OnlineForm
    success_url = '/thank_you/'

    def booking_view(self, request):   
        return render(request, 'bookings.html')
    
    def post(self, request):
        form = OnlineForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=True)
            booking.save()

        return render(request, 'thank_you.html')


class ThankYou(generic.DetailView):
    template_name = 'thank_you.html'

    def get(self, request):
        return render(request, 'thank_you.html')

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


class TableList(generic.ListView):
    template_name = 'table_listing.html'

    def get(self, request):
        return render(request, 'table_listing.html')


class editBooking(FormView):
    template_name = 'edit_bookings.html'
    form_class = EditBookingForm
    success_url = '/thank_you/'
    
    def edit_booking_form(request):
        if request.method == 'POST':
            searched = request.POST['searched']
            
            return render(request, 'edit_bookings.html', {'searched':searched} )
        else:
            return render(request, 'edit_bookings.html')


        

from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView
from .forms import OnlineForm
from .models import Booking


class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    template_name = 'index.html'

# The get request returns the template set out above
# In this case it was the index.html template
    def get(self, request):
        return render(request, 'index.html')


class BookingView(FormView):
    """
    Renders the Booking form page in the browser
    """
    template_name = 'bookings.html'
    form_class = OnlineForm
    success_url = '/thank_you/'

    def booking_view(self, request):
        return render(request, 'bookings.html')

    def post(self, request):
        form = OnlineForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

        return render(request, 'thank_you.html')


class ThankYou(generic.DetailView):
    """
    Renders the Thank You page in the browser
    """
    template_name = 'thank_you.html'

    def get(self, request):
        return render(request, 'thank_you.html')


class Menus(generic.DetailView):
    """
    Renders the Menu page in the browser
    """
    def get(self, request):
        return render(request, 'menus.html')


class SignIn(generic.DetailView):
    """
    Renders the Login page in the browser
    """

    def login_view(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            return render(request, 'login.html')


class ListBookingView(generic.DetailView):
    """
    This is the view that will bring up the
    list of bookings for a particular users
    so that they can be edited or deleted
    """

    template_name = 'my_bookings.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'my_bookings.html', {
                'bookings': bookings
            }
            )
        else:
            return redirect('account_login')


class EditBookingsView(FormView):


    template_name = 'edit_bookings.html'
    form_class = OnlineForm
    success_url = '/my_bookings/'

    def edit_bookings(request, booking_id):
        return render(request, 'edit_bookings.html')

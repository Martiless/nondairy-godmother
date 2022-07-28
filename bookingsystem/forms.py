from django.forms import ModelForm
from django import forms
from .models import Booking, SignUp


class DateInput(forms.DateInput):
    """
    This class provides a widget for use in the
    booking form. It provides a calendar for users
    to pick the booking date from
    """
    input_type = 'date'


class OnlineForm(ModelForm):
    """
    This form is connected with the view
    in order to provide users with the neccessary
    fields for making a booking
    """
    class Meta:
        """Defines which model to pull the
        fields from"""
        model = Booking
        # Tell the form to use all the fields provided
        fields = '__all__'
        # Except fot the user field
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }

class SignUpForm(ModelForm):
    """
    This form is connected with the Signup view
    so that visiters to the site can sign up 
    for the restaurants newsletter
    """
    class Meta:
        """Defines which model to pull the
        fields from"""
        model = SignUp
        # Tell the form to use all the fields provided
        fields = '__all__'
       
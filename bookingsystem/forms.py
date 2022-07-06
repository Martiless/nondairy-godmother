from django.forms import ModelForm
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class OnlineForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }


class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'number_of_people', 'date', 'time']
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

from django.forms import ModelForm
from .models import Booking


class OnlineForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


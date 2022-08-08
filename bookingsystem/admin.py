from django.contrib import admin
from .models import Booking, SignUp


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('name', 'email_address')


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    model = SignUp
    list_display = ('__all__')

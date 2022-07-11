from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('get_name', 'get_date', 'get_time', 'get_pax')

admin.site.register(Booking)

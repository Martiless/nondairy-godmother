from django.contrib import admin
from .models import Booking
from .models import Table


class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('get_name', 'get_date', 'get_time', 'get_pax')

admin.site.register(Booking)
admin.site.register(Table)

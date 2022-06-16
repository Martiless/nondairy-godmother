from . import views
from django.urls import path


urlpatterns = [
    path('book_a_table', views.BookingForm.as_view(), name='booking')
]
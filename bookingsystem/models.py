from django.db import models
from django.contrib.auth.models import User


# class Customer(models.Model):

class Booking(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone = models.IntegerField()
    pax = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    occasion = models.TextField(max_length=500)

    def __str__(self):
        return self.name



class Table(models.Model):
    #table_number = models.IntegerField()
    number_of_seats = models.IntegerField()
    max_pax = models.IntegerField()
    min_pax = models.IntegerField()

    def __str__(self):
        return self

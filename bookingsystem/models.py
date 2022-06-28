from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# class Customer(models.Model):

OCCASION_CHOICE = (
    ('Birthday', 'BIRTHDAY'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Graduation', 'GRADUATION'),
    ('Communion', 'COMMUNION'),
    ('Confirmation', 'CONFIRMATION'),
    ('Christening', 'CHRISTENING'),
    ('Date Night', 'DATE NIGHT'),
)

class Booking(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone = models.IntegerField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],default='1', help_text='For parties of more than 10, please call us on 021 4569 782')
    date = models.DateField()
    time = models.TimeField()
    occasion = models.CharField(max_length=100, choices=OCCASION_CHOICE, default='Birthday')

    def __str__(self):
        return self.name



class Table(models.Model):
    TableNo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],default='1')
    number_of_seats = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],default='1')
    max_pax = models.IntegerField()
    min_pax = models.IntegerField()

    def __str__(self):
        return self

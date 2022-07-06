from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


"""
The choice which are presented to people making bookings
and staff assiging tables
"""

OCCASION_CHOICE = (
    ('Birthday', 'BIRTHDAY'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Graduation', 'GRADUATION'),
    ('Communion', 'COMMUNION'),
    ('Confirmation', 'CONFIRMATION'),
    ('Christening', 'CHRISTENING'),
    ('Date Night', 'DATE NIGHT'),
)


TABLE_CHOICE = (
    ('Window', 'WINDOW'),
    ('Outside', 'OUTSIDE'),
    ('Inside', 'INSIDE'),
    ('Booth', 'BOOTH'),
)


TABLE_NUMBER = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),

)

TABLE_CAPACITY = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

"""
Models to be used in the forms.py and views.py
"""


class Table(models.Model):
    Table_number = models.CharField(max_length=10, choices=TABLE_NUMBER, default='1')
    max_pax = models.CharField(max_length=10, choices=TABLE_CAPACITY, default='2')

    def __str__(self):
        return self



class Booking(models.Model):
    name = models.CharField(max_length=60)
    email_address = models.EmailField(primary_key=True)
    phone = models.IntegerField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default='1', help_text='For parties of more than 10, please call us on 021 4569 782')
    date = models.DateField()
    time = models.TimeField()
    occasion = models.CharField(max_length=100, choices=OCCASION_CHOICE, default='Birthday')

    def __str__(self):
        return self.name

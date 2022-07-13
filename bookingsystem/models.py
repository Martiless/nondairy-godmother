from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# The choice which are presented to people making bookings

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


class Booking(models.Model):
    """
    Model to be used in the forms.py and views.py.
    It uses the User Foreign Key so that each book will be associated with a
    specific user.
    The rest of the information is saved for the booking
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default='1', help_text='For parties of more than 10, please call us on 021 4569 782')
    date = models.DateField()
    time = models.TimeField()
    table = models.CharField(max_length=50, choices=TABLE_CHOICE, default='Inside')
    occasion = models.CharField(max_length=100, choices=OCCASION_CHOICE, default='Birthday')

    def __str__(self):
        return self.name

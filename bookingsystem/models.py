from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# The choice which are presented to people making bookings

TIME_CHOICE = (
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),

)

OCCASION_CHOICE = (
    ('Birthday', 'BIRTHDAY'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Graduation', 'GRADUATION'),
    ('Communion', 'COMMUNION'),
    ('Confirmation', 'CONFIRMATION'),
    ('Christening', 'CHRISTENING'),
    ('Date Night', 'DATE NIGHT'),
    ('Friends Night', 'FRIENDS NIGHT'),
    ('None', 'None'),
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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings"
        )
    name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    number_of_people = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default='1',
        help_text='For parties of more than 10, please call us on 021 4569 782'
        )
    date = models.DateField()
    time = models.CharField(
        max_length=50, choices=TIME_CHOICE, default='12:00'
        )
    table = models.CharField(
        max_length=50, choices=TABLE_CHOICE, default='Inside'
        )
    occasion = models.CharField(
        max_length=100, choices=OCCASION_CHOICE, default='Birthday'
        )

    def __str__(self):
        return self.name

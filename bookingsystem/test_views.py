from django.test import TestCase, Client
from django.urls import reverse
from bookingsystem.models import Booking, SignUp
from django.contrib.auth.models import User



class TestViews(TestCase):
    """
    Testing of the views taken from
    the views.py file.
    All HTTP testing includes the base.html template
    as well as the view being tested to make sure everything
    is being tested as it would appear for a user
    """

    def test_home_view_get(self):
        """
        Testing the HTTP response of the view using
        Djangos built-in HTTP response with a status code
        of 200 which is a successful HHTP response.
        Using the '/' will direct to the Home page.
        To make sure the view is using the correct
        template Template Used is index.html
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_menus_view_get(self):
        """
        Testing the HTTP response of the view using
        Djangos built-in HTTP response with a status code
        of 200 which is a successful HHTP response.
        Using the '/menus/' will direct to the Menus page.
        To make sure the view is using the correct
        template Template Used is menus.html
        """
        response = self.client.get('/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menus.html', 'base.html')

    def test_thank_you_view_get(self):
        """
        Testing the HTTP response of the view using
        Djangos built-in HTTP response with a status code
        of 200 which is a successful HHTP response.
        Using the '/thank_you/' will direct to the Thank You page.
        To make sure the view is using the correct
        template Template Used is thank_you.html
        """
        response = self.client.get('/thank_you/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thank_you.html', 'base.html')

    def test_sign_up(self):
        """
        Testing the HTTP response of the view using
        Djangos built-in HTTP response with a status code
        of 200 which is a successful HHTP response.
        Using the '/sign_up' will direct to the Sign Up page.
        To make sure the view is using the correct
        template Template Used is sign_up.html
        """
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html', 'base.html')

    def test_booking_view(self):
        """
        Testing the HTTP response of the view using
        Djangos built-in HTTP response with a status code
        of 200 which is a successful HHTP response.
        Using the '/bookings' will direct to the Bookings page.
        To make sure the view is using the correct
        template Template Used is bookings.html
        """
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html', 'base.html')

    def test_my_booking_view(self):
            """
            Testing the HTTP response of the view using
            Djangos built-in HTTP response with a status code
            of 200 which is a successful HHTP response.
            Using the '/my_bookings' will direct to the My Bookings page.
            To make sure the view is using the correct
            template Template Used is my_bookings.html
            """
            response = self.client.get('/my_bookings/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'my_bookings.html', 'base.html')
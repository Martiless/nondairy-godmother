from django.test import TestCase, Client
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

    def setUp(self):
        """
        Set up test users and booking in
        order to test the CRUD functionality
        of the views"""
       
        testing_user = User.objects.create_user(
            username='JohnSmith',
            first_name='John',
            last_name='Smith',
            email='johnsmith@email.com',
            password='RandomWord1'
        )

        Booking.objects.create(
            user=testing_user,
            name='John Smith',
            email_address='johnsmith@email.com',
            phone='123654789',
            number_of_people='2',
            date='2022-10-20',
            time='19:00',
            table='Window',
            occasion='none'
        )

        SignUp.objects.create(
            first_name='Cindy Lou',
            last_name='Who',
            email_address='cindylou@whovill.com'
        )

    def log_in(self):
        """
        This is to help test the views
        that require a user to be logged in
        to access
        """
        self.client.login(
            username='JohnSmith',
            password='RandomWord1'
        )


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
        Using the log_in function saved above to test
        the HTTP response of the 'My Bookings' page
        Using the '/my_bookings' will direct to the My Bookings page.
        To make sure the view is using the correct
        template Template Used is my_bookings.html
        """
        self.log_in()
        response = self.client.get('/my_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_bookings.html', 'base.html')

    def test_edit_bookings_view(self):
        """
        Using the log in function saved above to test
        the HTTP reponse of the 'Edit booking' page.
        Using the '/edit_bookings/1 url this will direct to
        the booking outlined in the booking id.
        To make sure the view is using the correct
        template Tempalte Used is set to edit_booking.html
        """
        self.log_in()
        response = self.client.get('/edit_bookings/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_bookings.html', 'base.html')

    def test_add_booking(self):
        """
        Testing the CRUD functionality 
        of the app is working as it should
        """
        self.log_in()
        response = self.client.post('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bookings")

    def test_edit_booking(self):
        """
        This is use a booking that is
        created within the test to
        test the CRUD functionality
        of the app is working correctly
        """
        self.log_in()
        booking = Booking.objects.create(
            user='JohnSmith',
            name='John Smith',
            email_address='johnsmith@email.com',
            phone='123654789',
            number_of_people='2',
            date='2022-10-20',
            time='19:00',
            table='Window',
            occasion='none'
        )
        response = self.client.get(f'edit_bookings/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_bookings.html')

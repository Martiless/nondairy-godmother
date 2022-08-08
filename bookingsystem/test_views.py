from django.test import TestCase, Client
from django.urls import reverse
from bookingsystem.models import Booking, SignUp


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('Home')

    def test_home_view_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsystem/')

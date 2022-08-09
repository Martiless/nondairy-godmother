from django.test import TestCase, Client
from django.urls import reverse
from bookingsystem.models import Booking, SignUp


class TestViews(TestCase):
    def test_home_view_GET(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

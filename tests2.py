from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import home

class UrlTest(SimpleTestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

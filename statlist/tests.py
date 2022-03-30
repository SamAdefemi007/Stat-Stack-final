from django.test import TestCase, SimpleTestCase,Client
from statlist.views import home, profile, details, country, club
from django.urls import reverse, resolve
# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_club_url_resolves(self):
        url = reverse('club')
        self.assertEqual(resolve(url).func, club)

    def test_country_url_resolves(self):
        url = reverse('country')
        self.assertEqual(resolve(url).func, country)

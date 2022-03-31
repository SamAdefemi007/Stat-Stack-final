from django.test import TestCase, SimpleTestCase,Client
from statlist.views import home, profile, details, country, club, compare
from .models import Country, Club, Skills, TransferMarket, Player
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

    def test_compare_url_resolves(self):
        url = reverse('compare')
        self.assertEqual(resolve(url).func, compare)

class TestOtherUrls(TestCase):

    def test_details_url_resolves(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.club_url = reverse('club')
        self.country_url = reverse('country')
        self.compare_url = reverse('compare')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/profile.html')
        self.assertContains(response, "FIFA World Best Footballers")

    def test_club_GET(self):
        response = self.client.get(self.club_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/club.html')
        self.assertContains(response, "Please Select the Club")

    def test_country_GET(self):
        response = self.client.get(self.country_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/country.html')
        self.assertContains(response, "Please Select the country")

    def test_compare_GET(self):
        response = self.client.get(self.compare_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/compare.html')

#testing the string representation of the Models

class TestModelsString(TestCase):
    def setUp(self):
        self.countryobj = Country(countryName = "Argentina", countryFlag = "https://cdn.sofifa.com/flags/ar.png")
        self.clubobj = Club(clubName = "Barcelona", clubLogo = "https://cdn.sofifa.com/teams/241/30.png")
        self.skillsobj = Skills(prefferedFoot = "right", pace=100, shooting =100, passing=100, strength =100, dribbling=100, defending=100, rating=100)
        self.transferobj = TransferMarket(value="36M", contractExpiry = 2022, wages= "300k", releaseClause ="128M")
        self.playerobj = Player(playerName = "L.Messi", playerAge=35, playerPhoto = "https://cdn.sofifa.com/players/158/023/22_60.png", playerPosition="LW", playerCountry= self.countryobj
        ,playerClub=self.clubobj, skills = self.skillsobj, playerValue = self.transferobj)
    


    def test_string_country(self):
        self.assertEqual(str(self.countryobj), self.countryobj.countryName)

    def test_string_club(self):
        self.assertEqual(str(self.clubobj), self.clubobj.clubName)

    def test_string_Skills(self):
        self.assertEqual(str(self.skillsobj), f"{self.skillsobj.rating}, {self.skillsobj.prefferedFoot}")

    def test_string_TransferMarket(self):
        self.assertEqual(str(self.transferobj), str((self.transferobj.value, self.transferobj.wages, self.transferobj.releaseClause, self.transferobj.contractExpiry)))

    def test_string_club(self):
        self.assertEqual(str(self.playerobj), str((self.playerobj.playerName, self.playerobj.playerAge, self.playerobj.playerPosition)))
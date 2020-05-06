"""Test fixtures for the api app


"""

from django.test import TestCase
from api.models import City


class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(city="Yoorana", state="Victoria", rank=999)
        City.objects.create(city="Eros", state="Belter", rank=13)


    def test_city_has_rank(self):
        yoorana =  City.objects.get(city="Yoorana")
        eros = City.objects.get(city="Eros")
        self.assertEqual(yoorana.rank, 999)
        self.assertEqual(eros.rank, 13)


    def test_city_has_state(self):
        belter = City.objects.get(city="Eros")
        victoria = City.objects.get(city="Yoorana")
        self.assertEqual(belter.state, "Belter")
        self.assertEqual(victoria.state, "Victoria")


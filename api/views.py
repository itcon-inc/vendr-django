"""The api app views module


Visualizes the api app data
"""

from rest_framework import viewsets

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ModelViewSet):
    """
    Queries the database for all city data
    """
    queryset = City.objects.all().order_by('city')
    serializer_class = CitySerializer

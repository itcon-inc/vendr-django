"""The serializer module


This module serializes the city data and identifies the fields used
"""

from rest_framework import serializers

from .models import City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    """
    A representation of a city serializer
    """
    class Meta:
        """
        The meta class represents the actual fields used
        """
        model = City
        fields = ('id', 'city', 'rank', 'state')

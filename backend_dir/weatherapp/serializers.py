#weatherapp/serializers.py
from rest_framework import serializers
from .models import Weather

# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields='__all__'

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'


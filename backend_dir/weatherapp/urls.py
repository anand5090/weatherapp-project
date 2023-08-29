from django.urls import path
from .views import WeatherView

urlpatterns = [
    path('get_weather', WeatherView.as_view(), name='get_weather'),
]

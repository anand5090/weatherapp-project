import requests
from django.http import JsonResponse
from django.views import View


class WeatherView(View):
    def get(self, request, *args, **kwargs):
        city_name = request.GET.get('city')
        # city_name = request.POST.get('city', 'mau')  # Default to Pune if no city is provided
        api_key = "10ca9bd218a8939f7f58a9339f7f2e10"
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
        
        response = requests.get(url)
        data = response.json()

        # Print the API response to examine its structure
        print(data)

        # Extract required weather information from the data
        weather_info = {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"], 
            "pressure": data["main"]["pressure"],
            "weathermood": data["weather"][0]["main"],
            "name": data["name"],
            "speed": data["wind"]["speed"],
            "country": data["sys"]["country"],
            "sunset": data["sys"]["sunset"],

        }

        return JsonResponse(weather_info)



















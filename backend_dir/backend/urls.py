# from django.contrib import admin
# from django.urls import path
# from weatherapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('weather/<str:city_name>/', views.get_weather, name='get_weather'),
   
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapp.urls')),  # Use an appropriate URL prefix
]



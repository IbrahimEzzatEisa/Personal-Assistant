import re
import urllib
import webbrowser
import requests
from geotext import GeoText
class WeatherC :
    def __inti__(self):
        self.weather_text=None
        self.city=None

    def weatherForecast(self,cityName):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

        url = api_address + cityName

        json_data = requests.get(url).json()
        formatted_data = json_data['weather'][0]['description']
        return formatted_data


# from geotext import GeoText
#
# places = GeoText("london is a great city and Cairo and Paris and Egypt")
# print(places.countries)
# print(WeatherC().weatherForecast())
# print(WeatherC().weatherForecast('cairo'))
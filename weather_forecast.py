import requests 
import os
from pprint import pprint
from datetime import datetime

api_key = os.environ.get('WEATHER_KEY')

if api_key is None:
    print('The api key couldn\'t be found')
else:
    city = input('Enter a city name ')
    country = input('Enter the country code ')
    location = city + ',' + country 

url = 'http://api.openweathermap.org/data/2.5/forecast'

query = {
    'q': location,
    'units': 'imperial',
    'appid': api_key
}

try:
    data = requests.get(url, params=query).json()

    if 'list' in data:
        forescast_data = data['list']

        for forescast in forescast_data:
            timestamp = forescast['dt']
            temperature = forescast['main']['temp']
            weather_description = forescast['weather'][0]['description']
            wind_speed = forescast['wind']['speed']
            date = datetime.fromtimestamp(timestamp)

            print(f"The day and time are: {date}")
            print(f'The temperature is: {temperature}')
            print(f"At this time we can describe the weather as: {weather_description}")
            print(f"The wind speed is: {wind_speed}")
    else:
        print('No data was found for the input location')
except Exception:
    print(f'An error was occurred: {Exception}')

    
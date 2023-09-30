#import requests


#try:
    #response = requests.get('https://catfact.ninja/fact')
    #print(response.status_code)
    #response.raise_for_status()  # raise an exception for 400 or 500 status code
    #print(response.text)
    #print(response.json())

    #data = response.json()
    #fact = data['fact']
    #print(f'A random cat fact is {fact}')

#except Exception as e:
    #print(e)
    #print('There was an error making the request.')

from pprint import pprint
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=miami,us&units=imperial&appid=d4d45483fdf50fc7303bd92cb4a79eae'

data = requests.get(url).json()

pprint(data)

temp = data['main'] ['temp']
print('The current temperature is {temp}F')
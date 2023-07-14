import requests
import json

API_KEY = '674f4f59440ce3c5f050b58d10bee8bc'
URL = f"https://api.openweathermap.org/data/2.5/weather"


def get_current_temperature(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Request temperature in Celsius
    }
    # 'imperial' for Fahrenheit
    # 'standard' for Kelvin

    response = requests.get(URL, params=params)
    data = json.loads(response.text)
    print(data)  # Print the complete API response for inspection
    temp = data['main']['temp']
    return temp


print("Welcome to Temperature Tracker Project Created by Indir Solanki\n")

city_name = input("Enter city name: ")
temperature = get_current_temperature(city_name)
print(f"\nThe current temperature in {city_name} is {temperature}°C.")

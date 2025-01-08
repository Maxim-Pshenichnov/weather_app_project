import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city, units='celsius'):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        formatted_data = []
        for item in data["list"]:
            date = item["dt_txt"]
            temp = item["main"]["temp"]
            description = item["weather"][0]["description"]
            icon = item["weather"][0]["icon"]
            formatted_data.append({
                "date": date,
                "temp": temp,
                "description": description,
                "icon": icon,
            })
        return formatted_data
    else:
        return None

def get_forecast_data(city, units="celsius"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dates = [item["dt_txt"] for item in data["list"]]
        temps = [item["main"]["temp"] for item in data["list"]]
        return dates, temps
    else:
        return None, None

def get_city_coordinates(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return lat, lon
    return None, None

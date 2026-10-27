import requests
from datetime import datetime, timedelta, timezone
url = 'https://api.openweathermap.org/data/2.5/weather'


params = {
    "q": 'Voronezh',
    "appid": 'c65fe8935b63007d34fe5cb6f1f13ae0',
    "units": 'metric'
    }

response = requests.get(url, params=params)

if response.status_code == 200:
    weather_data = response.json()
    timezone_offset = weather_data['timezone']
    city_timezone = timezone(
    timedelta(seconds=timezone_offset)
    )
    current_time = datetime.now(city_timezone)
    print(current_time.strftime('%H:%M:%S'))
    print(list(params.values())[0])
    # Precipitation, humidity, description, temp, wind
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    speed = weather_data['wind']['speed']
    degrees = weather_data['wind']['deg']
    description = weather_data['weather'][0]['description']

    print(f"Temperature: {temperature} °C ({(temperature*9/5)+32} °F)")
    print(f"Feels like: {feels_like} °C ({(temperature*9/5)+32} °F)")
    print(f"Humidity: {humidity}%")
    print(f"Wind:\nSpeed: {speed} kmh\nDirection: {degrees}°")
    print(f"{description}")
else:
    print("Server error. Weather data could not be fetched")

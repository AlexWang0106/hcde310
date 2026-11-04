import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 47.6062,
    "longitude": -122.3321,
    "current": "temperature_2m,precipitation,wind_speed_10m",
    "timezone": "America/Los_Angeles"
}

response = requests.get(url, params=params, timeout=10)

if response.status_code == 200:
    data = response.json()
    current = data["current"]

    print("Current weather in Seattle")
    print("Time:", current["time"])
    print("Temperature:", current["temperature_2m"], "°C")
    print("Precipitation:", current["precipitation"], "mm")
    print("Wind speed:", current["wind_speed_10m"], "km/h")
else:
    print("API request failed:", response.status_code)
# Open-Meteo API Guide

## 1. What is Open-Meteo?

Open-Meteo is a free weather API that provides current weather conditions and forecasts for locations around the world. It includes information such as temperature, precipitation, and wind speed. It can be useful for designers who want to build weather-related applications, travel planners, or outdoor activity tools. For non-commercial projects, it does not require an API key, making it easy to get started.

Documentation: https://open-meteo.com/en/docs

## 2. Setup

I tested this API using Python and the `requests` library in VS Code.

1. Install Python and open a project folder in VS Code.
2. Install the requests library:

   `python -m pip install requests`

3. Create a Python file.
4. Import `requests` and use the Open-Meteo forecast endpoint.
5. Run the script using the code in my example

No account or API key is required for the free non-commercial API.

## 3. Working Example

This example uses the coordinates of Seattle to request the current temperature, precipitation, and wind speed.There are many other weather data and forcast data(humidity,weather code,cloud cover, wind direction ETC), but to keep the example short and readable I am only using current tempreture, precipitation and wind speed.

Code (`example.py`):

```python
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
```

Actual output from my test:

Current weather in Seattle
Time: 2026-11-03T21:30
Temperature: 6.3 °C
Precipitation: 0.0 mm
Wind speed: 8.7 km/h

The `params` dictionary specifies the location and the weather data to request. `requests.get()` sends the API request, and `response.json()` converts the response into a Python dictionary. The script then extracts the `current` weather data and prints the values.

## 4. Gotchas

Coordinates: The forecast API uses latitude and longitude rather than city names. You need to find the coordinates before making a request.
Units: The default units are Celsius for temperature and km/h for wind speed. Make sure the units are the unit you are lookong for.
Rate limits: The free non-commercial API is limited to fewer than 10,000 calls per day, 5,000 per hour, and 600 per minute.
Missing data or request failures: Weather values may be unavailable, and network requests can fail. Applications should handle these cases rather than assume every request succeeds.
Weather accuracy: Forecast data is not guaranteed to be completely accurate.

## 5. Design Angle

One possible application is a road trip planning tool that uses weather information to help drivers choose when to travel. It could display temperature, precipitation, and wind conditions along a planned route.

One important UX consideration is that weather forecasts are not always accurate. The application should clearly show when the data was updated and avoid giving users the impression that predicted conditions are guaranteed.

## References

- Open-Meteo Documentation: https://open-meteo.com/en/docs
- Open-Meteo Terms: https://open-meteo.com/en/terms
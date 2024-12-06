import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "71cbcc4e209c6fa4bfb9977da897b884"

weather_params = {
    "lat":39.896519 ,
    "lon":32.861969,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring your umbrella!")







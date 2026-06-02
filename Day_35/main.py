import requests

MY_LAT = 49.248810
MY_LON = -122.980507
MY_API_KEY = "asdasdadadd"
weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an umbrella.")
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
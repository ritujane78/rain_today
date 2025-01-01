import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

MY_LATITUDE = 53.408371
MY_LONGITUDE = -2.991573

URL = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "cnt" : 4
}
response = requests.get(url=URL, params=params)
weather_data = response.json()
print(weather_data)

will_rain = False
for hourly_weather in weather_data['list']:
    id = hourly_weather["weather"][0]["id"]
    if id < 700:
        will_rain = True
        print(will_rain)
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+19013502446",
        to="+447795896284",
    )
    print(message.status)


import requests
from twilio.rest import Client
import api_keys


parameters = {
    "lat": "47.49",
    "lon": "14.59",
    # "q": "london",
    "appid": api_keys.API_KEY,
    "exclude": "currently,minutely,daily"
    

}

will_rain = False

response = requests.get(url=api_keys.OWM_ENDPOINT, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
hours_12_list = data["hourly"][:12]

weather_condition_id = [item["weather"][0]["id"] for item in hours_12_list]
for id in weather_condition_id:
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(api_keys.ACCOUNT_SID, api_keys.AUTH_TOKEN)
    message = client.messages.create(body="Bring umbrella dude", from_=api_keys.from_phone_no, to=api_keys.to_phone_no)
    print(message.status)
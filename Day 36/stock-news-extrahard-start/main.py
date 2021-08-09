import requests
from twilio.rest import Client
import api_keys

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"




parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": api_keys.api_key_alphavantage
}


response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
yesterday_closing_price = data["Time Series (Daily)"]["2021-07-16"]["4. close"]
day_before_closing_price = data["Time Series (Daily)"]["2021-07-15"]["4. close"]
print(yesterday_closing_price, day_before_closing_price)

diff = 100 - ((float(yesterday_closing_price) * 100) / float(day_before_closing_price))

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": api_keys.newsapi_api_key,
    "from": "2021-07-15",
    "to": "2021-07-16",
    "sources": "Bloomberg",

}
news_response = requests.get(url=NEWS_URL, params=news_parameters)
news_data = news_response.json()

client = Client(api_keys.ACCOUNT_SID, api_keys.AUTH_TOKEN)
if diff > 0:
    print(f"Went up by: {diff}")
    for x in range(3):
        headline = "Headline: " + news_data["articles"][x]["title"]
        brief = "Brief: " + news_data["articles"][x]["description"]
        message = client.messages.create(body=f"{COMPANY_NAME} 🔺{diff}\n{headline}\n{brief}", from_=api_keys.from_phone_no, to=api_keys.to_phone_no)

else:
    print(f"went down by: {diff}")
    for x in range(3):
        headline = "Headline: " + news_data["articles"][x]["title"]
        brief = "Brief: " + news_data["articles"][x]["description"]
        message = client.messages.create(body=f"{COMPANY_NAME} 🔻{diff}\n{headline}\n{brief}", from_=api_keys.from_phone_no, to=api_keys.to_phone_no)

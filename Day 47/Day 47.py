import requests
from bs4 import BeautifulSoup
import smtplib
import api_keys




url = "https://www.amazon.co.uk/Hatteker-Cordless-Detailing-Grooming-Waterproof/dp/B08DJ6TXZN/ref=sr_1_2_sspa?adgrpid=96081337831&dchild=1&gclid=EAIaIQobChMIzLulkvqL8gIVge7tCh33QwxvEAAYAyAAEgKZSvD_BwE&hvadid=415375167993&hvdev=c&hvlocphy=9045999&hvnetw=g&hvqmt=e&hvrand=12921833759510887064&hvtargid=kwd-794005579850&hydadcr=22610_1723281&keywords=mens+pubes+trimmer&qid=1627688046&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVhIQlBMQUg2WlVQJmVuY3J5cHRlZElkPUEwODc1ODg0MlBZVEdOVkoxQk5EMyZlbmNyeXB0ZWRBZElkPUEwMjA1MTgzMU1IWFBZSVlZWTlZVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept-Language": "en-GB,en;q=0.5"
}

response = requests.get(url=url, headers=headers)
target_web_page = response.text
soup = BeautifulSoup(target_web_page, "html.parser")

price_string = soup.find_all(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price = price_string[0].getText()
float_price = float(price.split("£")[1])




if float_price < 21:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=api_keys.my_email, password=api_keys.password)
        connection.sendmail(
        from_addr=api_keys.my_email,
        to_addrs=api_keys.my_email,
        msg=f"Subject:Price Update\n\nToday price is {float_price}"
        )
else:
    print("Price is not below 21")

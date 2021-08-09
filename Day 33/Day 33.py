import datetime
import smtplib
import time
import requests
import api_keys

MY_LAT = 51.53118881973776
MY_LONG = -0.08949588609011068
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(latitude, longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def is_nearby():
    if (MY_LAT - 5 <= float(latitude) <= MY_LAT + 5) and (MY_LONG - 5 <= float(longitude) <= MY_LONG + 5):
        return True
    else:
        return False


def is_night():
    now = datetime.datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True
    else:
        return False



while True:
    time.sleep(60)
    if is_nearby() and is_night():
        with smtplib.SMTP(host="smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=api_keys.my_email, password=api_keys.password)
            conn.sendmail(from_addr=api_keys.my_email, to_addrs=api_keys.my_email, msg="update \n\nis nearby")

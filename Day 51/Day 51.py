#====ISP UP/DOWN SPEED CHECK AND TWITTER COMPLAINT BOT====#
# from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from InternetSpeedTwitterBot import INTERNETSPEEDTWITTERBOT
import api_keys

PROMISED_DOWN_SPEED = 150
PROMISED_UP_SPEED = 150
EXECUTABLE_PATH = "/Users/danielghebrat/Documents/Python Bootcamp/python-100/Webdriver/geckodriver"


url = "https://www.speedtest.net/"
twt_url = "https://twitter.com/login"
twt_url_homepage = "https://twitter.com/home"


driver = INTERNETSPEEDTWITTERBOT(web_driver_path=EXECUTABLE_PATH)
driver.get_internet_speed(url=url)
driver.tweet_at_provider(uname=api_keys.twitter_username, passwrd=api_keys.twitter_password, twitter_url=twt_url, twt_url_home=twt_url_homepage)


# driver.close()


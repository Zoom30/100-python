from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

class INTERNETSPEEDTWITTERBOT:
    def __init__(self, web_driver_path):
        self.driver = webdriver.Firefox(executable_path=web_driver_path)
        self.down = 0.0
        self.up = 0.0


    def get_internet_speed(self, url):

        self.driver.get(url=url)
        try:
            speed_test_button = self.driver.find_element_by_css_selector(".start-text")
            speed_test_button.click()
        except ElementClickInterceptedException:
            print("exception caught")
            consent_button = self.driver.find_element_by_css_selector("#_evidon-banner-acceptbutton")
            consent_button.click()
        finally:
            speed_test_button.click()

        time.sleep(70)
        back_to_results = self.driver.find_element_by_css_selector(".desktop-app-prompt-modal > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > a:nth-child(1)")
        back_to_results.click()

        down_result = self.driver.find_element_by_css_selector(".download-speed")
        up_result = self.driver.find_element_by_css_selector(".upload-speed")
        self.down = float(down_result.text)
        self.up = float(up_result.text)

        


    def tweet_at_provider(self, twitter_url, uname, passwrd, twt_url_home):
        self.driver.get(url=twitter_url)
        time.sleep(4)
        username_textbox = self.driver.find_element_by_css_selector("div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        username_textbox.send_keys(uname)
        
        password_textbox = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        password_textbox.send_keys(passwrd)
        
        #login button
        click_button = self.driver.find_element_by_css_selector("div.css-18t94o4:nth-child(1)")
        click_button.click()

        self.driver.get(url=twt_url_home)

        time.sleep(10)
        tweet_box = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")
        tweet_box.send_keys(f"Hey CFL, here's my speed: UP {self.up} and DOWN {self.down}")
        
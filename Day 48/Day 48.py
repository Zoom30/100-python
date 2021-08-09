from selenium import webdriver
import urllib
from datetime import datetime
import re

webdriver_path = "{your path}/geckodriver"

driver = webdriver.Firefox(executable_path=webdriver_path)
# driver.get(url="https://www.jdsports.co.uk/search/men+blue+adidas/brand/adidas-originals,adidas/colour/blue/size/m/")


# price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul/li[15]/span/span[2]/div[1]/span")
# jd_search_name = driver.find_element_by_name("q")
# print(jd_search_name.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("logo-large")
# print(logo.size)


# link = driver.find_element_by_css_selector("#uspAll .maxWidth #usp1 a")
# print(link.get_attribute("href"))

#========================================================================================
#getting hold of upcoming events from python.org

now = datetime.now() #datatype of datetime.datetime
driver.get(url="https://www.python.org/")
scraped_dates = driver.find_elements_by_tag_name("time")

#1. get hold of the scraped dates and their "datetime" attribute
#2. use "re" to split
#3. use list slicing to remove the time
dates = [re.split("-|T|:",date.get_attribute("datetime"))[:3:] for date in scraped_dates] #list of 'str' dates
# print(now)
print(dates)
print(type(now.day))
future_dates = []
for date in dates:

    if int(date[2]) > now.day and int(date[1]) == now.month:
        future_dates.append(date)
    elif int(date[1]) > now.month:
        future_dates.append(date)
    elif int(date[0]) > now.year:
        future_dates.append(date)
    else:
         print(date, " is in the past")




#========================================================================================

# x = "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/"
# y = "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[5]/a"
# z = "/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[5]/a"


events = []
scarped_events = driver.find_elements_by_css_selector(".event-widget a")
for event in scarped_events:
    events.append(event.text)

events.remove(events[0])

event_with_dates = {}
print(f"""
These are the events {events}
and
These are the dates {future_dates}
""")
n = 0
for date in future_dates:
    event_with_dates[n]={"-".join(date): events[n]}
    n += 1


print(event_with_dates)
driver.quit()

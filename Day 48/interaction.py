from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
import time

webdriver_path = "{your path}/geckodriver"
driver = webdriver.Firefox(executable_path=webdriver_path)
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# articles_in_eng = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# all_portals = driver.find_element_by_link_text("All portals")
# search_bar = driver.find_element_by_css_selector("#searchInput")
# search_button = driver.find_element_by_css_selector("#searchButton")
# search_bar.send_keys("python")
# # To search, either...
# # search_button.click()
# # or...
# search_bar.send_keys(Keys.ENTER)

#============================================================================================

# username = "TestUN"
# last_name = "TestP"
# email = f"{username}.{last_name}@{last_name}.com"

# driver.get(url="http://secure-retreat-92358.herokuapp.com/")
# username_textbox = driver.find_element_by_name("fName")
# username_textbox.send_keys(username)
# last_name_textbox = driver.find_element_by_name("lName")
# last_name_textbox.send_keys(last_name)
# email_textbox = driver.find_element_by_name("email")
# email_textbox.send_keys(email)
# search_button = driver.find_element_by_css_selector(".btn")
# search_button.click()



#============================================================================================


driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
# cookie = driver.find_element_by_css_selector("#cookie")
# score = driver.find_element_by_css_selector("#money")

# cursor_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[1]/b")
# grandma_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/b")
# factory_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[3]/b")
# mine_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[4]/b")
# shipment_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[5]/b")
# alchemy_lab_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[6]/b")
# portal_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[7]/b")
# time_machine_score = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[8]/b")





# buy_cursor_button = driver.find_element_by_css_selector("#buyCursor")
# buy_grandma_button = driver.find_element_by_css_selector("#buyGrandma")
# buy_factory_button = driver.find_element_by_css_selector("#buyFactory")
# buy_mine_button = driver.find_element_by_css_selector("#buyMine")
# buy_shipment_button = driver.find_element_by_css_selector("#buyShipment")
# buy_alchemy_lab_button = driver.find_element_by_css_selector("#buyAlchemy\ lab")
# buy_portal_button = driver.find_element_by_css_selector("#buyPortal")
# buy_time_machine_button = driver.find_element_by_css_selector("#buyTime\ machine")

# buttons_to_click = [buy_cursor_button, buy_grandma_button, buy_factory_button, buy_mine_button, buy_shipment_button, buy_alchemy_lab_button, buy_portal_button, buy_time_machine_button]
# start_time = time.time()
# initial_time = time.time()
# timeout = time.time() + 5



# while True:
#     cookie.click()

#     if time.time() > timeout:
#         cursor_cost = int(cursor_score.text.split("-")[1])
#         grandma_cost = int(grandma_score.text.split("-")[1])
#         factory_cost = int(factory_score.text.split("-")[1])
#         mine_cost = int(mine_score.text.split("-")[1].replace(",", ""))
#         shipment_cost = int(shipment_score.text.split("-")[1].replace(",", ""))
#         alchemy_lab_cost = int(alchemy_lab_score.text.split("-")[1].replace(",", ""))
#         portal_cost = int(portal_score.text.split("-")[1].replace(",", ""))
#         time_machine_cost = int(time_machine_score.text.split("-")[1].replace(",", ""))
#         item_to_buy = [cursor_cost, grandma_cost, factory_cost, mine_cost, shipment_cost, alchemy_lab_cost, portal_cost, time_machine_cost]


#         cookie_upgrades = {}
#         for n in range(len(item_to_buy)):
#             cookie_upgrades[item_to_buy[n]] = 
#             pass
        
#     current_score = int(score.text)
#     re = current_score
    
#     if time.time() - start_time >= 5:
#         print("it's been 5 seconds")
        
#         for item in item_to_buy:
#             re = current_score - item
#             print(f"re is now {current_score} - {item} = {re}")
#             if re <= 0:
#                 # print(f"bought item for {item_to_buy[item_to_buy.index(item) - 1]}")
#                 if item_to_buy.index(item) == 0:
#                     buttons_to_click[item_to_buy.index(item)].click()
#                 else:
#                     try:
#                         buttons_to_click[item_to_buy.index(item) - 1].click()
#                     except StaleElementReferenceException:
#                         print("not available yet")

                    
            
#         start_time = time.time()
    
#     if time.time() - initial_time >= 300:
#         print(score.text)
#         break



#=====================ANGELA'S METHOD========================#

cookie = driver.find_element_by_id("cookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

# driver.close()
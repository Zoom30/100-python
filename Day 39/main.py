import requests
import twilio
import api_keys


# TEQUILA_URL = "https://tequila-api.kiwi.com/locations/query"
HOME_TOWN_IATACODE = "LON"


# Reading from google sheets and updating iata codes
sheety_city_get_url = "https://api.sheety.co/dd81a891f83891fcffdab1dcc7c5a53e/flightDeals/prices"


city_response = requests.get(url=sheety_city_get_url, headers=api_keys.heety_headers)
city_data = city_response.json()
list_of_cities = [item["city"] for item in city_data["prices"]]


# Fetching IATA codes and updating google sheets
kiwi_headers = {
    "apikey": api_keys.TEQUILA_API_KEY
}

for city in list_of_cities:
    kiwi_params = {
    "term": city
    }
    kiwi_response = requests.get(url=api_keys.TEQUILA_URL, headers=kiwi_headers, params=kiwi_params)
    kiwi_data = kiwi_response.json()
    city_code = kiwi_data["locations"][0]["code"]
    
    body = {
        "price":{
                "iataCode": city_code
                }
            }
            
    city_iata_response = requests.put(url=f"{sheety_city_get_url}/{list_of_cities.index(city) + 2}", json=body, headers=api_keys.sheety_headers)


# checking flights from HOME_TOWN_IATACODE to destination IATACODES






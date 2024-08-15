#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. 
# Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

# The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.



# ------------------------------------API's------------------------------------

# Google Sheet Data Management - https://sheety.co/

# Amadeus Flight Search API (Free Signup, Credit Card not required) - https://developers.amadeus.com/

# Amadeus Flight Offer Docs - https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference

# Amadeus How to work with API keys and tokens guide - https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335

# Amadeus Search for Airport Codes by City name - https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference

# Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python


# -----------------------------------------------------------------------------


import os
import requests
from dotenv import load_dotenv
import json
load_dotenv()

# -----------------ENVS--------------------
A_API_KEY = os.getenv("A_API_KEY")
A_API_SECRET = os.getenv('A_API_SECRET')

SHEETLY_API_ENPOINT = "https://api.sheety.co/f378ff5e745942b1075afca807afb7b8/flightDeals/prices"
AMADEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_GET_IATA_ENDPOINT = "https://test.api.amadeus.com/v1/refrence-data/locations/cities"

def get_token():
    payload = {
        "grant_type" : "client_credentials",
        "client_id" : A_API_KEY,
        "client_secret" : A_API_SECRET
    }
    token_response = requests.post(AMADEUS_TOKEN_ENDPOINT, data=payload)
    token_response.raise_for_status()
    data = json.loads(token_response.text)
    return data['access_token']


def get_iata_code(): 
    payload= {
        "keyword" : 'paris'
    }
    city_response = requests.get(f"{AMADEUS_GET_IATA_ENDPOINT}?countryCode=FR&keyword=PARIS&max=10")
    city_response.raise_for_status()
    print(city_response.text)

token_finder = get_token()

get_iata_code()

# get_sheetly_shit = requests.get(SHEETLY_API_ENPOINT)
# get_sheetly_shit.raise_for_status()
# print(get_sheetly_shit.text)





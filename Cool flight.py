import time
import json
import requests
import webbrowser
import colorama
from tkinter import messagebox
from colorama import Fore
from colorama import Back


colorama.init(autoreset=True)
Flight_ICAO = input(f"{Fore.RED}What ICAO?\n: ")
try:
    response = requests.get(f"https://airlabs.co/api/v9/flights?api_key=19d63b03-421b-408e-925a-d50a54bc6b8a&flight_icao={Flight_ICAO}")
    response = json.loads(response.text)
    lat = response["response"][0]["lat"]
    lng = response["response"][0]["lng"]
    speed = response["response"][0]["speed"] / 1.8
    url = f"https://www.latlong.net/c/?lat={lat}&long={lng}"
    print(f"{Fore.GREEN}{url}")
    print(f"{Fore.CYAN}{Back.BLUE}{speed} Knots")
    uri = "https://trueway-geocoding.p.rapidapi.com/ReverseGeocode"
    querystring = {"location":f"{lat},{lng}","language":"en"}
    headers = {
    	"X-RapidAPI-Key": "4433f63431msh8d98becb55a842bp11ddb2jsn71a03c7f28d2",
    	"X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
    }
    response = requests.request("GET", uri, headers=headers, params=querystring)
    print(f'{Fore.BLUE}Address: {response.json()["results"][0]["address"]}')
    time.sleep(5)
    webbrowser.open(url)
except:
    messagebox.showerror("Cool Flight", "Task failed successfully.")

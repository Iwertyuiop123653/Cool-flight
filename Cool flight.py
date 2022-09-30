import time
import config
import webbrowser
import requests
import json
import colorama
from colorama import Fore
from colorama import Back
colorama.init(autoreset=True)
Flight_ICAO = input(f"{Fore.RED}What ICAO?\n: ")
try:
    response = requests.get(f"https://airlabs.co/api/v9/flights?api_key={config.api_key}&flight_icao={Flight_ICAO}")
    response = json.loads(response.text)
    lat = response["response"][0]["lat"]
    lng = response["response"][0]["lng"]
    speed = response["response"][0]["speed"] / 1.8
    url = f"https://www.latlong.net/c/?lat={lat}&long={lng}"
    print(f"{Fore.GREEN}{url}")
    print(f"{Fore.CYAN}{Back.BLUE}{speed} Knots")
    time.sleep(3)
    webbrowser.open(url)
except:
    print(f"{Fore.RED}Mission Failed We'll get em next time")
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GREYNOISE_API_KEY")

def check_greynoise(ip):
    gn_url = f"https://api.greynoise.io/v3/community/{ip}"
    headers = {"key": API_KEY}
    response = requests.get(gn_url, headers=headers)
    return response.json()

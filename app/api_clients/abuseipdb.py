import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")
def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {'ipAddress': ip, 'maxAgeInDays': 30}
    headers = {'Key': API_KEY, 'Accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

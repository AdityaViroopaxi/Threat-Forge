import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def check_virustotal(ioc, ioc_type):
    vt_base = "https://www.virustotal.com/api/v3/"
    headers = {"x-apikey": API_KEY}
    # Choose endpoint based on IOC type
    if ioc_type == "IP":
        url = vt_base + f"ip_addresses/{ioc}"
    elif ioc_type == "domain":
        url = vt_base + f"domains/{ioc}"
    elif ioc_type == "url":
        # VT needs URL-safe base64 of the URL (simplified example)
        from base64 import urlsafe_b64encode
        encoded = urlsafe_b64encode(ioc.encode()).decode().strip("=")
        url = vt_base + f"urls/{encoded}"
    elif ioc_type == "hash":
        url = vt_base + f"files/{ioc}"
    else:
        return {"error": "Unsupported IOC type"}
    response = requests.get(url, headers=headers)
    return response.json()

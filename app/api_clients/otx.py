import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OTX_API_KEY")

def check_otx(ioc, ioc_type):
    otx_base = "https://otx.alienvault.com/api/v1/indicators/"
    headers = {"X-OTX-API-KEY": API_KEY}
    if ioc_type == "IP":
        url = otx_base + f"IPv4/{ioc}/general"
    elif ioc_type == "domain":
        url = otx_base + f"domain/{ioc}/general"
    elif ioc_type == "url":
        url = otx_base + f"url/{ioc}/general"
    elif ioc_type == "hash":
        url = otx_base + f"file/{ioc}/general"
    else:
        return {"error": "Unsupported IOC type"}
    response = requests.get(url, headers=headers)
    return response.json()

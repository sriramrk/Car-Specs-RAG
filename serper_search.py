# serper_search.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search_car_online(query, location):
    if not SERPER_API_KEY:
        raise ValueError("Missing SERPER_API_KEY environment variable.")

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "q": f"{query} for sale near {location} site:cargurus.com OR site:autotrader.com OR site:cars.com",
        "gl": "us",
        "hl": "en",
        "num": 10
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("organic", []):
            title = item.get("title", "").lower()
            link = item.get("link", "")
            if any(x in title for x in ["for sale", "buy", "deal", "listing", "price", "used", "new"]):
                if link:
                    results.append((item.get("title", "Listing"), link))

        return results[:5]

    except requests.exceptions.HTTPError as err:
        print("[Serper ERROR] HTTP error:", err)
        return []
    except Exception as e:
        print("[Serper ERROR] General exception:", e)
        return []

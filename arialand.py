import requests
import time
import random

# URL and headers
url = 'https://ariagames.io/aria_kombat_api_update/tap_reward?user_id=5826259925'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Basic dGVzdF9hZG1pbjpqdHRJWHJoUU1DdWpvcUR1Q3Vo',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://ariagames.io',
    'Referer': 'https://ariagames.io/aria_kombat/aria_kombat?tgWebAppStartParam=referral_1401873571',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"'
}

# Data payload
data = {
    "user_id": "5826259925"
}

# Infinite loop with random delay
while True:
    try:
        response = requests.put(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Random delay between 0.2 and 0.8 seconds
    time.sleep(random.uniform(0.002, 0.008))
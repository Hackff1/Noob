import requests
import random
import time

def generate_random_chat_instance():
    """Generate a random chat_instance as a large numeric string."""
    return str(random.randint(10**18, 10**19 - 1))

def fetch_ads():
    """Fetch ads and handle the response."""
    url = 'https://api.adsgram.ai/adv'
    params = {
        'blockId': '4853',
        'tg_id': '7302925429',
        'tg_platform': 'ios',
        'platform': 'Linux armv81',
        'language': 'en',
        'chat_type': 'sender',
        'chat_instance': generate_random_chat_instance(),
        'top_domain': 'app.notpx.app'
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://app.notpx.app',
        'Referer': 'https://app.notpx.app/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }

    # Send the initial request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()

            # Extract the 'reward' URL from the 'trackings' array
            trackings = data.get('banner', {}).get('trackings', [])
            reward_url = None
            for tracking in trackings:
                if tracking.get('name') == 'reward':
                    reward_url = tracking.get('value')
                    break

            if reward_url:
                # Make the follow-up request to the reward URL
                reward_response = requests.get(reward_url)
                print("Reward URL Status Code:", reward_response.status_code)
                print("Reward URL Response Body:", reward_response.text)
            else:
                print("Reward URL not found in the response.")
        except ValueError:
            print("Failed to parse JSON response.")
    else:
        print(f"Initial request failed with status code {response.status_code}")
        print(response.text)

# Infinite loop with a 25-second delay
while True:
    fetch_ads()
    print("Waiting for 25 seconds before the next request...")
    time.sleep(25)

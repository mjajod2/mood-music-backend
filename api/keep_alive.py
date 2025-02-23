import requests
import time

API_URL = "https://mood-music-api.onrender.com"  # Replace with your API URL

def keep_api_alive():
    while True:
        try:
            response = requests.get(API_URL)
            print(f"Pinged API: {response.status_code} - {response.text[:50]}")
        except requests.exceptions.RequestException as e:
            print(f"Error pinging API: {e}")
        
        time.sleep(300)  # Wait 5 minutes (300 seconds)

if __name__ == "__main__":
    keep_api_alive()

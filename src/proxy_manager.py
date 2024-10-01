import os
import requests
import logging

class ProxyManager:
    def __init__(self):
        self.api_key = os.getenv("PROXYFLY_API_KEY")
        self.proxy_url = "https://api.proxifly.dev/get_proxy"  # Replace with the actual API endpoint from Proxifly

    def get_proxies(self):
        logging.info("Fetching proxies from Proxifly API...")
        
        try:
            response = requests.get(self.proxy_url, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raise an error for bad responses

            proxies = response.json()  # Assuming the response is in JSON format
            if not proxies:
                logging.warning("No proxies received from Proxifly.")
                return []

            logging.info(f"Retrieved {len(proxies)} proxies.")
            return proxies  # Adjust as needed to return the format you want

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching proxies: {e}")
            return []


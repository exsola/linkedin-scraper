from src.linkedin_login import LinkedInLogin
from src.search_scraper import SearchScraper
from src.proxy_manager import ProxyManager
from src.utils import configure_logging
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    configure_logging()

    # Set up proxy manager and fetch proxies
    proxy_manager = ProxyManager()
    proxies = proxy_manager.get_proxies()
    
    # Choose a proxy from the list (implement your logic here)
    chosen_proxy = proxies[0] if proxies else None  # Modify as needed

    # Log into LinkedIn
    linkedin_login = LinkedInLogin()
    driver = linkedin_login.login(chosen_proxy)  # Modify login to accept a proxy if necessary

    # Perform a search and scrape profiles
    search_query = os.getenv("SEARCH_QUERY")
    search_scraper = SearchScraper(driver)
    search_scraper.search(search_query)

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()






from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
from src.profile_scraper import ProfileScraper

class SearchScraper:
    def __init__(self, driver):
        self.driver = driver
        self.profile_scraper = ProfileScraper()

    def search(self, query):
        logging.info(f"Searching LinkedIn for: {query}")
        search_box = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
        search_box.clear()
        search_box.send_keys(query + Keys.RETURN)

        time.sleep(2)  # Wait for the search results to load
        self.scrape_search_results()

    def scrape_search_results(self):
        time.sleep(3)  # Wait for search results to load

        # Retrieve search result elements
        results = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-control-name="search_srp_result"]')

        for result in results:
            profile_url = result.get_attribute('href')
            logging.info(f"Found profile URL: {profile_url}")
            profile_data = self.profile_scraper.scrape_profile(self.driver, profile_url)

            # Process the scraped data (e.g., save to a file or database)
            self.process_profile_data(profile_data)

    def process_profile_data(self, profile_data):
        # For simplicity, we print the profile data; you can customize this to save it
        logging.info(f"Profile data: {profile_data}")

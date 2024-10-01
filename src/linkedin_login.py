import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LinkedInLogin:
    def __init__(self):
        self.username = os.getenv("LINKEDIN_USERNAME")
        self.password = os.getenv("LINKEDIN_PASSWORD")

    def login(self, proxy=None):
        options = uc.ChromeOptions()
        if proxy:
           # Use the proxy for the WebDriver
             options.add_argument(f'--proxy-server={proxy}')  # Adjust the format if needed


        # options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = uc.Chrome(options=options)
        driver.get("https://www.linkedin.com/login")

        time.sleep(2)  # Wait for the page to load
        logging.info("Logging in to LinkedIn...")

        driver.find_element(By.ID, "username").send_keys(self.username)
        driver.find_element(By.ID, "password").send_keys(self.password)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        time.sleep(2)  # Wait for the dashboard to load
        logging.info("Successfully logged in.")

        return driver



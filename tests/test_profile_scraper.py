import unittest
from unittest.mock import MagicMock
from src.profile_scraper import ProfileScraper

class TestProfileScraper(unittest.TestCase):
    def test_scrape_profile(self):
        mock_driver = MagicMock()
        mock_driver.get.return_value = None
        
        scraper = ProfileScraper()
        mock_driver.find_element.return_value.text = "John Doe"

        profile_data = scraper.scrape_profile(mock_driver, "https://www.linkedin.com/in/example/")
        
        self.assertEqual(profile_data['name'], "John Doe")
        mock_driver.get.assert_called_with("https://www.linkedin.com/in/example/")

if __name__ == '__main__':
    unittest.main()

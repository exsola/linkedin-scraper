import unittest
from unittest.mock import patch, MagicMock
from src.scraper import main

class TestScraper(unittest.TestCase):
    @patch('src.linkedin_login.LinkedInLogin')
    @patch('src.profile_scraper.ProfileScraper')
    def test_main(self, MockProfileScraper, MockLinkedInLogin):
        mock_driver = MagicMock()
        mock_login_instance = MockLinkedInLogin.return_value
        mock_login_instance.login.return_value = mock_driver

        mock_profile_instance = MockProfileScraper.return_value
        mock_profile_instance.scrape_profile.return_value = {'name': 'John Doe'}

        # Run the main function
        main()

        # Assert that login was called
        MockLinkedInLogin.assert_called_once()
        mock_login_instance.login.assert_called_once()
        mock_profile_instance.scrape_profile.assert_called_once_with(mock_driver, "https://www.linkedin.com/in/example/")
        mock_driver.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()


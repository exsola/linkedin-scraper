import unittest
from unittest.mock import patch, MagicMock
from src.linkedin_login import LinkedInLogin

class TestLinkedInLogin(unittest.TestCase):
    @patch('src.linkedin_login.webdriver.Chrome')
    def test_login_success(self, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        login = LinkedInLogin("username", "password")
        driver = login.login()

        # Verify that the driver is the mocked driver
        self.assertEqual(driver, mock_driver)
        mock_driver.get.assert_called_with("https://www.linkedin.com/login")
        self.assertTrue(mock_driver.find_element.called)

if __name__ == '__main__':
    unittest.main()

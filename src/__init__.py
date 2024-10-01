"""
src/__init__.py

This file initializes the src package, handles core configuration, 
and allows for easier imports across the package.
"""

# Importing the primary components of the scraper for easy access
from .scraper import run_scraper
from .linkedin_login import login_linkedin
from .profile_scraper import scrape_profile
from .proxy_manager import init_browser_with_proxy
from .config import SCRAPER_CONFIG

# Package version (useful for tracking builds)
__version__ = "1.0.0"

# Define a list of all submodules to expose on `from src import *`
__all__ = [
    "run_scraper",
    "login_linkedin",
    "scrape_profile",
    "init_browser_with_proxy",
    "SCRAPER_CONFIG"
]

# Global configuration settings can also be initialized here if necessary.

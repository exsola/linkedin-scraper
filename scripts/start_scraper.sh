#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print the current directory
echo "Current directory: $(pwd)"

# Build and start the Docker containers
echo "Starting the LinkedIn scraper using Docker Compose..."
docker-compose up --build

echo "Scraping completed. Check the 'data' and 'logs' directories for output."

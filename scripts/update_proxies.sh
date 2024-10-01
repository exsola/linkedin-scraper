#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the proxy source URL (you can change this to your preferred source)
PROXY_SOURCE="${PROXY_LIST_URL}"

# Define the file where the proxies will be saved
PROXY_FILE="data/proxies.txt"

# Print current action
echo "Fetching new proxy list from $PROXY_SOURCE..."

# Fetch the proxy list and save it to the proxy file
curl -s $PROXY_SOURCE -o $PROXY_FILE

# Check if the proxy file is empty
if [[ ! -s $PROXY_FILE ]]; then
    echo "Failed to fetch proxies. The proxy file is empty."
    exit 1
fi

# Print success message
echo "Proxies updated successfully! Saved to $PROXY_FILE."

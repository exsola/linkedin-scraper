# Use a base image with Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src

# Copy other necessary files
COPY .env ./

# Command to run the scraper
CMD ["python", "src/scraper.py"]

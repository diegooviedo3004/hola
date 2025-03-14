# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (used by TikTokApi for scraping)
RUN playwright install chromium

# Copy the application code into the container
COPY . .

# Expose the port your API will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

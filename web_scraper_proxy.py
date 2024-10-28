#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import ipaddress

# URL of the website to scrape
url = 'https://free-proxy-list.net/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the rows containing the port, IP address, and type
rows = soup.find_all('tr')

# Function to check if an IP address is valid
def is_valid_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

# Counter variable to limit the output to 30 lines
count = 0

# Iterate over the rows and extract the desired data
for row in rows:
    # Find the cells in each row
    cells = row.find_all('td')
    
    if len(cells) >= 3:
        # Extract the port, IP address, and type
        ip_address = cells[0].text.strip()
        port = cells[1].text.strip()
        port_type = cells[2].text.strip()
        if port == "80" or port == "8080" or port == "8000" or port == "5000" or port == "8888" or port == "3000" or port == "9090" or port == "3123":
            port_type = "http"
        elif port == "443" or port == "8443" or port == "4433" or port == "9443" or port == "10443":
            port_type = "https"
        elif port == "1080":
            port_type = "socks4"
        # Check if the IP address is valid
        if is_valid_ip(ip_address):
                if port_type == "http" or port_type == "https" or port_type == "socks4":
                        count += 1
                        with open("copy.txt", "a") as output:
                                output.write(f"{port_type} {ip_address} {port}\n")
                        # Limit the output to 30 lines
                        if count >= 5:
                                break
def remove_duplicate_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    unique_lines = set(lines)

    with open(file_path, 'w') as file:
        for line in unique_lines:
            file.write(line)

# Usage
remove_duplicate_lines('copy.txt')  # Removes duplicate lines from 'copy.txt'

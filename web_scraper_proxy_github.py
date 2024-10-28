#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
# URL of the website to scrape
url = 'https://github.com/proxifly/free-proxy-list/blob/main/proxies/all/data.csv#L3'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

def find_socks5_lines(soup):
    text_content = soup.get_text()  
    for line in text_content.split('\n'):
        if 'socks5' in line.lower():
            print(line.strip())


# Sample text containing IP addresses and ports
# Regular expression to find socks5 and socks4 entries
pattern = r'(socks[45]://(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}))'
matches = re.findall(pattern, soup.text)

# Structure to store results
results = []

# Process the matches
for match in matches:
    protocol = match[0]  # Full match (e.g., socks5://...)
    ip_address = match[1]  # Extracted IP address
    port = match[2]  # Extracted port number
    results.append({
        'type': protocol.split('://')[0],  # 'socks5' or 'socks4'
        'ip': ip_address,
        'port': port
    })
count_1 = 0

for result in results:
    with open("copy.txt", "a") as output:
        output.write(f"\n{result['type']} {result['ip']} {result['port']}")
    count_1 += 1
    if count_1 == 10:
        break

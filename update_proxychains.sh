#!/bin/bash

./web_scraper_proxy.py

./web_scraper_proxy_github.py

./validion_copy.py 

# Path to your proxy list
PROXY_LIST="/home/haim/Desktop/copy.txt"

# Path to the ProxyChains configuration file
PROXYCHAINS_CONF="/etc/proxychains4.conf"

# Backup the original configuration file with sudo
#sudo cp $PROXYCHAINS_CONF ${PROXYCHAINS_CONF}.bak
#touch temp.txt
# Create the new ProxyList section with dynamic chain
{
    cat copy.txt
}
sudo mv copy.txt /etc/proxychains4.conf
#rm -r temp.txt
echo "ProxyChains configuration updated with dynamic chaining and proxies from $PROXY_LIST."
proxychains firefox


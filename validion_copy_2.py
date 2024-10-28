#!/bin/python

import re

def format_proxy_file(filename):
    # Template header as a single string for easy comparison
    template_header = [
        "#ProxyChains configuration file",
        "round_robin_chain",
        "remote_dns_subnet 224",
        "tcp_read_time_out 15000",
        "tcp_connect_time_out 8000",
        "[ProxyList]"
    ]
    
    try:
        # Read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Split content into lines and remove empty lines
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Create the header block string for comparison
        header_block = '\n'.join(template_header)
        
        # Replace all occurrences of the header block with a single occurrence
        content = '\n'.join(lines)
        content = content.replace(header_block + '\n' + header_block, header_block)
        
        # Split the content again to process proxy lines
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Collect unique proxy lines
        proxy_lines = set()
        for line in lines:
            if line not in template_header:  # Skip header lines
                ip_port_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\s+\d{1,5}\b', line)
                if ip_port_match:
                    ip_port = ip_port_match.group(0)
                    ip, port = ip_port.split()
                    proxy_lines.add(f"socks5 {ip} {port}")
        
        # Create final content
        final_content = template_header + sorted(list(proxy_lines))
        
        # Write the formatted content back to the file
        with open(filename, 'w') as file:
            file.write('\n'.join(final_content) + '\n')
            
        print("File has been successfully formatted with duplicate headers removed!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def remove_duplicate_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove duplicates by converting the list to a set, then back to a list
        unique_lines = list(set(lines))

        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        print("Duplicate lines removed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    remove_duplicate_lines('copy.txt')
    format_proxy_file('copy.txt')


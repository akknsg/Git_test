import netmiko
from netmiko import ConnectHandler
from cyberark.identity import CyberArkIdentity
import io
import os
import sys
import logging

# Open the file in read mode
with open('Device_IP_Details.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Get a specific line (e.g., line 3, index starts from 0)
line_number = 2  # Adjust to the line you want
if line_number < len(lines):
    selected_line = lines[line_number]
    print(f"The selected line is: {selected_line.strip()}")
else:
    print("The specified line number is out of range.")


# Example usage of Netmiko to connect to a network device
# Retrieve credentials from CyberArk
cyberark = CyberArkIdentity(
    tenant_url="https://your-tenant-url.cyberark.com",
    app_id="your-app-id",
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# Fetch the username and password
credentials = cyberark.get_credentials("safe_name", "object_name")
device['username'] = credentials['username']
device['password'] = credentials['password']
# Define the device details
device = {
    'device_type': 'cisco_ios',  # Change this based on your device type
    'host': '192.168.1.1',       # Replace with the device's IP address
    'username': 'admin',         # Replace with your username
    'password': 'password',      # Replace with your password
    'secret': 'enable_password', # Replace with your enable password if needed
}

# Establish a connection to the device
try:
    connection = ConnectHandler(**device)
    connection.enable()  # Enter enable mode if required

    # Send a command and capture the output
    output = connection.send_command('show ip interface brief')
    print(output)

    # Close the connection
    connection.disconnect()
except Exception as e:
    print(f"An error occurred: {e}")
    log_file = '/home/master/python_projects/error_log.txt'
    with io.open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"An error occurred: {e}\n")
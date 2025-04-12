import json
from netmiko import ConnectHandler

# Load the JSON file
with open("JSON_Format_IP.txt", "r") as file:
    devices = json.load(file)

# Loop through each device and connect
for device in devices:
    try:
        print(f"Connecting to {device['host']}...")
        connection = ConnectHandler(**device)  # Establish SSH connection
        connection.enable()  # Enter enable mode (if required)

        # Execute a command
        output = connection.send_command("show ip interface brief")
        print(output)

        connection.disconnect()  # Close the connection
    except Exception as e:
        print(f"Failed to connect to {device['host']}: {e}")
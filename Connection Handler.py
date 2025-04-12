from netmiko import ConnectHandler
import json

# Open and read the file containing devices
with open('JSON_Format_IP.txt', 'r') as file:
    devices = [json.loads(line.strip()) for line in file]

# Iterate over each device and connect
for device in devices:
    try:
        print(f"Connecting to {device['host']}...")
        connection = ConnectHandler(**device)
        # Example command execution
        output = connection.send_command("show ip interface brief")
        print(f"Output from {device['host']}:\n{output}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['host']}: {e}")
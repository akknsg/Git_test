import os

# Set the desired path under /tmp/
path = "/tmp/Device_folder"

# Create the directory
try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully!")
except PermissionError:
    print(f"Permission denied: Unable to create directory '{path}'")
except Exception as e:
    print(f"An error occurred: {e}")
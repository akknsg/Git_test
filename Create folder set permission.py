import os
import stat

# Set the desired path under /tmp/
path = "/tmp/Device_folder"
# Check if the path is a directory

try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully!")
except PermissionError:
    print(f"Permission denied: Unable to create directory '{path}'")
except Exception as e:
    print(f"An error occurred: {e}")
    # Create a file under the directory
file_name = "Host_file.txt"
file_path = os.path.join(path, file_name)

try:
    with open(file_path, "w") as file:
        file.write("This is an Host file.")
        print(f"File '{file_path}' created successfully!")
except PermissionError:
    print(f"Permission denied: Unable to create file '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")


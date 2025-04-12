import os
import stat

# Specify the existing folder path
folder_path = "/tmp/Device_folder"

# Create the file path by combining the folder path and file name
file_path = os.path.join(folder_path, "Devices_file.txt")

# Specify the filename
file_name = "Devices_file.txt"
# Create and open the file in write mode ('w')
with open(file_name, 'w') as file:
    # Write some content to the file (optional)
    file.write("This is a sample text file.\nYou can add more lines here.")

print(f"File '{file_name}' has been created successfully!")
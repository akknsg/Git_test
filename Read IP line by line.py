# Open the file in read mode
#with open('Device_IP_Details.txt', 'r') as file:
    # Loop through each line in the file
try:
    with open('/home/master/python_projects/Device_IP_Details.txt', 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Print each line after stripping leading/trailing whitespace
            print(line.strip())
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
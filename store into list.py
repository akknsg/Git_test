# Initialize an empty list to store lines
lines_list = []
# Open the file in read mode
with open('/home/master/python_projects/Device_IP_Details.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Add each line (after stripping whitespace) to the list
        lines_list.append(line.strip())

# Print the resulting list
print("Stored Lines:", lines_list)
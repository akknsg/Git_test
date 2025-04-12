lists = []  # List to store separate lists for each line

with open("/home/master/python_projects/Device_IP_Details.txt", "r") as file:
    for line in file:
        # Strip whitespace and split the line into a list of words
        line_list = line.strip()  # Split by comma
        lists.append(line_list)  # Add the list to the main list

# Print the separate lists
for i, single_list in enumerate(lists, start=1):
    print(f"IP {i}: {single_list}")
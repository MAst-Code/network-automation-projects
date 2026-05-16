# Disclaimer - Device.txt has fake credentials
# Project: Process devices.txt inventory file
# Goal:
# Read each device entry from the file and convert it into a nested list structure.
#
# Each line in the file becomes its own list.
# Each value within the line is split by ':' into separate list elements.

# with open('devices.txt') as f:
#     f.readline()
#     content = f.readline().strip().split(':')
#     devices_list = []
#     devices_list.append(content)
#     content = f.readline().strip().split(':')
#     devices_list.append(content)
#     content = f.readline().strip().split(':')
#     devices_list.append(content)
#     content = f.readline().strip().split(':')
#     devices_list.append(content)
#     content = f.readline().strip().split(':')
#     devices_list.append(content)
#     print(devices_list)

# this code above does achieve this goal but the code is very repetitve 
# Initially, I didnt realise that for loops iterate line by line for a file type
# I thought it did it character by character, changing the script to use a for loop\
# My code

with open('devices.txt') as f:                # open file devices.txt in read only mode
    f.readline()                              # Skip the first line of the file

    devices_list = []                         # variable to place our device content in

    for line in f:                            # iterate through each line of the file
        content = line.strip().split(':')     # Remove whitespace and split values by ':' in the string
        devices_list.append(content)          # Add the now list data into devices_list

    print(devices_list)                       # Print nested lists of device attributes

    for device in devices_list:               # Print the IP address of each device
        print(f'Pinging {device[1]}')


# Instructor code

with open('devices.txt') as f:
    content = f.read().splitlines()
    # print(content)
    devices = list()
    for line in content[1:]:
        devices.append(line.split(':'))

    print(devices)

    for device in devices:
        print(f'Pinging {device[1]}')

    


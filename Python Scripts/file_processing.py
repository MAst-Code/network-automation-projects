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

with open('devices.txt') as f:
    f.readline()

    devices_list = []

    for line in f:
        content = line.strip().split(':')
        devices_list.append(content)
print(devices_list)

# Instructor code

with open('devices.txt') as f:
    content = f.read().splitlines()
    # print(content)
    device = list()
    for line in content[1:]:
        device.append(line.split(':'))
print(device)


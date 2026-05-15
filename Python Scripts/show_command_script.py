from netmiko import ConnectHandler
import time
from rich.progress import track

router = {
    "device_type": "cisco_ios",
    "host": "Placeholder IP",
    "username": "Placeholder",
    "password": "Placeholder",
}

# Connect to device
connection = ConnectHandler(**router)


print(f'Connecting to {router['host']}')
for step in track(range(10), description="Connecting..."):
    time.sleep(0.2)

# Enter enable mode
# connection.enable()

# Run command
output = connection.send_command("show ip int br")

# Print output
print(output)

# Disconnect session
connection.disconnect()
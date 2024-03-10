import subprocess
import time

# Function to uninstall drivers using PnPUtil
def uninstall_drivers():
    subprocess.run('PnPUtil /remove-device *')

# Main loop
while True:
    try:
        uninstall_drivers()
        time.sleep(1)  # Wait for 1 second before uninstalling the next driver
    except Exception as e:
        print(f"Error occurred: {e}")
        break

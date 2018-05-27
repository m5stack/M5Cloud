# This file is executed on every boot (including wake-boot from deepsleep)

import sys

# Set default path
# Needed for importing modules and upip
sys.path[1] = '/flash/lib'


# Start WiFi auto connect config
import wifisetup
wifisetup.start()

# Start M5Cloud Client
import m5cloud
m5cloud.run()

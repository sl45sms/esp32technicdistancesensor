# On LMS-ESP32 (MicroPython)
# ESP32 MicroPython Sketch for Emulating Technic/SPIKE Color Sensor
# this is a random color sensor example that simulates a sensor sending random color values to the hub.
# tested on LMS-ESP32v2 board with powered up hub (train hub)
from pupremote import PUPRemoteSensor
import time
import random

# Assuming sensor ID 61 is used for the color sensor
TECHNIC_COLOR_SENSOR_ID = 61

# If using Pybricks on the hub, max_packet_size=16 is essential.
p_sensor = PUPRemoteSensor(sensor_id=TECHNIC_COLOR_SENSOR_ID, max_packet_size=16)

def single_byte_data():
    # Simulate reading a single byte value
    return random.randint(0, 10)

# 'B' means it will send one unsigned byte (1 byte) to the hub.
p_sensor.add_channel('data_stream_color', to_hub_fmt='B') 

while True:
    # For the channel, update its value periodically
    p_sensor.update_channel('data_stream_color', single_byte_data())

    p_sensor.process() # Handle LPF2 communication
    time.sleep_ms(100) # Update rate for the channel
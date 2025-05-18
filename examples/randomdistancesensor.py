# ESP32 MicroPython Sketch for Emulating Technic/SPIKE Distance Sensor

from pupremote import PUPRemoteSensor
import time
import random

# LEGO Technic/SPIKE Prime Distance Sensor Device ID
TECHNIC_DISTANCE_SENSOR_ID = 62  # Hex: 0x3E

# Initialize PUPRemoteSensor
# If your LEGO hub is running Pybricks firmware, max_packet_size=16 is crucial.
# For official LEGO firmware on hubs like SPIKE Prime or Robot Inventor,
# the default packet size might be acceptable, but 16 is safer for broader compatibility.
esp32_as_sensor = PUPRemoteSensor(sensor_id=TECHNIC_DISTANCE_SENSOR_ID, max_packet_size=16)

# function to return a random distance value in mm
# This simulates the behavior of a real distance sensor.
def distance_mm():
    return random.randint(50, 2000)

print(f"ESP32 emulating Technic Distance Sensor (ID: {TECHNIC_DISTANCE_SENSOR_ID})")
print("Providing distance in millimeters (LPF2 Mode 0, format 'H').")
esp32_as_sensor.add_channel('data_stream_distance', to_hub_fmt='H')

while True:
    # Simulate a distance reading
    esp32_as_sensor.update_channel('data_stream_distance', distance_mm())
    # This method processes incoming LPF2 requests from the hub
    esp32_as_sensor.process()
    time.sleep_ms(50) # Main loop delay, affects responsiveness to new connections/disconnections.
                      # Data sending rate is determined by hub polling.

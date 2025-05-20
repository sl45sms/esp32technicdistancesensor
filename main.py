# ESP32 MicroPython Sketch for Emulating Technic/SPIKE Distance Sensor

from pupremote import PUPRemoteSensor
import time
import machine

# Define your GPIO pins here
TRIG_PIN = 13   # GPIO13(IO13), change as needed
ECHO_PIN = 14  #  GPIO14(IO14), change as needed

# LEGO Technic/SPIKE Prime Distance Sensor Device ID
TECHNIC_DISTANCE_SENSOR_ID = 62  # Hex: 0x3E

# Initialize PUPRemoteSensor
# If your LEGO hub is running Pybricks firmware, max_packet_size=16 is crucial.
# For official LEGO firmware on hubs like SPIKE Prime or Robot Inventor,
# the default packet size might be acceptable, but 16 is safer for broader compatibility.
esp32_as_sensor = PUPRemoteSensor(sensor_id=TECHNIC_DISTANCE_SENSOR_ID, max_packet_size=16)

# Initialize GPIO pins
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# function to read distance from the ultrasonic sensor
def distance_mm():
    """
    Reads distance from HY-SRF05 ultrasonic sensor in millimeters.
    Includes timeout to avoid infinite loop if sensor fails.
    """
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Wait for echo to go high (start pulse)
    timeout = 10000  # microseconds
    start_wait = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), start_wait) > timeout:
            return 0  # Timeout waiting for echo high
    start = time.ticks_us()

    # Wait for echo to go low (end pulse)
    end_wait = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), end_wait) > timeout:
            return 2000  # Timeout waiting for echo low (max distance)
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    distance = (duration * 0.343) / 2
    if distance < 50:
        return 0
    elif distance > 2000:
        return 2000
    return int(distance)

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

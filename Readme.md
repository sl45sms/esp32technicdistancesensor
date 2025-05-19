A diy technic distance sensor using HY-SRF05 ultrasonic sensor on LMS-ESP32-v2.0 board from antonsmindstorms.com

Use a voltage divider to convert the 5V signal from the HY-SRF05 echo pin to 3.3V for the ESP32.

like this:
```
VCC (5V) ----> HY-SRF05 VCC
GND (GND) ----> HY-SRF05 GND
GPIO 13(IO13) ----> HY-SRF05 TRIG
GPIO 14(IO14) ----> HY-SRF05 ECHO (use voltage divider with 1k on sensor echo pin and 2k resistor to GND, get the ~3.3V signal from the junction of the two resistors) 
```

Tested with "train hub" but should work with any powered up hub.

demo video:[https://youtube.com/shorts/TxOgPfGrovo?feature=share]

* development with vscode and pymakr extension, change the serial port on workspace settings
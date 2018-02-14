# Arduino to Raspberry Pi Data Transfer

The easiest way to send information to the Raspberry Pi is through the USB ports on the Arduino Uno and Raspberry Pi 3.

## Output Data Serially from Arduino

Write to serial

``` cpp
void setup() {
    Serial.begin(9600);
}

void loop() {
    // logic
    Serial.println("<data>")
}
```

## Read Serial Output from Arduino

Run Python 2 [not Python 3] on the Raspberry Pi from Programming menu. Type:

``` python
import Serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
    ser.readline()
```

### Device Name

In order to find the device name, go to terminal with Arduino unplugged and run the command: `ls /dev/tty*`

Run this command again with arduino plugged in, and the name that appears is the Arduino device name. It is most likely `/dev/ttyACM0`.


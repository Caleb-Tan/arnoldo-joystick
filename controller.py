import time
from tts import Tts
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

tts = Tts()

# joystick area constraints
deadzone_dist = 150**2
max_x = 100
max_y = 100

# Main program loop.
while True:
    x = int(mcp.read_adc(1))-512
    y = int(mcp.read_adc(0))-512
    center_dist = (x**2) + (y**2)
    if center_dist > deadzone_dist:
        if x > 0:
            print ("yee")
    print(str(x) + " | " + str(y))
    time.sleep(0.1)

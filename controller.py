import math
import time
from tts import Tts
from gui import Gui
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 2
MISO = 3
MOSI = 4
CS   = 14
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

class Controller:
    def __init__(self):
        self.deadzone_dist = 100**2
        self.pressure_cutoff = 1023
        self.max_x_dist = 75
        self.max_y_dist = 75
        self.init_x = mcp.read_adc(1)
        self.init_y = mcp.read_adc(0)
        self.tts = Tts()
        self.in_zone = True
        self.is_pressed = False

    def ret_deadzone(self):
        return int(math.sqrt(self.deadzone_dist))

    def check_vals(self, x, y, n):
        x = x - self.init_x
        y = y - self.init_y
	    #print(str(x) + " | " + str(y))
        # if n > self.pressure_cutoff and self.in_zone:
        #     self.is_pressed = True
        center_dist = (x**2) + (y**2)
        if center_dist > self.deadzone_dist and self.in_zone:
            if (-self.max_x_dist < x < self.max_x_dist):
                self.tts.handle_action(0) if y < 0 else self.tts.handle_action(2)
                self.in_zone = False
            elif (-self.max_y_dist < y < self.max_y_dist):
                self.tts.handle_action(1) if x < 0 else self.tts.handle_action(3)
                self.in_zone = False
        elif center_dist < self.deadzone_dist:
            self.in_zone = True

# Main program loop.
if __name__ == "__main__":
    c = Controller()
    g = Gui()
    while True:
        x = int(mcp.read_adc(1))
        y = int(mcp.read_adc(0))
        n = int(mcp.read_adc(6))
        print(str(x) + " | " + str(y))
        c.check_vals(x, y, n)
        g.draw_joystick(x, y, n)
        time.sleep(0.1)

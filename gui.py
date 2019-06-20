from guizero import App, Box, Text, Drawing
from tkinter import *
from controller import Controller

class Gui:
    def __init__(self):
        window_width = 900
        self.window_height = int(window_width*(2/3))
        self.js_box_width = self.window_height
        c_box_width = window_width - self.js_box_width
        self.js = 30
        dz = 100
        self.c = Controller()

        app = App(width=window_width, height=self.window_height, title="Speech Synth")
        joystick_box = Box(app, width=self.js_box_width, height="fill", align="left", border=True)
        control_box = Box(app, width=c_box_width, height="fill", align="right", border=True)
        joystick_box.set_border(2, "black")
        control_box.set_border(2, "black")
        # drawing joystick grid
        self.draw = Drawing(joystick_box, width="fill", height="fill")
        # deadzone circle
        self.draw.oval(int(self.js_box_width/2)-dz, int(self.window_height/2)-dz, int(self.js_box_width/2)+dz, int(self.window_height/2)+dz, color="white", outline=True, outline_color="red")
        # x and y axis lines
        self.draw.line(int(self.js_box_width/2), 0, int(self.js_box_width/2), self.window_height, color="red", width=2) 
        self.draw.line(0, int(self.window_height/2), self.js_box_width, int(self.window_height/2), color="red", width=2)
        # joystick oval
        self.js_oval_id = self.draw.oval(int(self.js_box_width/2)-self.js, int(self.window_height/2)-self.js, int(self.js_box_width/2)+self.js, int(self.window_height/2)+self.js, color="blue", outline=False)
        self.draw.oval(0,0,5,5)
        self.draw.repeat(100, self.run_loop)
        app.display()

    def run_loop(self):
        values = self.c.run()
        self.draw_joystick(values[0], values[1], values[2])

    def draw_joystick(self, x, y, n):
        self.draw.delete(self.js_oval_id)
        x = x + 512
        x = 0 if x < 0 else x
        x = 1023 if x > 1023 else x
        y = y + 512
        y = 0 if y < 0 else y
        y = 1023 if y > 1023 else y
        x = (float(x)/1023)*self.js_box_width
        y = (float(y)/1023)*self.window_height
        print(str(x) + " | " + str(y))
        self.js_oval_id = self.draw.oval(x-self.js, y-self.js, x+self.js, y+self.js)

if __name__ == "__main__":
    g = Gui()
from guizero import App, Box, Text, Drawing
from tkinter import *
from controller import Controller

c = Controller()
window_width = 900
window_height = int(window_width*(2/3))
js_box_width = window_height
c_box_width = window_width - js_box_width
js = 30
dz = 100

def run_loop():
    values = c.run()
    draw_joystick(values[0], values[1], values[2])

def draw_joystick(x, y, n):
    draw.delete(js_oval_id)
    print(str(x) + " | " + str(y))
    x = 0 if x < 0 else x
    x = 1023 if x > 1023 else x
    y = 0 if y < 0 else y
    y = 1023 if y > 1023 else y
    x = (float(x)/1023)*js_box_width
    y = (float(y)/1023)*window_height
    # print(str(x) + " | " + str(y))
    js_oval_id = draw.oval(x-js, y-js, x+js, y+js,color="blue", outline=False)

app = App(width=window_width, height=window_height, title="Speech Synth")
joystick_box = Box(app, width=js_box_width, height="fill", align="left", border=True)
control_box = Box(app, width=c_box_width, height="fill", align="right", border=True)
joystick_box.set_border(2, "black")
control_box.set_border(2, "black")
# drawing joystick grid
draw = Drawing(joystick_box, width="fill", height="fill")
# deadzone circle
draw.oval(int(js_box_width/2)-dz, int(window_height/2)-dz, int(js_box_width/2)+dz, int(window_height/2)+dz, color="white", outline=True, outline_color="red")
# x and y axis lines
draw.line(int(js_box_width/2), 0, int(js_box_width/2), window_height, color="red", width=2) 
draw.line(0, int(window_height/2), js_box_width, int(window_height/2), color="red", width=2)
# joystick oval
js_oval_id = draw.oval(int(js_box_width/2)-js, int(window_height/2)-js, int(js_box_width/2)+js, int(window_height/2)+js, color="blue", outline=False)
draw.repeat(100, run_loop)
app.display()

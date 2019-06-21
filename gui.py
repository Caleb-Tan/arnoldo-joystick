from guizero import App, Box, Text, TextBox, Drawing
from tkinter import *
from controller import Controller

c = Controller()
window_width = 900
window_height = int(window_width*(2/3))
js_box_width = window_height
c_box_width = window_width - js_box_width
js = 30
dz = 100

app = App(width=window_width, height=window_height, title="Speech Synth")
main_box = Box(app, width=js_box_width, height="fill", align="left", border=True)
side_box = Box(app, width=c_box_width, height="fill", align="right", border=True)
main_box.set_border(2, "black")
side_box.set_border(2, "black")
### side box graphics
input_box = TextBox(side_box, align="top", multiline=True, height=50, width="fill")

### main panel graphics
# drawing joystick grid
draw = Drawing(main_box, width="fill", height="fill")
# deadzone circle
draw.oval(int(js_box_width/2)-dz, int(window_height/2)-dz, int(js_box_width/2)+dz, int(window_height/2)+dz, color="white", outline=True, outline_color="red")
# x and y axis lines
draw.line(int(js_box_width/2), 0, int(js_box_width/2), window_height, color="red", width=2) 
draw.line(0, int(window_height/2), js_box_width, int(window_height/2), color="red", width=2)
# text
draw.text(js_box_width/2-75, int(window_height/12)-20, "A, B, C, D, E", color="black", size=20, max_width=None) # top
draw.text(js_box_width/2-75, int(window_height*11/12), "L, M, N, O, P", color="black", size=20, max_width=None) # bottom
draw.text(int(js_box_width/12)-30, int(window_height/2), "F, G, H, I, J", color="black", size=20, max_width=None) # left
draw.text(int(js_box_width*7/10), int(window_height/2), "Q, R, S, U, T", color="black", size=20, max_width=None) # right
# joystick oval
js_oval_id = draw.oval(int(js_box_width/2)-js, int(window_height/2)-js, int(js_box_width/2)+js, int(window_height/2)+js, color="blue", outline=False)

def run_loop():
    values = c.run()
    draw_joystick(values[0], values[1], values[2])

def draw_joystick(x, y, n):
    global js_oval_id, js_box_width, window_height, js
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

draw.repeat(100, run_loop)
app.display()

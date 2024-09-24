from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

r = 300

def run_circle():
    for d in range(0,360):
        x = r * math.cos(math.radians(d))
        y = r * math.sin(math.radians(d))
    pass

def run_bottom():
    for x in range(50,750,10):
        draw_boy(x,90)
    pass

def run_right():
    for y in range(90,550,10):
        draw_boy(750,y)
    pass

def run_rectangle():
    run_bottom()
    run_right()
    run_top()
    run_left()

    pass

while True:
    run_circle()
    run_rectangle()

close_canvas()
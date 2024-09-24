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


while True:
    run_circle()
    run_rectangle()

close_canvas()
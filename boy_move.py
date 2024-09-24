from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

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
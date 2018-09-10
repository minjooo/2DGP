from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
angle=270
while (True):
    x=400
    y=90
    angle=270
    while(x<700 and y==90):
        x=x+2
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(x==700 and y<500):
        y=y+2
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(y==500 and x>100):
        x=x-2
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(x==100 and y>92):
        y=y-2
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(y==92 and x<400):
        x=x+2
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(angle<630):
        x=400+212*math.cos(math.radians(angle))
        y=300+212*math.sin(math.radians(angle))
        angle=angle+1
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

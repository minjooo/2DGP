from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_from_center_to_right():
    x, y = 800 // 2, 90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

def move_up():
    x, y = 800 - 25, 90
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

def move_left():
    x, y = 800 - 25, 600 - 50
    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

def move_down():
    x, y = 0 + 25, 600-50
    while y > 0 + 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

def move_from_right_to_center():
    x, y = 0 + 25, 90
    while x < 800//2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

def make_rectangle():
    # move_from_center_to_right()
    # move_up()
    # move_left()
    # move_down()
    # move_from_right_to_center()
    pass

def make_circle():
    angle = 270
    x,y=800//2,90
    while angle < 630:
        x=800//2 + 212 * math.cos(math.radians(angle))
        y = 300 + 212 * math.sin(math.radians(angle))
        angle+=1
        clear_canvas_now()
        grass.draw_now(800//2,30)
        character.draw_now(x,y)
        delay(0.01)

while True:
    make_rectangle()
    make_circle()

    
close_canvas()

from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def draw_character(x,y):
    global frame
    if where == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8

def move_character (p1, p2):
    for i in range(0, 100 + 1, 10):
        t = i/100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        global frame
        if where == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.02)
    draw_character(x, y)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
where=1
hide_cursor()
size=6
points = [(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]
n=1

while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    move_character(points[n-1], points[n])
    update_canvas()
    n = (n + 1) % size


close_canvas()
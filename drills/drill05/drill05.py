from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def go_203_132():
    frame=0
    count=0
    x=203
    y=535
    gox=(132-203)/100
    goy=(243-535)/100
    while count<=100:
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        update_canvas()
        count+=1
        x+=gox
        y+=goy
        frame=(frame+1)%8
        delay(0.05)

    pass
def go_132_535():
    pass
def go_535_477():
    pass
def go_477_715():
    pass
def go_715_316():
    pass
def go_316_510():
    pass
def go_510_692():
    pass
def go_692_682():
    pass
def go_682_712():
    pass

def go_682_203():
    pass

while True:
    go_203_132()
    go_132_535()
    go_535_477()
    go_477_715()
    go_715_316()
    go_316_510()
    go_510_692()
    go_692_682()
    go_682_712()
    go_682_203()
    
close_canvas()

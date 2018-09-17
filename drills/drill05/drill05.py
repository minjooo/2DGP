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

def go_132_535():
    frame = 0
    count = 0
    x = 132
    y = 243
    gox = (535 - 132) / 100
    goy = (470 - 243) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)

def go_535_477():
    frame = 0
    count = 0
    x = 535
    y = 470
    gox = (477 - 535) / 100
    goy = (203 - 470) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_477_715():
    frame = 0
    count = 0
    x = 477
    y = 203
    gox = (715 - 477) / 100
    goy = (136 - 203) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_715_316():
    frame = 0
    count = 0
    x = 715
    y = 136
    gox = (316 - 715) / 100
    goy = (225 - 136) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_316_510():
    frame = 0
    count = 0
    x = 316
    y = 225
    gox = (510 - 316) / 100
    goy = (92 - 225) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_510_692():
    frame = 0
    count = 0
    x = 510
    y = 92
    gox = (692 - 510) / 100
    goy = (518 - 92) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_692_682():
    frame = 0
    count = 0
    x = 692
    y = 518
    gox = (682 - 692) / 100
    goy = (336 - 518) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)
def go_682_712():
    frame = 0
    count = 0
    x = 682
    y = 336
    gox = (712 - 682) / 100
    goy = (349 - 336) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gox
        y += goy
        frame = (frame + 1) % 8
        delay(0.05)

def go_682_203():
    pass

while True:
    # go_203_132()
    # go_132_535()
    # go_535_477()
    # go_477_715()
    # go_715_316()
    # go_316_510()
    # go_510_692()
    # go_692_682()
    go_682_712()
    go_682_203()
    
close_canvas()

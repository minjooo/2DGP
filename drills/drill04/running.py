from pico2d import *
open_canvas()
grass=load_image('grass.png')
character=load_image('animation_sheet.png')

x=0
y=800
frame=0
while(True):
    x=0
    y=800
    while(x<800):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,100,100,100,x,90)
        update_canvas()
        frame=(frame+1)%8
        x+=5
        delay(0.05)
    while(y>0):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, y, 90)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)

close_canvas
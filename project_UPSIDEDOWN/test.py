from pico2d import *

open_canvas()
happy = load_image('run_happiness100.png')

frame=0
running = True

while running == True:
    clear_canvas()
    happy.clip_draw(frame*100,0,100,100,100,100)
    update_canvas()
    frame=(frame+1)%8
    delay(0.05)

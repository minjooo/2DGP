from pico2d import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
happy = load_image('run_happiness100.png')
sad = load_image('run_sadness100.png')

frame=0
running = True

while running == True:
    clear_canvas()
    happy.clip_draw(frame*100,0,100,100,100,100)
    sad.clip_draw(frame*100,0,100,100,230,100)
    update_canvas()
    frame=(frame+1)%8
    delay(0.05)
    handle_events()

close_canvas()
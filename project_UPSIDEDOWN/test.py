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
p_marble = load_image('purple_marble40.png')
b_marble = load_image('blue_marble30.png')
minjoo =  load_image('yellow_marble30.png')
card = load_image('card100.png')
boyfriend = load_image('imaginary_boyfriend100.png')
broom = load_image('broom100.png')

frame=0
Wframe=0
running = True

while running == True:
    clear_canvas()
    happy.clip_draw(frame*100,0,100,100,100,100)
    sad.clip_draw(frame*100,0,100,100,0,0)
    p_marble.draw(100,250)
    b_marble.draw(200, 250)
    minjoo.draw(150,150)
    #card.draw(0,0)
    boyfriend.draw(250, 350)
    update_canvas()

    frame=(frame+1)%8
    Wframe=(Wframe+1)%4
    delay(0.05)
    handle_events()

close_canvas()
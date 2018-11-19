import game_framework
import main_state
from pico2d import *

name = 'pause_state'
image = None

class Pause:
    def __init__(self):
        self.image = load_image('resources\\pause360.png')
    def draw(self):
        self.image.draw(450,350)

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_p:
                game_framework.pop_state()

def update():
    pass

def draw():
    clear_canvas()
    main_state.draw()
    pause.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
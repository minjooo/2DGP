import game_framework
import choose_state
from pico2d import *

name = 'main_state'
image = None




def enter():
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(choose_state)

def update():
    pass

def draw():
    clear_canvas()
    update_canvas()



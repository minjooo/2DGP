import game_framework
import title_state
import main_state
from pico2d import *
import game_world

from Cursor import Cursor
import Choose_happiness300
from Choose_happiness300 import Choose_happiness300
from Choose_sadness300 import Choose_sadness300
from Background import ChooseBackground as Background

name = 'choose_state'
image = None





def enter():
    global cursor, background, sad, happy, selected_character
    cursor = Cursor()
    background = Background()
    sad = Choose_sadness300()
    happy = Choose_happiness300()
    selected_character = 'none'

    game_world.add_object(happy, 0)
    game_world.add_object(sad, 0)
    game_world.add_object(cursor, 1)


def exit():
    game_world.clear()

def handle_events():
    global cursor
    global selected_character
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if selected_character != 'none':
                game_world.clear()
                game_framework.push_state(main_state)
        else:
            for game_object in game_world.all_objects():
                game_object.handle_event(event)
            return

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    background.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.05)

def pause():
    pass

def resume():
    pass


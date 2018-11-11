import game_framework
import title_state
import main_state
from pico2d import *
import game_world

from Cursor import Cursor
from Choose_happiness300 import Choose_happiness300
from Choose_sadness300 import Choose_sadness300

name = 'choose_state'
image = None


class Choose_Background:
    def __init__(self):
        self.image = load_image('resources\\choose.png')
    def draw(self):
        self.image.draw(450, 350)


def enter():
    global cursor, choose_bg, sad, happy, selected_character
    cursor = Cursor()
    choose_bg = Choose_Background()
    sad = Choose_sadness300()
    happy = Choose_happiness300()
    selected_character = 'none'

    game_world.add_object(happy, 0)
    game_world.add_object(sad, 0)


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
        else:
            happy.handle_event(event)
            sad.handle_event(event)
            return

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    choose_bg.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    cursor.draw()
    update_canvas()
    delay(0.05)

def pause():
    pass

def resume():
    pass


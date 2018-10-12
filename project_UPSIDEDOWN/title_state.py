import game_framework
import choose_state
from pico2d import *

name = 'title_state'
image = None

class Cursor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('cursor80.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Start_Background:
    def __init__(self):
        self.image = load_image('start_image.png')

    def draw(self):
        self.image.draw(450,350)

class Big_start:
    def __init__(self):
        self.image = load_image('big_start.png')

    def draw(self):
        self.image.draw(450,350)

class Small_start:
    def __init__(self):
        self.image = load_image('small_start.png')

    def draw(self):
        self.image.draw(450, 350)


def enter():
    global start_select, cursor, start_bg, big_start, small_start
    start_select = False
    cursor = Cursor()
    start_bg = Start_Background()
    big_start = Big_start()
    small_start = Small_start()
    hide_cursor()

def exit():
    global start_select, cursor, start_bg, big_start, small_start
    del(cursor)
    del(start_select)
    del(start_bg)
    del(big_start)
    del(small_start)

def handle_events():
    global start_select
    global cursor
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 700 - 1 - event.y
            if 415 < event.x < 695 and 150 < (700 - 1 - event.y) < 260:
                start_select = True
            else:
                start_select = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if start_select:
                game_framework.change_state(choose_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update():
    pass

def draw():
    clear_canvas()
    start_bg.draw()
    if start_select:
        big_start.draw()
    else:
        small_start.draw()
    cursor.draw()
    update_canvas()



import game_framework
import choose_state
from pico2d import *
import game_world


from Cursor import Cursor
from Big_start import Big_start
from Small_start import Small_start
from Background import StartBackground as Background

name = 'title_state'
image = None


def enter():
    hide_cursor()
    global start_select, cursor, background, big_start, small_start
    start_select = False
    cursor = Cursor()
    background = Background()
    big_start = Big_start()
    small_start = Small_start()
    game_world.add_object(cursor, 0)

def exit():
    global start_select, background, big_start, small_start
    del(background)
    del(start_select)
    del(big_start)
    del(small_start)
    game_world.clear()

def handle_events():
    global start_select
    global cursor
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
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
            for game_object in game_world.all_objects():
                game_object.handle_event(event)
            return


def update():
    pass


def draw():
    clear_canvas()
    background.draw()
    if start_select:
        big_start.draw()
    else:
        small_start.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
        update_canvas()



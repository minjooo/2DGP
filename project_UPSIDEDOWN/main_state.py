import game_framework
import choose_state
import pause_state
from pico2d import *
import game_world

from Numbers import Numbers
from Run_happiness100 import Run_happiness100
from Run_sadness100 import Run_sadness100
from Path import Path
from FollowingMarbles import FollowingMarbles
from Map import Map
from Background import RunningBackground as Background

name = 'main_state'
image = None

number = None
map = None
is_crush = None
character = None
inputJump = None

def enter():
    global background, character, path, number, following_marbles, is_crush, map
    background = Background()
    if choose_state.selected_character == 'sad':
        character = Run_sadness100()
    elif choose_state.selected_character == 'happy':
        character = Run_happiness100()
    path = Path()
    number = Numbers()
    map = Map()
    following_marbles = FollowingMarbles()
    is_crush = False
    game_world.add_object(background, 0)
    game_world.add_object(path, 1)
    game_world.add_object(map, 1)
    game_world.add_object(number, 1)
    game_world.add_object(character, 1)
    game_world.add_object(following_marbles, 1)


def exit():
    global is_crush
    del (is_crush)
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(choose_state)
                return
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)
            else:
                for game_object in game_world.all_objects():
                    game_object.handle_event(event)
                return


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass

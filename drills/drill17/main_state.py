import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import ranking_state

import world_build_state
from boy import Boy
from zombie import Zombie

name = "MainState"
crush = None


def collide(a, b):
    global boy, zombie
    left_a, bottom_a, right_a, top_a = boy.get_bb()
    left_b, bottom_b, right_b, top_b = zombie.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None
zombie = None

def enter():
    global boy, zombie
    boy = world_build_state.get_boy()
    zombie = Zombie()
    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)


def update():
    global crush,boy
    for game_object in game_world.all_objects():
        game_object.update()
    crush = collide(boy, zombie)
    if True == crush:
        with open('ranking.json', 'w') as f:
            boy.start_time = json.dump(f)

        game_framework.change_state(ranking_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







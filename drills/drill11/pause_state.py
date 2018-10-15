import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state



name = "PauseState"

boy = None
grass = None
font = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.blink = False

    def update(self):
        if self.blink == False:
            self.blink = True
        else:
            self.blink = False
        delay(0.5)


    def draw(self):
        self.image.clip_draw(250,250,400,400,400,400)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, pause
    boy = Boy()
    grass = Grass()
    pause = Pause()


def exit():
    global boy, grass, pause
    del(boy)
    del(grass)
    del(pause)


def pause():
    pass



def resume():
    pass


def handle_events():
    global pause
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    boy.update()
    pause.update()


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if pause.blink:
        pause.draw()
    update_canvas()






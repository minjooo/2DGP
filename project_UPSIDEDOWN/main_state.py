import game_framework
import choose_state
import pause_state
import end_state
from pico2d import *
import game_world
import random

from Numbers import Numbers
from Run_happiness100 import Run_happiness100
from Run_sadness100 import Run_sadness100
from Path import Path
from Card import Card
from Broom import Broom
from Boyfriend import Boyfriend
from Marble import Marble
from Tray import Tray
from FollowingMarbles import FollowingMarbles
from Map import Map

name = 'main_state'
image = None

class Running_Background:
    def __init__(self):
        self.image = load_image('resources\\running_BG_bar.png')

    def draw(self):
        self.image.draw(450,350)


def enter():
    global main_bg, run_happy, run_sad, path, number, following_marbles, is_crush, map
    main_bg = Running_Background()
    run_happy = Run_happiness100()
    run_sad = Run_sadness100()
    path = Path()
    number = Numbers()
    map = Map()
    following_marbles = FollowingMarbles()
    is_crush = False
    game_world.add_object(map, 0)
    game_world.add_object(run_sad, 0)



def exit():
    global main_bg, run_happy, run_sad, path, number, Cards_up, Boyfriends_up, Brooms_up, Marbles_up,Cards_down, Boyfriends_down, Brooms_down, Marbles_down, Tray_up, Tray_down, up, down,following_marbles,  is_crush
    del main_bg
    del run_happy
    del run_sad
    del path
    del number
    del following_marbles
    del is_crush
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



def update():
    path.update()
    following_marbles.update()
    #check_Crush()
    if number.marble_number > 2:
        following_marbles.order = 3
    else:
        following_marbles.order = number.marble_number
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    main_bg.draw()
    path.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    if following_marbles.order != 0:
        if choose_state.selected_character == 'sad':
            if run_happy.UP:
                for following_marbles.num in range(1, following_marbles.order + 1):
                    following_marbles.blue_draw_up_f()
            else:
                for following_marbles.num in range(1, following_marbles.order + 1):
                    following_marbles.blue_draw_down_f()

        elif choose_state.selected_character == 'happy':
            if run_happy.UP:
                for following_marbles.num in range(1, following_marbles.order + 1):
                    following_marbles.yellow_draw_up_f()
            else:
                for following_marbles.num in range(1, following_marbles.order + 1):
                    following_marbles.yellow_draw_down_f()
    number.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass


def collide(ch_x1, ch_x2, ch_y1, ch_y2, e_x1, e_x2, e_y1, e_y2):
    if ch_x2 < e_x1:
        return False
    if e_x2 < ch_x1:
        return False
    if e_y2 < ch_y1:
        return False
    if ch_y2 < e_y1:
        return False
    return True


def check_Crush():
    ups = Cards_up + Boyfriends_up + Brooms_up + Marbles_up + Tray_up
    downs = Cards_down + Boyfriends_down + Brooms_down + Marbles_down + Tray_down
    is_crush = False
    for i in ups + downs:
        if i.x < 300 and i.x > 100:
            i.check = True
        else:
            i.check = False

    if run_happy.UP == True or run_sad.UP == True:
        for i in ups:  # 충돌 계산 해줄곳 위
            if i.check == True:
                if type(i) == Card:
                    is_crush = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                       i.x - 25, i.x + 25, 310, 370)
                if type(i) == Boyfriend:
                    is_crush = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                       i.x - 25, i.x + 25, 310, 510)
                if type(i) == Broom:
                    is_crush = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                       i.x - 20, i.x + 20, 419, 610)
                if type(i) == Marble:
                    if i.eated == False:
                        i.eated = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                          i.x - 15, i.x + 15, 310, 350)
                        if i.eated == True:
                            number.marble_number += 1
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                         i.x - 30, i.x + 30, 310, 400)
                        if i.full == True:
                            number.score = number.marble_number*1000
                            number.marble_number = 0


    if run_happy.UP == False or run_sad.UP == False:
        for i in downs:  # 충돌 계산 해줄곳 아래
            if i.check == True:
                if type(i) == Card:
                    is_crush = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                       i.x - 25, i.x + 25, 230, 290)
                if type(i) == Boyfriend:
                    is_crush = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                       i.x - 25, i.x + 25, 140, 290)
                if type(i) == Broom:
                    is_crush = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                       i.x - 20, i.x + 20, 0, 191)
                if type(i) == Marble:
                    if i.eated == False:
                        i.eated = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                          i.x - 15, i.x + 15, 250, 290)
                        if i.eated == True:
                            number.marble_number += 1
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                         i.x - 30, i.x + 30, 200, 290)
                        if i.full == True:
                            number.score = number.marble_number*1000
                            number.marble_number = 0

    if True == is_crush:
        game_framework.push_state(end_state)
import game_framework
import choose_state
import pause_state
import end_state
from pico2d import *
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

name = 'main_state'
image = None

class Running_Background:
    def __init__(self):
        self.image = load_image('resources\\running_BG_bar.png')

    def draw(self):
        self.image.draw(450,350)


def enter():
    global main_bg, run_happy, run_sad, path, number, Cards_up, Boyfriends_up, Brooms_up, Marbles_up, Tray_up, Tray_down, up, down, Cards_down, Boyfriends_down, Brooms_down, Marbles_down, following_marbles, is_crush
    main_bg = Running_Background()
    run_happy = Run_happiness100()
    run_sad = Run_sadness100()
    path = Path()
    number = Numbers()
    Cards_up = []
    Boyfriends_up = []
    Brooms_up = []
    Marbles_up = []
    Cards_down = []
    Boyfriends_down = []
    Brooms_down = []
    Marbles_down = []
    Tray_up = []
    Tray_down = []
    following_marbles = FollowingMarbles()
    is_crush = False

    f = open('resources\\map.txt', 'r')
    u = f.readline()
    d = f.readline()
    up = u.split()
    for i in range(0, len(up)):
        up[i] = int(up[i])
    down = d.split()
    for i in range(0, len(down)):
        down[i] = int(down[i])
    f.close()

    for i in range(0, len(up)): # up 훑겠다
        n = up[i]
        if n == 0:
            pass
        elif n == 1: # 카드
            Cards_up.append(Card())
            Cards_up[-1].x = i * 100
        elif n == 2: # 남친
            Boyfriends_up.append(Boyfriend())
            Boyfriends_up[-1].x = i * 100
        elif n == 3: # 빗자루
            Brooms_up.append(Broom())
            Brooms_up[-1].x = i * 100
        elif n == 4: #구슬하고싶은데
            Marbles_up.append(Marble())
            Marbles_up[-1].x = i * 100
            Marbles_up[-1].color = random.randint(1, 4 + 1)
        elif n == 5: # 트레이다
            Tray_up.append(Tray())
            Tray_up[-1].x = i * 100

    for i in range(0, len(down)): # down 훑겠다
        n = down[i]
        if n == 0:
            pass
        elif n == 1: # 카드
            Cards_down.append(Card())
            Cards_down[-1].x = i * 100
        elif n == 2: # 남친
            Boyfriends_down.append(Boyfriend())
            Boyfriends_down[-1].x = i * 100
        elif n == 3: # 빗자루
            Brooms_down.append(Broom())
            Brooms_down[-1].x = i * 100
        elif n == 4: #구슬하고싶은데
            Marbles_down.append(Marble())
            Marbles_down[-1].x = i * 100
            Marbles_down[-1].color = random.randint(1, 4 + 1)
        elif n == 5: # 트레이다
            Tray_down.append(Tray())
            Tray_down[-1].x = i * 100


def exit():
    global main_bg, run_happy, run_sad, path, number, Cards_up, Boyfriends_up, Brooms_up, Marbles_up,Cards_down, Boyfriends_down, Brooms_down, Marbles_down, Tray_up, Tray_down, up, down,following_marbles,  is_crush
    del main_bg
    del run_happy
    del run_sad
    del path
    del number
    del Cards_up
    del Boyfriends_up
    del Brooms_up
    del Marbles_up
    del Cards_down
    del Boyfriends_down
    del Brooms_down
    del Marbles_down
    del Tray_up
    del Tray_down
    del up
    del down
    del(following_marbles)
    del is_crush

def handle_events():
    global run_happy, run_sad, number
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
                return
            elif event.key == SDLK_SPACE:
                run_sad.jump = True
                run_happy.jump = True
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.key == SDLK_DELETE and run_sad.jump == False and run_happy.jump == False:
                if run_sad.UP and run_happy.UP:
                    run_sad.UP = False
                    run_happy.UP = False
                else:
                    run_sad.UP = True
                    run_happy.UP = True


#FRAME_CYCLE = 10
#frame = 0

def update():
    #global frame
    #frame = (frame + 1) % FRAME_CYCLE
    #if 0 == frame:
    run_sad.update()
    run_happy.update()
    path.update()
    following_marbles.update()
    check_Crush()
    for i in Cards_up + Boyfriends_up + Brooms_up + Cards_down + Boyfriends_down + Brooms_down + Marbles_up + Marbles_down + Tray_up + Tray_down:
        i.update()
    if number.total_marble_number > 2:
        following_marbles.order = 3
    else:
        following_marbles.order = number.total_marble_number


def draw():
    clear_canvas()
    main_bg.draw()
    path.draw()
    for i in Cards_up + Boyfriends_up + Brooms_up:
        i.draw_up()
    for i in Cards_down + Boyfriends_down + Brooms_down:
        i.draw_down()
    for i in Marbles_up:
        if i.eated == False:
            if i.color == 1:
                i.red_draw_up()
            elif i.color == 2:
                i.blue_draw_up()
            elif i.color == 3:
                i.yellow_draw_up()
            elif i.color == 4:
                i.purple_draw_up()
    for i in Marbles_down:
        if i.eated == False:
            if i.color == 1:
                i.red_draw_down()
            elif i.color == 2:
                i.blue_draw_down()
            elif i.color == 3:
                i.yellow_draw_down()
            elif i.color == 4:
                i.purple_draw_down()
    for i in Tray_up:
        if i.full == False:
            i.draw_empty_up()
        else:
            i.draw_full_up()
    for i in Tray_down:
        if i.full == False:
            i.draw_empty_down()
        else:
            i.draw_full_down()
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
    number.draw_score()
    number.draw_marble_num()
    if choose_state.selected_character == 'sad':
        if run_sad.jump:
            if run_sad.UP:
                run_sad.draw_jump_up()
            else:
                run_sad.draw_jump_down()
        else:
            if run_sad.UP:
                run_sad.draw_up()
            elif run_sad.UP == False:
                run_sad.draw_down()
    elif choose_state.selected_character == 'happy':
        if run_happy.jump:
            if run_happy.UP:
                run_happy.draw_jump_up()
            else:
                run_happy.draw_jump_down()
        else:
            if run_happy.UP:
                run_happy.draw_up()
            elif run_happy.UP == False:
                run_happy.draw_down()
    if game_framework.stack[-1].name == name:
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
                            number.total_marble_number += 1
                            number.marble_number = number.total_marble_number
                            number.update_marble()
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 360 + run_happy.height - 10, 360 + run_happy.height + 40,
                                         i.x - 30, i.x + 30, 310, 400)
                        if i.full == True:
                            number.total_score = number.total_marble_number
                            number.score = number.total_score
                            number.total_marble_number = 0
                            number.update_score()
                            number.update_marble()


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
                            number.total_marble_number += 1
                            number.marble_number = number.total_marble_number
                            number.update_marble()
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 240 - run_happy.height - 40, 240 - run_happy.height + 10,
                                         i.x - 30, i.x + 30, 200, 290)
                        if i.full == True:
                            number.total_score += number.total_marble_number
                            number.score = number.total_score
                            number.total_marble_number = 0
                            number.update_score()
                            number.update_marble()

    if True == is_crush:
        game_framework.push_state(end_state)
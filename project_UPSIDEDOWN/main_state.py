import game_framework
import choose_state
import pause_state
import end_state
from pico2d import *
import random

name = 'main_state'
image = None

class Running_Background:
    def __init__(self):
        self.image = load_image('running_BG_bar.png')

    def draw(self):
        self.image.draw(450,350)


class Numbers:
    image = None
    def __init__(self):
        self.total_score = 0
        self.score = 0
        self.total_marble_number = 0
        self.marble_number = 0
        self.score100 = 0
        self.score10 = 0
        self.score1 = 0
        self.marble10 = 0
        self.marble1 = 0
        if Numbers.image == None:
            Numbers.image = load_image('number.png')

    def update_score(self):
        if self.score >= 100:
            self.score100 = 0
            while self.score >= 100:
                self.score -= 100
                self.score100 += 1
        if self.score >= 10:
            self.score10 = 0
            while self.score >= 10:
                self.score -=10
                self.score10 += 1
        self.score1 = self.score
        self.score = 0
    def update_marble(self):
        if self.marble_number >= 10:
            self.marble10 = 0
            while self.marble_number >= 10:
                self.marble_number -= 10
                self.marble10 += 1
        self.marble1 = self.marble_number
        self.marble_number = 0

    def draw_score(self):
        if self.score100 != 0:
            self.image.clip_draw(self.score100*25,0,25,50,175,649)
        if self.score10 != 0 or (self.score10 == 0 and self.score100 != 0):
            self.image.clip_draw(self.score10*25,0,25,50,200,649)
        if self.total_score != 0:
            self.image.clip_draw(0, 0, 25, 50, 250, 649)
            self.image.clip_draw(0, 0, 25, 50, 275, 649)
            self.image.clip_draw(0, 0, 25, 50, 300, 649)
        self.image.clip_draw(self.score1*25, 0, 25, 50, 225, 649)
    def draw_marble_num(self):
        if self.marble10 != 0:
            self.image.clip_draw(self.marble10*25,0,25,50,670,649)
        self.image.clip_draw(self.marble1 * 25, 0, 25, 50, 695, 649)


class Run_happiness100:
    def __init__(self):
        self.point = 0
        self.UP = True
        self.hight = 0
        self.jump = False
        self.goup = True # 점프할 때 올라가는지 내려가는지 구분
        self.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        self.count_jump_speed = -1
        self.frame = 0
        self.image_up = load_image('run_happiness100.png')
        self.image_down = load_image('run_happiness100_down.png')
        self.image_jump_up = load_image('run_happiness100_jump.png')
        self.image_jump_down = load_image('run_happiness100_jump_down.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.hight += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -8:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100, 0, 100, 100, 200, 360 + self.hight)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100, 0, 100, 100, 200, 240 - self.hight)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.hight)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.hight)


class Run_sadness100:
    def __init__(self):
        self.point = 0
        self.UP = True
        self.jump = False
        self.goup = True
        self.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        self.count_jump_speed = -1
        self.height = 0
        self.frame = 0
        self.image_up = load_image('run_sadness100.png')
        self.image_down = load_image('run_sadness100_down.png')
        self.image_jump_up = load_image('run_sadness100_jump.png')
        self.image_jump_down = load_image('run_sadness100_jump_down.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.height += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -8:
                    self.goup = False
            if self.goup == False:
                self.height -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100, 0, 100, 100, 200, 360 + self.height)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100, 0, 100, 100, 200, 240 - self.height)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.height)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.height)


class Path:
    def __init__(self):
        self.frame = 0
        self.image = load_image('path1350_3.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 45, 0, 900, 20, 450, 300)


class Card:
    image_up = None
    image_down = None
    def __init__(self):
        self.x = None
        self.check = False
        if Card.image_up == None:
            Card.image_up = load_image('card100.png')
        if Card.image_down == None:
            Card.image_down = load_image('card100_down.png')

    def update(self):
        self.x -= 12

    def draw_up(self):
        self.image_up.draw(self.x, 360)
    def draw_down(self):
        self.image_down.draw(self.x, 240)

class Boyfriend:
    image_up = None
    image_down = None
    def __init__(self):
        self.x = None
        self.check = False
        if Boyfriend.image_up == None:
            Boyfriend.image_up = load_image('imaginary_boyfriend100.png')
        if Boyfriend.image_down == None:
            Boyfriend.image_down = load_image('imaginary_boyfriend100_down.png')

    def update(self):
        self.x -= 12

    def draw_up(self):
        self.image_up.draw(self.x, 410)
    def draw_down(self):
        self.image_down.draw(self.x,190)


class Broom:
    image_up = None
    image_down = None
    def __init__(self):
        self.x = None
        self.check = False
        if Broom.image_up == None:
            Broom.image_up = load_image('broom100.png')
        if Broom.image_down == None:
            Broom.image_down = load_image('broom100_down.png')

    def update(self):
        self.x -= 12

    def draw_up(self):
        self.image_up.draw(self.x, 510)
    def draw_down(self):
        self.image_down.draw(self.x, 90)


class Marble:
    red_image_up = None
    blue_image_up = None
    purple_image_up = None
    yellow_image_up = None
    red_image_down = None
    blue_image_down = None
    purple_image_down = None
    yellow_image_down = None
    def __init__(self):
        self.x = None
        self.color = 0
        self.eated = False
        self.check = False
        if Marble.red_image_up == None:
            Marble.red_image_up = load_image('red_marble40.png')
        if Marble.blue_image_up == None:
            Marble.blue_image_up = load_image('blue_marble40.png')
        if Marble.purple_image_up == None:
            Marble.purple_image_up = load_image('purple_marble40.png')
        if Marble.yellow_image_up == None:
            Marble.yellow_image_up = load_image('yellow_marble40.png')
        if Marble.red_image_down == None:
            Marble.red_image_down = load_image('red_marble40_down.png')
        if Marble.blue_image_down == None:
            Marble.blue_image_down = load_image('blue_marble40_down.png')
        if Marble.purple_image_down == None:
            Marble.purple_image_down = load_image('purple_marble40_down.png')
        if Marble.yellow_image_down == None:
            Marble.yellow_image_down = load_image('yellow_marble40_down.png')

    def update(self):
        self.x -= 12

    def red_draw_up(self):
        self.red_image_up.draw(self.x, 330)
    def blue_draw_up(self):
        self.blue_image_up.draw(self.x, 330)
    def purple_draw_up(self):
        self.purple_image_up.draw(self.x, 330)
    def yellow_draw_up(self):
        self.yellow_image_up.draw(self.x, 330)

    def red_draw_down(self):
        self.red_image_down.draw(self.x, 270)
    def blue_draw_down(self):
        self.blue_image_down.draw(self.x, 270)
    def purple_draw_down(self):
        self.purple_image_down.draw(self.x, 270)
    def yellow_draw_down(self):
        self.yellow_image_down.draw(self.x, 270)

class Tray:
    empty_image = None
    full_image = None
    empty_image_down = None
    full_image_down = None
    def __init__(self):
        self.x = None
        self.full = False
        self.check = False
        if Tray.empty_image == None:
            Tray.empty_image = load_image('tray100.png')
        if Tray.full_image == None:
            Tray.full_image = load_image('tray100_full.png')
        if Tray.empty_image_down == None:
            Tray.empty_image_down = load_image('tray100_down.png')
        if Tray.full_image_down == None:
            Tray.full_image_down = load_image('tray100_full_Down.png')

    def update(self):
        self.x -= 12

    def draw_empty_up(self):
        self.empty_image.draw(self.x, 360)
    def draw_full_up(self):
        self.full_image.draw(self.x, 360)
    def draw_empty_down(self):
        self.empty_image_down.draw(self.x, 240)
    def draw_full_down(self):
        self.full_image_down.draw(self.x, 240)


class FollowingMarbles:
    red_image_up_f = None
    blue_image_up_f = None
    purple_image_up_f = None
    yellow_image_up_f = None
    red_image_down_f = None
    blue_image_down_f = None
    purple_image_down_f = None
    yellow_image_down_f = None
    def __init__(self):
        self.order = 0 #순서 저장할꺼임 1개,2개,3개 이렇게 구슬 다 반납하면 0으로
        self.num = 0
        self.color = 0
        self.hight = 0
        self.jump = False
        self.goup = True
        self.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        self.count_jump_speed = -1
        self.height = 0
        if FollowingMarbles.red_image_up_f == None:
            FollowingMarbles.red_image_up_f = load_image('red_marble30.png')
        if FollowingMarbles.blue_image_up_f == None:
            FollowingMarbles.blue_image_up_f = load_image('blue_marble30.png')
        if FollowingMarbles.purple_image_up_f == None:
            FollowingMarbles.purple_image_up_f = load_image('purple_marble30.png')
        if FollowingMarbles.yellow_image_up_f == None:
            FollowingMarbles.yellow_image_up_f = load_image('yellow_marble30.png')
        if FollowingMarbles.red_image_down_f == None:
            FollowingMarbles.red_image_down_f = load_image('red_marble30_down.png')
        if FollowingMarbles.blue_image_down_f == None:
            FollowingMarbles.blue_image_down_f = load_image('blue_marble30_down.png')
        if FollowingMarbles.purple_image_down_f == None:
            FollowingMarbles.purple_image_down_f = load_image('purple_marble30_down.png')
        if FollowingMarbles.yellow_image_down_f == None:
            FollowingMarbles.yellow_image_down_f = load_image('yellow_marble30_down.png')

    def update(self):
        if self.jump:
            if self.goup:
                self.hight += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -8:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1


    def red_draw_up_f(self):
        self.red_image_up_f.draw(165 - (self.num * 45), 360 + self.hight)
    def blue_draw_up_f(self):
        self.blue_image_up_f.draw(165 - (self.num * 45), 360 + self.hight)
    def purple_draw_up_f(self):
        self.purple_image_up_f.draw(165 - (self.num * 45), 360 + self.hight)
    def yellow_draw_up_f(self):
        self.yellow_image_up_f.draw(165 - (self.num * 45), 360 + self.hight)

    def red_draw_down_f(self):
        self.red_image_down_f.draw(165 - (self.num * 45), 240 - self.hight)
    def blue_draw_down_f(self):
        self.blue_image_down_f.draw(165 - (self.num * 45), 240 - self.hight)
    def purple_draw_down_f(self):
        self.purple_image_down_f.draw(165 - (self.num * 45), 240 - self.hight)
    def yellow_draw_down_f(self):
        self.yellow_image_down_f.draw(165 - (self.num * 45), 240 - self.hight)






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

    f = open('map.txt', 'r')
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
                    is_crush = collide(170, 220, 360 + run_happy.hight - 10, 360 + run_happy.hight + 40,
                                       i.x - 25, i.x + 25, 310, 370)
                if type(i) == Boyfriend:
                    is_crush = collide(170, 220, 360 + run_happy.hight - 10, 360 + run_happy.hight + 40,
                                       i.x - 25, i.x + 25, 310, 510)
                if type(i) == Broom:
                    is_crush = collide(170, 220, 360 + run_happy.hight - 10, 360 + run_happy.hight + 40,
                                       i.x - 20, i.x + 20, 419, 610)
                if type(i) == Marble:
                    if i.eated == False:
                        i.eated = collide(170, 220, 360 + run_happy.hight - 10, 360 + run_happy.hight + 40,
                                          i.x - 15, i.x + 15, 310, 350)
                        if i.eated == True:
                            number.total_marble_number += 1
                            number.marble_number = number.total_marble_number
                            number.update_marble()
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 360 + run_happy.hight - 10, 360 + run_happy.hight + 40,
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
                    is_crush = collide(170, 220, 240 - run_happy.hight - 40, 240 - run_happy.hight + 10,
                                       i.x - 25, i.x + 25, 230, 290)
                if type(i) == Boyfriend:
                    is_crush = collide(170, 220, 240 - run_happy.hight - 40, 240 - run_happy.hight + 10,
                                       i.x - 25, i.x + 25, 140, 290)
                if type(i) == Broom:
                    is_crush = collide(170, 220, 240 - run_happy.hight - 40, 240 - run_happy.hight + 10,
                                       i.x - 20, i.x + 20, 0, 191)
                if type(i) == Marble:
                    if i.eated == False:
                        i.eated = collide(170, 220, 240 - run_happy.hight - 40, 240 - run_happy.hight + 10,
                                          i.x - 15, i.x + 15, 250, 290)
                        if i.eated == True:
                            number.total_marble_number += 1
                            number.marble_number = number.total_marble_number
                            number.update_marble()
                if type(i) == Tray:
                    if i.full == False:
                        i.full = collide(170, 220, 240 - run_happy.hight - 40, 240 - run_happy.hight + 10,
                                         i.x - 30, i.x + 30, 200, 290)
                        if i.full == True:
                            number.total_score += number.total_marble_number
                            number.score = number.total_score
                            number.total_marble_number = 0
                            number.update_score()
                            number.update_marble()

    if True == is_crush:
        game_framework.push_state(end_state)
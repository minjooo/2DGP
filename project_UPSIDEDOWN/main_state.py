import game_framework
import choose_state
import pause_state
from pico2d import *

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
        self.image.clip_draw(self.score1*25,0,25,50,225,649)
    def draw_marble_num(self):
        if self.marble10 != 0:
            self.image.clip_draw(self.marble10*25,0,25,50,670,649)
        self.image.clip_draw(self.marble1 * 25, 0, 25, 50, 695, 649)

class Run_happiness100:
    def __init__(self):
        self.UP = True
        self.hight = 0
        self.jump = False
        self.goup = True # 점프할 때 올라가는지 내려가는지 구분
        self.jump_speed = [n for n in range(0, 20 + 1) if n % 2 == 0]
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
                if self.count_jump_speed == -11:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100, 0, 100, 100, 200, 360)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100, 0, 100, 100, 200, 240)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.hight)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.hight)


class Run_sadness100:
    def __init__(self):
        self.UP = True
        self.jump = False
        self.goup = True
        self.jump_speed = [n for n in range(0, 20 + 1) if n % 2 == 0]
        self.count_jump_speed = -1
        self.hight = 0
        self.frame = 0
        self.image_up = load_image('run_sadness100.png')
        self.image_down = load_image('run_sadness100_down.png')
        self.image_jump_up = load_image('run_sadness100_jump.png')
        self.image_jump_down = load_image('run_sadness100_jump_down.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.hight += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -11:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100 , 0, 100, 100, 200, 360)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100 , 0, 100, 100, 200, 240)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.hight)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.hight)


class Path:
    def __init__(self):
        self.x ,self.y = 450, 300
        self.frame = 0
        self.image = load_image('path1350_3.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 45, 0, 900, 20, self.x, self.y)


class Card:
    image_up = None
    image_down = None
    def __init__(self):
        self.x_up , self.y_up = 1000, 365
        self.x_down, self.y_down = 1000,250
        if Card.image_up == None:
            Card.image_up = load_image('card100.png')
        if Card.image_down == None:
            Card.image_down = load_image('card100_down.png')

    def update(self):
        self.x_up -= 5
        self.x_down -= 5

    def draw_up(self):
        pass
    def draw_down(self):
        pass

def enter():
    global main_bg, run_happy, run_sad, path, number
    main_bg = Running_Background()
    run_happy = Run_happiness100()
    run_sad = Run_sadness100()
    path = Path()
    number = Numbers()

def exit():
    global main_bg, run_happy, run_sad, path, number
    del(main_bg)
    del(run_happy)
    del(run_sad)
    del(path)
    del(number)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_SPACE:
                run_sad.jump = True
                run_happy.jump = True
            elif event.key == SDLK_s:
                number.total_score += 1
                number.score = number.total_score
                number.update_score()
            elif event.key == SDLK_m:
                number.total_marble_number += 1
                number.marble_number = number.total_marble_number
                number.update_marble()
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.key == SDLK_DELETE and run_sad.jump == False and run_happy.jump == False:
                if run_sad.UP and run_happy.UP:
                    run_sad.UP = False
                    run_happy.UP = False
                else:
                    run_sad.UP = True
                    run_happy.UP = True

def update():
    run_sad.update()
    run_happy.update()
    path.update()

def draw():
    clear_canvas()
    main_bg.draw()
    path.draw()
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
    update_canvas()
    delay(0.05)

def pause():
    pass

def resume():
    pass
from pico2d import *
import random
import game_framework

import main_state
import choose_state

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 300.0

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class FollowingMarbles:
    def __init__(self):
        self.order = 0 #순서 저장할꺼임 1개,2개,3개 이렇게 구슬 다 반납하면 0으로
        self.marbles = []
        self.inputJump = main_state.inputJump
        for i in range(0, 3):
            self.marbles.append(EachMarble())
            self.marbles[i].num = i + 1
            self.marbles[i].angle = i * 30

    def update(self):
        ##self.inputJump = main_state.inputJump
        if main_state.number.marble_number > 3:
            self.order = 3
        else:
            self.order = main_state.number.marble_number
        for i in range(0, 3):
            self.marbles[i].update()
        #if self.inputJump == True:
        #    for i in range(0, 3):
        #        self.marbles[i].jump = True


    def draw(self):
        if self.order !=0:
            if choose_state.selected_character == 'sad':
                if main_state.character.position == 'up':
                    for i in range(1, self.order + 1):
                        self.marbles[i - 1].blue_draw_up_f()
                else:  # down
                    for i in range(1, self.order + 1):
                        self.marbles[i - 1].blue_draw_down_f()

            elif choose_state.selected_character == 'happy':
                if main_state.character.position == 'up':
                    for i in range(1, self.order + 1):
                        self.marbles[i - 1].yellow_draw_up_f()
                else:  # down
                    for i in range(1, self.order + 1):
                        self.marbles[i - 1].yellow_draw_down_f()


    def handle_event(self, event):
        pass


class EachMarble:
    blue_image_f = None
    yellow_image_f = None
    def __init__(self):
        self.num = 0
        self.color = 0
        self.height = 0
        self.jump = False
        self.goup = True
        self.angle = 0
        if EachMarble.blue_image_f == None:
            EachMarble.blue_image_f = load_image('resources/blue_marble30.png')
        if EachMarble.yellow_image_f == None:
            EachMarble.yellow_image_f = load_image('resources/yellow_marble30.png')


    def update(self):
        if self.goup == True:
            self.height += (1 - math.sin(self.angle * math.pi / 180)) * 21
            self.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if self.angle >= 90:
                self.goup = False
        else:
            self.height -= (1 - math.sin(self.angle * math.pi / 180)) * 21
            self.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if self.angle >= 180:
                self.goup = True
                self.angle = 0
                self.height = 0
                self.jump = False

    def draw(self):
        pass

    def blue_draw_up_f(self):
        self.blue_image_f.draw(165 - (self.num * 45), 325 + self.height)

    def yellow_draw_up_f(self):
        self.yellow_image_f.draw(165 - (self.num * 45), 325 + self.height)

    def blue_draw_down_f(self):
        self.blue_image_f.clip_composite_draw(0, 0, 30, 30, 0, 'v', 165 - (self.num * 45), 265 - self.height, 30, 30)

    def yellow_draw_down_f(self):
        self.yellow_image_f.clip_composite_draw(0, 0, 30, 30, 0, 'v', 165 - (self.num * 45), 265 - self.height, 30, 30)

    def handle_event(self, event):
        pass
from pico2d import *

import main_state
import choose_state

class FollowingMarbles:
    blue_image_f = None
    yellow_image_f = None
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
        if FollowingMarbles.blue_image_f == None:
            FollowingMarbles.blue_image_f = load_image('resources/blue_marble30.png')
        if FollowingMarbles.yellow_image_f == None:
            FollowingMarbles.yellow_image_f = load_image('resources/yellow_marble30.png')

    def update(self):
        if main_state.number.marble_number > 2:
            self.order = 3
        else:
            self.order = main_state.number.marble_number
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

    def draw(self):
        if self.order != 0:
            if choose_state.selected_character == 'sad':
                if main_state.character.position == 'up':
                    for self.num in range(1, self.order + 1):
                        self.blue_draw_up_f()
                else:
                    for self.num in range(1, self.order + 1):
                        self.blue_draw_down_f()

            elif choose_state.selected_character == 'happy':
                if main_state.character.position == 'up':
                    for self.num in range(1, self.order + 1):
                        self.yellow_draw_up_f()
                else:
                    for self.num in range(1, self.order + 1):
                        self.yellow_draw_down_f()

    def blue_draw_up_f(self):
        self.blue_image_f.draw(165 - (self.num * 45), 360 + self.hight)
    def yellow_draw_up_f(self):
        self.yellow_image_f.draw(165 - (self.num * 45), 360 + self.hight)

    def blue_draw_down_f(self):
        self.blue_image_f.clip_composite_draw(0, 0, 30, 30, 0, 'v', 165 - (self.num * 45), 240 - self.hight, 30, 30)
    def yellow_draw_down_f(self):
        self.yellow_image_f.clip_composite_draw(0, 0, 30, 30, 0, 'v', 165 - (self.num * 45), 240 - self.hight, 30, 30)

    def handle_event(self, event):
        pass
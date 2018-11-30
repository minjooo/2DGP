from pico2d import *
import end_state
import game_framework
import math

import main_state

import FollowingMarbles
import Map as P_map

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 300.0

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

SPACE, ENTER, LANDING = range(3)

key_event_table = {
    (SDL_KEYDOWN, 13): ENTER,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class RunUpState:

    @staticmethod
    def enter(happy, event):
        happy.position = 'up'

    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        happy.frame = (happy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(happy):
        happy.image.clip_draw(int(happy.frame) * 100, 0, 100, 100, 200, 360)


class RunDownState:

    @staticmethod
    def enter(happy, event):
        happy.position = 'down'

    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        happy.frame = (happy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(happy):
        happy.image.clip_composite_draw(int(happy.frame) * 100, 0, 100, 100, 0, 'v', 200, 240, 100, 100)


class JumpUpState:

    @staticmethod
    def enter(happy, event):
        pass

    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        if happy.goup == True:
            happy.height += (1 - math.sin(happy.angle * math.pi / 180)) * 32
            happy.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if happy.angle >= 90:
                happy.goup = False
        else:
            happy.height -= (1 - math.sin(happy.angle * math.pi / 180)) * 32
            happy.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if happy.angle >= 180:
                happy.goup = True
                happy.angle = 0
                happy.height = 0
                happy.add_event(LANDING)

    @staticmethod
    def draw(happy):
        happy.image_jump.draw(200, 360 + happy.height)


class JumpDownState:

    @staticmethod
    def enter(happy, event):
        pass


    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        if happy.goup == True:
            happy.height += (1 - math.sin(happy.angle * math.pi / 180)) * 32
            happy.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if happy.angle >= 90:
                happy.goup = False
        else:
            happy.height -= (1 - math.sin(happy.angle * math.pi / 180)) * 32
            happy.angle += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
            if happy.angle >= 180:
                happy.goup = True
                happy.angle = 0
                happy.height = 0
                happy.add_event(LANDING)

    @staticmethod
    def draw(happy):
        happy.image_jump.clip_composite_draw(0, 0, 100, 100, 0, 'v', 200, 240 - happy.height, 100, 100)


next_state_table = {
    RunUpState: {SPACE: JumpUpState, ENTER: RunDownState},
    RunDownState: {SPACE: JumpDownState, ENTER: RunUpState},
    JumpUpState: {SPACE: JumpUpState, ENTER: JumpUpState, LANDING: RunUpState},
    JumpDownState: {SPACE: JumpDownState, ENTER: JumpDownState, LANDING: RunDownState}
}


class Run_happiness100:
    image = None
    image_jump = None
    def __init__(self):
        self.frame = 0
        self.goup = True
        self.angle = 0
        self.height = 0
        if self.image == None:
            self.image = load_image('resources\\run_happiness100.png')
        if self.image_jump == None:
            self.image_jump = load_image('resources\\run_happiness100_jump.png')
        self.event_que = []
        self.cur_state = RunUpState
        self.cur_state.enter(self, None)
        self.position = 'up'
        self.jump_sound = load_wav('resources\\jump.wav')
        self.jump_sound.set_volume(64)
        self.eat_sound = load_wav('resources\\eat.wav')
        self.eat_sound.set_volume(70)
        self.return_sound = load_wav('resources\\return.wav')
        self.return_sound.set_volume(70)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.check_Crush()
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                if self.cur_state == RunUpState or self.cur_state == RunDownState:
                    self.jump_sound.play()


    def collide(self, ch_x1, ch_x2, ch_y1, ch_y2, e_x1, e_x2, e_y1, e_y2):
        if ch_x2 < e_x1:
            return False
        if e_x2 < ch_x1:
            return False
        if e_y2 < ch_y1:
            return False
        if ch_y2 < e_y1:
            return False
        return True

    def check_Crush(self):
        ups = main_state.map.Cards_up + main_state.map.Boyfriends_up + main_state.map.Brooms_up + main_state.map.Marbles_up + main_state.map.Tray_up
        downs = main_state.map.Cards_down + main_state.map.Boyfriends_down + main_state.map.Brooms_down + main_state.map.Marbles_down + main_state.map.Tray_down
        main_state.is_crush = False
        for i in ups + downs:
            if i.x < 300 and i.x > 100:
                i.check = True
            else:
                i.check = False

        if self.cur_state == RunUpState or self.cur_state == JumpUpState:
            for i in ups:  # 충돌 계산 해줄곳 위
                if i.check == True:
                    if type(i) == P_map.Card:
                        main_state.is_crush = self.collide(170, 220, 360 + self.height - 10, 360 + self.height + 40,
                                           i.x - 25, i.x + 25, 310, 370)
                    if type(i) == P_map.Boyfriend:
                        main_state.is_crush = self.collide(170, 220, 360 + self.height - 10, 360 + self.height + 40,
                                           i.x - 25, i.x + 25, 310, 510)
                    if type(i) == P_map.Broom:
                        main_state.is_crush = self.collide(170, 220, 360 + self.height - 10, 360 + self.height + 40,
                                           i.x - 20, i.x + 20, 419, 610)
                    if type(i) == P_map.Marble:
                        if i.eated == False:
                            i.eated = self.collide(170, 220, 360 + self.height - 10, 360 + self.height + 40,
                                              i.x - 15, i.x + 15, 310, 350)
                            if i.eated == True:
                                self.eat_sound.play()
                                main_state.number.marble_number += 1
                    if type(i) == P_map.Tray:
                        if i.full == False:
                            i.full = self.collide(170, 220, 360 + self.height - 10, 360 + self.height + 40,
                                             i.x - 30, i.x + 30, 310, 400)
                            if i.full == True:
                                self.return_sound.play()
                                main_state.number.score += main_state.number.marble_number * 1000
                                main_state.number.marble_number = 0

        if self.cur_state == RunDownState or self.cur_state == JumpDownState:
            for i in downs:  # 충돌 계산 해줄곳 아래
                if i.check == True:
                    if type(i) == P_map.Card:
                        main_state.is_crush = self.collide(170, 220, 240 - self.height - 40, 240 - self.height + 10,
                                           i.x - 25, i.x + 25, 230, 290)
                    if type(i) == P_map.Boyfriend:
                        main_state.is_crush = self.collide(170, 220, 240 - self.height - 40, 240 - self.height + 10,
                                           i.x - 25, i.x + 25, 140, 290)
                    if type(i) == P_map.Broom:
                        main_state.is_crush = self.collide(170, 220, 240 - self.height - 40, 240 - self.height + 10,
                                           i.x - 20, i.x + 20, 0, 191)
                    if type(i) == P_map.Marble:
                        if i.eated == False:
                            i.eated = self.collide(170, 220, 240 - self.height - 40, 240 - self.height + 10,
                                              i.x - 15, i.x + 15, 250, 290)
                            if i.eated == True:
                                self.eat_sound.play()
                                main_state.number.marble_number += 1
                    if type(i) == P_map.Tray:
                        if i.full == False:
                            i.full = self.collide(170, 220, 240 - self.height - 40, 240 - self.height + 10,
                                             i.x - 30, i.x + 30, 200, 290)
                            if i.full == True:
                                self.return_sound.play()
                                main_state.number.score += main_state.number.marble_number * 1000
                                main_state.number.marble_number = 0

        if True == main_state.is_crush:
            game_framework.push_state(end_state)
from pico2d import *

from Cursor import Cursor
import main_state
import game_framework
import game_world

MOUSE_STUCK, MOUSE_UNSTUCK = range(2)

key_event_table = {
}

class IdleState:

    @staticmethod
    def enter(happy, event):
        pass

    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        happy.wait_frame = (happy.wait_frame + 1) % 4

    @staticmethod
    def draw(happy):
        happy.wait_image.clip_draw(happy.wait_frame * 300, 0, 300, 300, 300, 300)


class RunState:

    @staticmethod
    def enter(happy, event):
        pass

    @staticmethod
    def exit(happy, event):
        pass

    @staticmethod
    def do(happy):
        happy.run_frame = (happy.run_frame + 1) % 8

    @staticmethod
    def draw(happy):
        happy.run_image.clip_composite_draw(happy.run_frame*100, 0, 100, 100, 0, '', 300, 300, 300, 300)




next_state_table = {
    IdleState: {MOUSE_STUCK: RunState, MOUSE_UNSTUCK: IdleState},
    RunState: {MOUSE_STUCK: RunState, MOUSE_UNSTUCK: IdleState}
}

class Choose_happiness300:
    def __init__(self):
        self.run_frame = 0
        self.wait_frame = 0
        self.run_image = load_image('resources\\run_happiness100.png')
        self.wait_image = load_image('resources\\wait_happiness300.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
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
        elif event.type == SDL_MOUSEMOTION:
            if 150 < event.x < 450 and 100 < (700 - 1 - event.y) < 450:
                self.add_event(MOUSE_STUCK)
            else:
                self.add_event(MOUSE_UNSTUCK)
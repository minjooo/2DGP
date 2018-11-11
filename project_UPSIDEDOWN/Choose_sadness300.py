from pico2d import *

from Cursor import Cursor
import main_state
import game_framework
import game_world

MOUSE_STUCK, MOUSE_UNSTUCK, RIGHT_DOWN = range(3)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN
}

class IdleState:

    @staticmethod
    def enter(sad, event):
        pass

    @staticmethod
    def exit(sad, event):
        pass

    @staticmethod
    def do(sad):
        sad.wait_frame = (sad.wait_frame + 1) % 4

    @staticmethod
    def draw(sad):
        sad.wait_image.clip_draw(sad.wait_frame*300, 0, 300, 300, 650, 300)


class RunState:

    @staticmethod
    def enter(sad, event):
        pass

    @staticmethod
    def exit(sad, event):
        if event == RIGHT_DOWN:
            game_framework.push_state(main_state)


    @staticmethod
    def do(sad):
        sad.run_frame = (sad.run_frame + 1) % 8

    @staticmethod
    def draw(sad):
        sad.run_image.clip_composite_draw(sad.run_frame*100, 0, 100, 100, 0, '', 650, 300, 300, 300)




next_state_table = {
    IdleState: {MOUSE_STUCK: RunState, MOUSE_UNSTUCK: IdleState, RIGHT_DOWN: IdleState},
    RunState: {MOUSE_STUCK: RunState, MOUSE_UNSTUCK: IdleState, RIGHT_DOWN: RunState}
}

class Choose_sadness300:
    def __init__(self):
        self.run_frame = 0
        self.wait_frame = 0
        self.run_image = load_image('resources\\run_sadness100.png')
        self.wait_image = load_image('resources\\wait_sadness300.png')
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
            if 500 < event.x < 800 and 100 < (700 - 1 - event.y) < 450:
                self.add_event(MOUSE_STUCK)
            else:
                self.add_event(MOUSE_UNSTUCK)
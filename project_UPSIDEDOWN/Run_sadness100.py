from pico2d import *

SPACE, DELETE = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_DELETE): DELETE,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class RunUpState:

    @staticmethod
    def enter(sad, event):
        sad.frame = 0

    @staticmethod
    def exit(sad, event):
        pass

    @staticmethod
    def do(sad):
        sad.frame = (sad.frame + 1) % 8

    @staticmethod
    def draw(sad):
        sad.image.clip_draw(sad.frame * 100, 0, 100, 100, 200, 360)


class RunDownState:

    @staticmethod
    def enter(sad, event):
        sad.frame = 0

    @staticmethod
    def exit(sad, event):
        pass

    @staticmethod
    def do(sad):
        sad.frame = (sad.frame + 1) % 8

    @staticmethod
    def draw(sad):
        sad.image.clip_composite_draw(sad.frame * 100, 0, 100, 100, 0, 'v', 200, 240, 100, 100)


class JumpUpState:

    @staticmethod
    def enter(sad, event):
        sad.goup = True
        sad.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        sad.count_jump_speed = -1
        sad.height = 0

    @staticmethod
    def exit(sad, event):
        pass

    @staticmethod
    def do(sad):
        if sad.goup:
            sad.height += sad.jump_speed[sad.count_jump_speed]
            sad.count_jump_speed -= 1
            if sad.count_jump_speed == -8:
                sad.goup = False
        if sad.goup == False:
            sad.height -= sad.jump_speed[sad.count_jump_speed]
            sad.count_jump_speed += 1
            if sad.count_jump_speed == 1:
                sad.goup = True
                sad.jump = False
                sad.count_jump_speed = -1

    @staticmethod
    def draw(sad):
        sad.image_jump.draw(200, 360 + sad.height)


class JumpDownState:

    @staticmethod
    def enter(sad, event):
        sad.goup = True
        sad.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        sad.count_jump_speed = -1
        sad.height = 0

    @staticmethod
    def exit(sad, event):
        pass

    @staticmethod
    def do(sad):
        if sad.goup:
            sad.height += sad.jump_speed[sad.count_jump_speed]
            sad.count_jump_speed -= 1
            if sad.count_jump_speed == -8:
                sad.goup = False
        if sad.goup == False:
            sad.height -= sad.jump_speed[sad.count_jump_speed]
            sad.count_jump_speed += 1
            if sad.count_jump_speed == 1:
                sad.goup = True
                sad.jump = False
                sad.count_jump_speed = -1

    @staticmethod
    def draw(sad):
        sad.image_jump.clip_composite_draw(0, 0, 100, 100, 0, 'v', 200, 240 - sad.height, 100, 100)


next_state_table = {
    RunUpState: {SPACE: JumpUpState, DELETE: RunDownState},
    RunDownState: {SPACE: JumpDownState, DELETE: RunUpState},
    JumpUpState: {SPACE: JumpUpState, DELETE: JumpUpState},
    JumpDownState: {SPACE: JumpDownState, DELETE: JumpDownState}
}


class Run_sadness100:
    def __init__(self):
        self.image = load_image('resources\\run_sadness100.png')
        self.image_jump = load_image('resources\\run_sadness100_jump.png')
        self.event_que = []
        self.cur_state = RunUpState
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
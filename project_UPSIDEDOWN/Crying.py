from pico2d import *

import game_framework

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Crying:
    image = None
    def __init__(self):
        self.frame = 0
        if self.image == None:
            self.image = load_image('resources\\crying_sadness200.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    def draw(self):
        self.image.clip_draw(int(self.frame) * 264, 0, 264, 294, 280, 350)
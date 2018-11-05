from pico2d import *

import game_world


class Run_happiness300:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resources\\run_happiness100.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_composite_draw(self.frame*100, 0, 100, 100, 0, '', 300, 300, 300, 300)
from pico2d import *

import game_world


class Crying:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resources\\crying_sadness200.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 264, 0, 264, 294, 280, 350);
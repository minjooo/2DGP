from pico2d import *

import game_world



class Wait_sadness:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resources\\wait_sadness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, 650, 300)
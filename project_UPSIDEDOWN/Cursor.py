from pico2d import *

import game_world

class Cursor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('resources\\cursor80.png')

    def draw(self):
        self.image.draw(self.x, self.y)
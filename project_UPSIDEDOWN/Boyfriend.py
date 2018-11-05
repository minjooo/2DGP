from pico2d import *

import game_world

class Boyfriend:
    image = None
    def __init__(self):
        self.x = None
        self.check = False
        if Boyfriend.image == None:
            Boyfriend.image = load_image('resources\\imaginary_boyfriend100.png')
    def update(self):
        self.x -= 12

    def draw_up(self):
        self.image.draw(self.x, 410)
    def draw_down(self):
        self.image.clip_composite_draw(0, 0, 100, 200, 0, 'v', self.x, 190, 100, 200)



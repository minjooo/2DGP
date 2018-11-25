from pico2d import *


class Card:
    image = None
    def __init__(self):
        self.x = None
        self.check = False
        if Card.image == None:
            Card.image = load_image('resources\\card100.png')

    def update(self):
        self.x -= 12

    def draw_up(self):
        self.image.draw(self.x, 360)
    def draw_down(self):
        self.image.clip_composite_draw(0, 0, 100, 100, 0, 'v', self.x, 240, 100, 100)
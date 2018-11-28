from pico2d import *
import game_framework

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 300.0

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / 0.5

class Card:
    image = None
    def __init__(self):
        self.x = None
        self.check = False
        if Card.image == None:
            Card.image = load_image('resources\\card100.png')

    def update(self):
        #self.x -= 12
        self.x += (-RUN_SPEED_PPS) * game_framework.frame_time

    def draw_up(self):
        self.image.draw(self.x, 360)
    def draw_down(self):
        self.image.clip_composite_draw(0, 0, 100, 100, 0, 'v', self.x, 240, 100, 100)
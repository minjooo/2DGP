from pico2d import *
import game_framework

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 400.0

class Broom:
    image = None
    def __init__(self):
        self.x = None
        self.check = False
        if Broom.image == None:
            Broom.image = load_image('resources\\broom100.png')

    def update(self):
        #self.x -= 12
        self.x += (-RUN_SPEED_PPS) * game_framework.frame_time

    def draw_up(self):
        self.image.draw(self.x, 510)
    def draw_down(self):
        self.image.clip_composite_draw(0, 0, 100, 200, 0, 'v', self.x, 90, 100, 200)
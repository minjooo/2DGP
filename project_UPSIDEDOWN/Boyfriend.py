from pico2d import *
import game_framework

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 400.0

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / 0.5

class Boyfriend:
    image = None
    def __init__(self):
        self.x = None
        self.check = False
        if Boyfriend.image == None:
            Boyfriend.image = load_image('resources\\imaginary_boyfriend100.png')
    def update(self):
        #self.x -= 12
        self.x += (-RUN_SPEED_PPS) * game_framework.frame_time

    def draw_up(self):
        self.image.draw(self.x, 410)
    def draw_down(self):
        self.image.clip_composite_draw(0, 0, 100, 200, 0, 'v', self.x, 190, 100, 200)



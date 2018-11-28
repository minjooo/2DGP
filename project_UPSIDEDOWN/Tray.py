from pico2d import *
import game_framework

PIXEL_PER_CM = 10.0
RUN_SPEED_PPS = 400.0

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / 0.5


class Tray:
    empty_image = None
    full_image = None
    def __init__(self):
        self.x = None
        self.full = False
        self.check = False
        if Tray.empty_image == None:
            Tray.empty_image = load_image('resources\\tray100.png')
        if Tray.full_image == None:
            Tray.full_image = load_image('resources\\tray100_full.png')

    def update(self):
        #self.x -= 12
        self.x += (-RUN_SPEED_PPS) * game_framework.frame_time

    def draw_empty_up(self):
        self.empty_image.draw(self.x, 360)
    def draw_full_up(self):
        self.full_image.draw(self.x, 360)
    def draw_empty_down(self):
        self.empty_image.clip_composite_draw(0, 0, 100, 100, 0, 'v', self.x, 240, 100, 100)
    def draw_full_down(self):
        self.full_image.clip_composite_draw(0, 0, 100, 100, 0, 'v', self.x, 240, 100, 100)
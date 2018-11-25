import random
from pico2d import *

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 800-1), 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_bg(self, bg):
        self.bg=bg


    def set_center_object(self, boy):
        self.center_object = boy

    def draw(self):
        bx=self.x - self.bg.window_left
        by=self.y - self.bg.window_bottom
        self.image.draw(bx,by)
        draw_rectangle(*self.get_bb())

    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)


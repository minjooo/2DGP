from pico2d import *


class Marble:
    red_image = None
    blue_image = None
    purple_image = None
    yellow_image = None
    def __init__(self):
        self.x = None
        self.color = 0
        self.eated = False
        self.check = False
        if Marble.red_image == None:
            Marble.red_image = load_image('resources\\red_marble40.png')
        if Marble.blue_image == None:
            Marble.blue_image = load_image('resources\\blue_marble40.png')
        if Marble.purple_image == None:
            Marble.purple_image = load_image('resources\\purple_marble40.png')
        if Marble.yellow_image == None:
            Marble.yellow_image = load_image('resources\\yellow_marble40.png')

    def update(self):
        self.x -= 12

    def red_draw_up(self):
        self.red_image.draw(self.x, 330)
    def blue_draw_up(self):
        self.blue_image.draw(self.x, 330)
    def purple_draw_up(self):
        self.purple_image.draw(self.x, 330)
    def yellow_draw_up(self):
        self.yellow_image.draw(self.x, 330)

    def red_draw_down(self):
        self.red_image.clip_composite_draw(0, 0, 40, 40, 0, 'v', self.x, 270, 40, 40)
    def blue_draw_down(self):
        self.blue_image.clip_composite_draw(0, 0, 40, 40, 0, 'v', self.x, 270, 40, 40)
    def purple_draw_down(self):
        self.purple_image.clip_composite_draw(0, 0, 40, 40, 0, 'v', self.x, 270, 40, 40)
    def yellow_draw_down(self):
        self.yellow_image.clip_composite_draw(0, 0, 40, 40, 0, 'v', self.x, 270, 40, 40)
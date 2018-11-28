from pico2d import *


class Path:
    image = None
    def __init__(self):
        self.frame = 0
        if self.image == None:
            self.image = load_image('resources\\path1350_3.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 45, 0, 900, 20, 450, 300)

    def handle_event(self, event):
        pass
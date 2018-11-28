from pico2d import *


class BigReplay:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources/bigReplay.png')

    def draw(self):
        self.image.draw(450, 350)

    def handle_event(self, event):
        pass
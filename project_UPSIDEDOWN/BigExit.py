from pico2d import *


class BigExit:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\bigExit.png')

    def draw(self):
        self.image.draw(450, 350)

    def handle_event(self, event):
        pass
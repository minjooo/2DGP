from pico2d import *

import game_world

class Small_start:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\small_start.png')

    def draw(self):
        self.image.draw(450, 350)

    def handle_event(self, event):
        pass
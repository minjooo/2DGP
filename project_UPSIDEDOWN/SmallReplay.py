from pico2d import *

import game_world

class SmallReplay:
    def __init__(self):
        self.image = load_image('resources\\smallReplay.png')

    def draw(self):
        self.image.draw(450, 350)

    def handle_event(self, event):
        pass
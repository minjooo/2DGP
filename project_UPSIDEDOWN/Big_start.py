from pico2d import *

import game_world

class Big_start:
    def __init__(self):
        self.image = load_image('resources\\big_start.png')

    def draw(self):
        self.image.draw(450,350)

    def handle_event(self, event):
        pass
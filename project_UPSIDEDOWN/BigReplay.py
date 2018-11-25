from pico2d import *

import game_world


class BigReplay:
    def __init__(self):
        self.image = load_image('resources\\bigReplay.png')

    def draw(self):
        self.image.draw(450, 350)

    def handle_event(self, event):
        pass
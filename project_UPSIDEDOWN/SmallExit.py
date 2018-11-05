from pico2d import *

import game_world



class SmallExit:
    def __init__(self):
        self.image = load_image('resources\\smallExit.png')

    def draw(self):
        self.image.draw(450, 350)
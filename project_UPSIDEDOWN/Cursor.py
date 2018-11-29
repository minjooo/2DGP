from pico2d import *

import game_world



class Cursor:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        if self.image == None:
            self.image = load_image('resources\\cursor80.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, 700 - 1 - event.y


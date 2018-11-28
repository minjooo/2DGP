from pico2d import *


class Numbers:
    image = None
    def __init__(self):
        self.score = 0
        self.marble_number = 0
        self.font = load_font('resources/OCRAStd.otf',45)


    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        self.font.draw(200, 649, '%d'%self.score, (0,76,99))
        self.font.draw(650, 649, '%d'%self.marble_number, (0,76,99))


from pico2d import *


class Score:
    font = None
    def __init__(self):
        self.score = 0
        if self.font == None:
            self.font = load_font('resources\\OCRAStd.otf', 100)

    def draw(self):
        self.font.draw(500, 330, '%d' % self.score, (255, 110, 0))

    def update(self):
        pass

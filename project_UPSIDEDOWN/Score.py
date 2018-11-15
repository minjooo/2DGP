from pico2d import *

import game_world

class Score:
    def __init__(self):
        self.score = 0
        self.font = load_font('resources\\OCRAStd.otf',100)


    def draw(self):
        self.font.draw(500, 330, '%d000'%self.score, (255,110,0))

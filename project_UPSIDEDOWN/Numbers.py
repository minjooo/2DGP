from pico2d import *

import game_world

class Numbers:
    image = None
    def __init__(self):
        self.total_score = 0
        self.score = 0
        self.total_marble_number = 0
        self.marble_number = 0
        self.score100 = 0
        self.score10 = 0
        self.score1 = 0
        self.marble10 = 0
        self.marble1 = 0
        if Numbers.image == None:
            Numbers.image = load_image('resources\\number.png')

    def update_score(self):
        if self.score >= 100:
            self.score100 = 0
            while self.score >= 100:
                self.score -= 100
                self.score100 += 1
        if self.score >= 10:
            self.score10 = 0
            while self.score >= 10:
                self.score -=10
                self.score10 += 1
        self.score1 = self.score
        self.score = 0
    def update_marble(self):
        if self.marble_number >= 10:
            self.marble10 = 0
            while self.marble_number >= 10:
                self.marble_number -= 10
                self.marble10 += 1
        self.marble1 = self.marble_number
        self.marble_number = 0

    def draw_score(self):
        if self.score100 != 0:
            self.image.clip_draw(self.score100*25,0,25,50,175,649)
        if self.score10 != 0 or (self.score10 == 0 and self.score100 != 0):
            self.image.clip_draw(self.score10*25,0,25,50,200,649)
        if self.total_score != 0:
            self.image.clip_draw(0, 0, 25, 50, 250, 649)
            self.image.clip_draw(0, 0, 25, 50, 275, 649)
            self.image.clip_draw(0, 0, 25, 50, 300, 649)
        self.image.clip_draw(self.score1*25, 0, 25, 50, 225, 649)
    def draw_marble_num(self):
        if self.marble10 != 0:
            self.image.clip_draw(self.marble10*25,0,25,50,670,649)
        self.image.clip_draw(self.marble1 * 25, 0, 25, 50, 695, 649)


from pico2d import *

import game_world

class Score:
    image = None
    def __init__(self):
        self.score100 = 0
        self.score10 = 0
        self.score1 = 0
        self.score = 0
        if Score.image == None:
            Score.image = load_image('resources\\orangeNumber.png')


    def draw(self):
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
        if self.score100 != 0:
            self.image.clip_draw(self.score100 * 50, 0, 50, 100, 500, 300)
        if self.score10 != 0 or (self.score10 == 0 and self.score100 != 0):
            self.image.clip_draw(self.score10 * 50, 0, 50, 100, 550, 300)
        if self.score != 0:
            self.image.clip_draw(0, 0, 50, 100, 650, 300)
            self.image.clip_draw(0, 0, 50, 100, 700, 300)
            self.image.clip_draw(0, 0, 50, 100, 750, 300)
        self.image.clip_draw(self.score1 * 50, 0, 50, 100, 600, 300)

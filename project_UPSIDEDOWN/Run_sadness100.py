from pico2d import *

import game_world

class Run_sadness100:
    def __init__(self):
        self.point = 0
        self.UP = True
        self.jump = False
        self.goup = True
        self.jump_speed = [n for n in range(0, 35 + 1) if n % 5 == 0]
        self.count_jump_speed = -1
        self.height = 0
        self.frame = 0
        self.image = load_image('resources\\run_sadness100.png')
        self.image_jump = load_image('resources\\run_sadness100_jump.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.height += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -8:
                    self.goup = False
            if self.goup == False:
                self.height -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, 200, 360 + self.height)
    def draw_down(self):
        self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, 'v', 200, 240, 100, 100)
    def draw_jump_up(self):
        self.image_jump.draw(200, 360 + self.height)
    def draw_jump_down(self):
        self.image_jump.clip_composite_draw(0, 0, 100, 100, 0, 'v', 200, 240 - self.height, 100, 100)



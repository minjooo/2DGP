from pico2d import *
import random

from Card import Card
from Broom import Broom
from Boyfriend import Boyfriend
from Marble import Marble
from Tray import Tray


class Map:
    def __init__(self):
        self.Cards_up = []
        self.Boyfriends_up = []
        self.Brooms_up = []
        self.Marbles_up = []
        self.Cards_down = []
        self.Boyfriends_down = []
        self.Brooms_down = []
        self.Marbles_down = []
        self.Tray_up = []
        self.Tray_down = []
        self.load()


    def load(self):
        f = open('resources\\map.txt', 'r')
        u = f.readline()
        d = f.readline()
        up = u.split()
        for i in range(0, len(up)):
            up[i] = int(up[i])
        down = d.split()
        for i in range(0, len(down)):
            down[i] = int(down[i])
        f.close()

        for i in range(0, len(up)):  # up 훑겠다
            n = up[i]
            if n == 0:
                pass
            elif n == 1:  # 카드
                self.Cards_up.append(Card())
                self.Cards_up[-1].x = i * 100
            elif n == 2:  # 남친
                self.Boyfriends_up.append(Boyfriend())
                self.Boyfriends_up[-1].x = i * 100
            elif n == 3:  # 빗자루
                self.Brooms_up.append(Broom())
                self.Brooms_up[-1].x = i * 100
            elif n == 4:  # 구슬하고싶은데
                self.Marbles_up.append(Marble())
                self.Marbles_up[-1].x = i * 100
                self.Marbles_up[-1].color = random.randint(1, 4 + 1)
            elif n == 5:  # 트레이다
                self.Tray_up.append(Tray())
                self.Tray_up[-1].x = i * 100

        for i in range(0, len(down)):  # down 훑겠다
            n = down[i]
            if n == 0:
                pass
            elif n == 1:  # 카드
                self.Cards_down.append(Card())
                self.Cards_down[-1].x = i * 100
            elif n == 2:  # 남친
                self.Boyfriends_down.append(Boyfriend())
                self.Boyfriends_down[-1].x = i * 100
            elif n == 3:  # 빗자루
                self.Brooms_down.append(Broom())
                self.Brooms_down[-1].x = i * 100
            elif n == 4:  # 구슬하고싶은데
                self.Marbles_down.append(Marble())
                self.Marbles_down[-1].x = i * 100
                self.Marbles_down[-1].color = random.randint(1, 4 + 1)
            elif n == 5:  # 트레이다
                self.Tray_down.append(Tray())
                self.Tray_down[-1].x = i * 100


    def add_event(self, event):
        pass

    def update(self):
        for i in self.Cards_up + self.Boyfriends_up + self.Brooms_up + self.Cards_down + self.Boyfriends_down + self.Brooms_down + self.Marbles_up + self.Marbles_down + self.Tray_up + self.Tray_down:
            i.update()

    def draw(self):
        for i in self.Cards_up + self.Boyfriends_up + self.Brooms_up:
            i.draw_up()
        for i in self.Cards_down + self.Boyfriends_down + self.Brooms_down:
            i.draw_down()
        for i in self.Marbles_up:
            if i.eated == False:
                if i.color == 1:
                    i.red_draw_up()
                elif i.color == 2:
                    i.blue_draw_up()
                elif i.color == 3:
                    i.yellow_draw_up()
                elif i.color == 4:
                    i.purple_draw_up()
        for i in self.Marbles_down:
            if i.eated == False:
                if i.color == 1:
                    i.red_draw_down()
                elif i.color == 2:
                    i.blue_draw_down()
                elif i.color == 3:
                    i.yellow_draw_down()
                elif i.color == 4:
                    i.purple_draw_down()
        for i in self.Tray_up:
            if i.full == False:
                i.draw_empty_up()
            else:
                i.draw_full_up()
        for i in self.Tray_down:
            if i.full == False:
                i.draw_empty_down()
            else:
                i.draw_full_down()

    def handle_event(self, event):
        pass


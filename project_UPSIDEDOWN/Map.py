import game_world
from pico2d import *
import random

from Card import Card
from Broom import Broom
from Boyfriend import Boyfriend
from Marble import Marble
from Tray import Tray

name = 'map_state'
image = None

class Map:
    def __init__(self):
        global up, down, Cards_up, Boyfriends_up, Brooms_up, Marbles_up, Tray_up, Tray_down, Cards_down, Boyfriends_down, Brooms_down, Marbles_down, is_crush
        Cards_up = []
        Boyfriends_up = []
        Brooms_up = []
        Marbles_up = []
        Cards_down = []
        Boyfriends_down = []
        Brooms_down = []
        Marbles_down = []
        Tray_up = []
        Tray_down = []

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

        for i in range(0, len(up)): # up 훑겠다
            n = up[i]
            if n == 0:
                pass
            elif n == 1: # 카드
                Cards_up.append(Card())
                Cards_up[-1].x = i * 100
            elif n == 2: # 남친
                Boyfriends_up.append(Boyfriend())
                Boyfriends_up[-1].x = i * 100
            elif n == 3: # 빗자루
                Brooms_up.append(Broom())
                Brooms_up[-1].x = i * 100
            elif n == 4: #구슬하고싶은데
                Marbles_up.append(Marble())
                Marbles_up[-1].x = i * 100
                Marbles_up[-1].color = random.randint(1, 4 + 1)
            elif n == 5: # 트레이다
                Tray_up.append(Tray())
                Tray_up[-1].x = i * 100

        for i in range(0, len(down)): # down 훑겠다
            n = down[i]
            if n == 0:
                pass
            elif n == 1: # 카드
                Cards_down.append(Card())
                Cards_down[-1].x = i * 100
            elif n == 2: # 남친
                Boyfriends_down.append(Boyfriend())
                Boyfriends_down[-1].x = i * 100
            elif n == 3: # 빗자루
                Brooms_down.append(Broom())
                Brooms_down[-1].x = i * 100
            elif n == 4: #구슬하고싶은데
                Marbles_down.append(Marble())
                Marbles_down[-1].x = i * 100
                Marbles_down[-1].color = random.randint(1, 4 + 1)
            elif n == 5: # 트레이다
                Tray_down.append(Tray())
                Tray_down[-1].x = i * 100


    def add_event(self, event):
        pass

    def update(self):
        for i in Cards_up + Boyfriends_up + Brooms_up + Cards_down + Boyfriends_down + Brooms_down + Marbles_up + Marbles_down + Tray_up + Tray_down:
            i.update()

    def draw(self):
        for i in Cards_up + Boyfriends_up + Brooms_up:
            i.draw_up()
        for i in Cards_down + Boyfriends_down + Brooms_down:
            i.draw_down()
        for i in Marbles_up:
            if i.eated == False:
                if i.color == 1:
                    i.red_draw_up()
                elif i.color == 2:
                    i.blue_draw_up()
                elif i.color == 3:
                    i.yellow_draw_up()
                elif i.color == 4:
                    i.purple_draw_up()
        for i in Marbles_down:
            if i.eated == False:
                if i.color == 1:
                    i.red_draw_down()
                elif i.color == 2:
                    i.blue_draw_down()
                elif i.color == 3:
                    i.yellow_draw_down()
                elif i.color == 4:
                    i.purple_draw_down()
        for i in Tray_up:
            if i.full == False:
                i.draw_empty_up()
            else:
                i.draw_full_up()
        for i in Tray_down:
            if i.full == False:
                i.draw_empty_down()
            else:
                i.draw_full_down()

    def handle_event(self, event):
        pass


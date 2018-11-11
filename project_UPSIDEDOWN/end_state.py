import game_framework
import main_state
import title_state
import choose_state
from pico2d import *

import game_world

from Cursor import Cursor
from Score import Score
from Crying import Crying
from SmallExit import SmallExit
from SmallReplay import SmallReplay
from BigReplay import BigReplay
from BigExit import BigExit

name = 'end_state'
image = None


class Ending:
    def __init__(self):
        self.image = load_image('resources\\gameover2.png')

    def draw(self):
        self.image.draw(450, 350)


def enter():
    global end, smallReplay, smallExit, bigReplay, bigExit, chooseExit, chooseReplay, cursor, crying, score
    end = Ending()
    smallReplay = SmallReplay()
    smallExit = SmallExit()
    bigReplay = BigReplay()
    bigExit = BigExit()
    chooseExit = False
    chooseReplay = False
    cursor = Cursor()
    crying = Crying()
    score = Score()
    score.score = main_state.number.total_score

def exit():
    global end, smallReplay, smallExit, bigReplay, bigExit, chooseExit, chooseReplay, cursor, crying, score
    del(end)
    del(smallExit)
    del(smallReplay)
    del(bigExit)
    del(bigReplay)
    del(chooseExit)
    del(chooseReplay)
    del(cursor)
    del(crying)
    del(score)

def handle_events():
    global chooseReplay
    global chooseExit
    global cursor
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 700 - 1 - event.y
            if 150 < event.x < 450 and 50 < (700 - 1 - event.y) < 150:
                chooseReplay = True
            else:
                chooseReplay = False
            if 600 < event.x < 800 and 50 < (700 - 1 - event.y) < 150:
                chooseExit = True
            else:
                chooseExit = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if chooseReplay:
                game_world.clear()
                game_framework.change_state(choose_state)
                return
            elif chooseExit:
                game_framework.quit()
                return
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
                return

def update():
    crying.update()
    delay(0.05)

def draw():
    clear_canvas()
    end.draw()
    crying.draw()
    if chooseReplay == True:
        bigReplay.draw()
    else:
        smallReplay.draw()
    if chooseExit == True:
        bigExit.draw()
    else:
        smallExit.draw()
    score.draw()
    cursor.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
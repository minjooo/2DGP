import game_framework
import main_state
import title_state
import choose_state
from pico2d import *

name = 'end_state'
image = None

class Ending:
    def __init__(self):
        self.image = load_image('gameover.png')

    def draw(self):
        self.image.draw(450, 350)


class Cursor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('cursor80.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class SmallReplay:
    def __init__(self):
        self.image = load_image('smallReplay.png')

    def draw(self):
        self.image.draw(450, 350)

class BigReplay:
    def __init__(self):
        self.image = load_image('bigReplay.png')

    def draw(self):
        self.image.draw(450, 350)


class SmallExit:
    def __init__(self):
        self.image = load_image('smallExit.png')

    def draw(self):
        self.image.draw(450, 350)


class BigExit:
    def __init__(self):
        self.image = load_image('bigExit.png')

    def draw(self):
        self.image.draw(450, 350)

def enter():
    global end, smallReplay, smallExit, bigReplay, bigExit, chooseExit, chooseReplay, cursor
    end = Ending()
    smallReplay = SmallReplay()
    smallExit = SmallExit()
    bigReplay = BigReplay()
    bigExit = BigExit()
    chooseExit = False
    chooseReplay = False
    cursor = Cursor()

def exit():
    global end, smallReplay, smallExit, bigReplay, bigExit, chooseExit, chooseReplay, cursor
    del(end)
    del(smallExit)
    del(smallReplay)
    del(bigExit)
    del(bigReplay)
    del(chooseExit)
    del(chooseReplay)
    del(cursor)

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
            if 150 < event.x < 450 and 0 < (700 - 1 - event.y) < 100:
                chooseReplay = True
            else:
                chooseReplay = False
            if 600 < event.x < 800 and 0 < (700 - 1 - event.y) < 100:
                chooseExit = True
            else:
                chooseExit = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if chooseReplay:
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
    pass

def draw():
    clear_canvas()
    end.draw()
    if chooseReplay == True:
        bigReplay.draw()
    else:
        smallReplay.draw()
    if chooseExit == True:
        bigExit.draw()
    else:
        smallExit.draw()
    cursor.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
import game_framework
import title_state
import main_state
from pico2d import *

name = 'choose_state'
image = None

class Cursor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('cursor80.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Choose_Background:
    def __init__(self):
        self.image = load_image('choose.png')
    def draw(self):
        self.image.draw(450, 350)

class Wait_happiness:
    def __init__(self):
        self.frame = 0
        self.image = load_image('wait_happiness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, 300, 300)

class Wait_sadness:
    def __init__(self):
        self.frame = 0
        self.image = load_image('wait_sadness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, 650, 300)

class Run_happiness300:
    def __init__(self):
        self.frame = 0
        self.image = load_image('run_happiness100.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_composite_draw(self.frame*100, 0, 100, 100, 0, '', 300, 300, 300, 300)

class Run_sadness300:
    def __init__(self):
        self.frame = 2
        self.image = load_image('run_sadness100.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_composite_draw(self.frame*100, 0, 100, 100, 0, '', 650, 300, 300, 300)


def enter():
    global cursor, choose_happy, choose_sad, choose_bg, wait_sad, wait_happy, run_sad, run_happy, selected_character
    cursor = Cursor()
    choose_happy = False
    choose_sad = False
    choose_bg = Choose_Background()
    wait_sad = Wait_sadness()
    wait_happy = Wait_happiness()
    run_sad = Run_sadness300()
    run_happy = Run_happiness300()
    selected_character = 'none'


def exit():
    global cursor, choose_happy, choose_sad, choose_bg, wait_sad, wait_happy, run_sad, run_happy, selected_character
    del(cursor)
    del(choose_happy)
    del(choose_sad)
    del(choose_bg)
    del(wait_sad)
    del(wait_happy)
    del(run_sad)
    del(run_happy)
    del(selected_character)

def handle_events():
    global cursor
    global choose_happy
    global choose_sad
    global selected_character
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 700 - 1 - event.y
            if 150 < event.x < 450 and 100 < (700 - 1 - event.y) < 450:
                choose_happy = True
            else:
                choose_happy = False
            if 500 < event.x < 800 and 100 < (700 - 1 - event.y) < 450:
                choose_sad = True
            else:
                choose_sad = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if choose_happy:
                selected_character = 'happy'
                game_framework.push_state(main_state)
                return
            elif choose_sad:
                selected_character = 'sad'
                game_framework.push_state(main_state)
                return
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
                return

def update():
    wait_happy.update()
    wait_sad.update()
    run_happy.update()
    run_sad.update()

def draw():
    clear_canvas()
    choose_bg.draw()
    if choose_happy:
        run_happy.draw()
    else:
        wait_happy.draw()
    if choose_sad:
        run_sad.draw()
    else:
        wait_sad.draw()
    cursor.draw()
    update_canvas()
    delay(0.05)

def pause():
    pass

def resume():
    pass


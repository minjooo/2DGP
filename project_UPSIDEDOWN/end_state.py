import game_framework
import main_state
from pico2d import *

name = 'end_state'
image = None

class Pause:
    def __init__(self):
        self.image = load_image('pause360.png')

    def draw(self):
        self.image.draw(450,350)

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_p:
                game_framework.pop_state()

def update():
    pass

def draw():
    clear_canvas()
    main_state.main_bg.draw()
    main_state.path.draw()
    for i in main_state.Cards_up + main_state.Boyfriends_up + main_state.Brooms_up:
        i.draw_up()
    for i in main_state.Cards_down + main_state.Boyfriends_down + main_state.Brooms_down:
        i.draw_down()
    for i in main_state.Marbles_up:
        if i.color == 1:
            i.red_draw_up()
        elif i.color == 2:
            i.blue_draw_up()
        elif i.color == 3:
            i.yellow_draw_up()
        elif i.color == 4:
            i.purple_draw_up()
    for i in main_state.Marbles_down:
        if i.color == 1:
            i.red_draw_down()
        elif i.color == 2:
            i.blue_draw_down()
        elif i.color == 3:
            i.yellow_draw_down()
        elif i.color == 4:
            i.purple_draw_down()
    for i in main_state.Tray_up:
        i.draw_empty_up()
    for i in main_state.Tray_down:
        i.draw_empty_down()

    main_state.number.draw_score()
    main_state.number.draw_marble_num()
    if choose_state.selected_character == 'sad':
        if main_state.run_sad.jump:
            if main_state.run_sad.UP:
                main_state.run_sad.draw_jump_up()
            else:
                main_state.run_sad.draw_jump_down()
        else:
            if main_state.run_sad.UP:
                main_state.run_sad.draw_up()
            elif main_state.run_sad.UP == False:
                main_state.run_sad.draw_down()
    elif choose_state.selected_character == 'happy':
        if main_state.run_happy.jump:
            if main_state.run_happy.UP:
                main_state.run_happy.draw_jump_up()
            else:
                main_state.run_happy.draw_jump_down()
        else:
            if main_state.run_happy.UP:
                main_state.run_happy.draw_up()
            elif main_state.run_happy.UP == False:
                main_state.run_happy.draw_down()
    pause.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
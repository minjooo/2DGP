from pico2d import *

# 캔버스 크기 900*700
#게임 오브잭트 클래스 자리
class Cursor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('cursor80.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Start_Background:
    def __init__(self):
        self.image = load_image('start_image.png')

    def draw(self):
        self.image.draw(450,350)

class Big_start:
    def __init__(self):
        self.image = load_image('big_start.png')

    def draw(self):
        self.image.draw(450,350)

class Small_start:
    def __init__(self):
        self.image = load_image('small_start.png')

    def draw(self):
        self.image.draw(450, 350)

def handle_events():
    global running
    global starting
    global choosing
    global Big_cursor
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            starting = False
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 700 - 1 - event.y
            if 415 < event.x < 695 and 150 < (700 - 1 - event.y) < 260:
                Big_cursor = True
            else:
                Big_cursor = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if Big_cursor == True:
                starting = False
                choosing = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            starting = False

# 초키화 자리
open_canvas(900, 700)
startImage = Start_Background()
smallStart = Small_start()
bigStart = Big_start()
cursor = Cursor()
hide_cursor()

running = False
starting = True
choosing = False
Big_cursor = False

# 메인 루프 자리
while starting:
    handle_events()

    clear_canvas()
    startImage.draw()
    if Big_cursor == True:
        bigStart.draw()
    else:
        smallStart.draw()
    cursor.draw()
    update_canvas()

while choosing:
    close_canvas()
    pass

# 코드 종료 자리
close_canvas()
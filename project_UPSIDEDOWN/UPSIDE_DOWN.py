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

class Choose_Background:
    def __init__(self):
        self.image = load_image('choose.png')

    def draw(self):
        self.image.draw(450, 350)

class Wait_happiness:
    def __init__(self):
        self.x, self.y = 300, 300
        self.frame = 0
        self.image = load_image('wait_happiness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, self.x,self.y)

class Wait_sadness:
    def __init__(self):
        self.x, self.y = 650, 300
        self.frame = 0
        self.image = load_image('wait_sadness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, self.x, self.y)

class Run_happiness300:
    def __init__(self):
        self.x, self.y =300, 300
        self.frame = 0
        self.image = load_image('run_happiness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, self.x,self.y)

class Run_sadness300:
    def __init__(self):
        self.x, self.y = 650, 300
        self.frame = 2
        self.image = load_image('run_sadness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 300, 300, self.x, self.y)

def handle_events():
    global running
    global starting
    global choosing
    global Big_cursor
    global Big_happy
    global Big_sad
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            starting = False
            choosing = False
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 700 - 1 - event.y
            if starting:
                if 415 < event.x < 695 and 150 < (700 - 1 - event.y) < 260:
                    Big_cursor = True
                else:
                    Big_cursor = False
            elif choosing:
                if 150 < event.x <450 and 100 < (700 - 1 - event.y) < 450:
                    Big_happy = True
                else:
                    Big_happy = False
                if 500 < event.x < 800 and 100 < (700 - 1 - event.y) < 450:
                    Big_sad = True
                else:
                    Big_sad = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if Big_cursor == True:
                starting = False
                choosing = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            starting = False
            choosing = False

# 초키화 자리
open_canvas(900, 700)
startImage = Start_Background()
smallStart = Small_start()
bigStart = Big_start()
cursor = Cursor()
chooseImage = Choose_Background()
wait_happy = Wait_happiness()
wait_sad = Wait_sadness()
run_happy300 = Run_happiness300()
run_sad300 = Run_sadness300()
hide_cursor()

running = False
starting = True
choosing = False
Big_cursor = False # start글씨 크게 나오게하는 bool값
Big_happy = False
Big_sad = False

# 메인 루프 자리
while starting:
    handle_events()

    clear_canvas()
    startImage.draw()
    if Big_cursor:
        bigStart.draw()
    else:
        smallStart.draw()
    cursor.draw()
    update_canvas()

while choosing:
    handle_events()

    wait_happy.update()
    wait_sad.update()
    run_happy300.update()
    run_sad300.update()

    clear_canvas()
    chooseImage.draw()
    if Big_happy:
        run_happy300.draw()
    else:
        wait_happy.draw()
    if Big_sad:
        run_sad300.draw()
    else:
        wait_sad.draw()
    cursor.draw()
    update_canvas()

    delay(0.05)

# 코드 종료 자리
close_canvas()
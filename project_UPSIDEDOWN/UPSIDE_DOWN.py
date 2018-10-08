from pico2d import *

# 캔버스 크기 900*700
#게임 오브잭트 클래스 자리
class Start_Background:
    def __init__(self):
        self.image = load_image('start_image.png')

    def draw(self):
        self.image.draw(450,350)

class Big_start:
    def __init__(self):
        self.image = load_image('big_start.png')

    def draw(self):
        self.image.draw(455,340)

class Small_start:
    def __init__(self):
        self.image = load_image('small_start.png')

    def draw(self):
        self.image.draw(455, 340)

def handle_events():
    global running
    global starting
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            starting = False
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            starting = False

# 초키화 자리
open_canvas(900,700)
startImage = Start_Background()
smallStart = Small_start()
bigStart = Big_start()

running = False
starting = True

# 메인 루프 자리
while starting:
    handle_events()

    clear_canvas()
    startImage.draw()
    smallStart.draw()
    update_canvas()

# 코드 종료 자리
close_canvas()
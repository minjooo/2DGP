from pico2d import *

# 캔버스 크기 900*700
#게임 오브잭트 클래스 자리



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 초키화 자리
open_canvas(900,700)

running = False

# 메인 루프 자리

# 코드 종료 자리
close_canvas()
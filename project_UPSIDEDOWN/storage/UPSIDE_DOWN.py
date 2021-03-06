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
        self.image = load_image('run_happiness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*300, 0, 300, 300, 300, 300)

class Run_sadness300:
    def __init__(self):
        self.frame = 2
        self.image = load_image('run_sadness300.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 300, 300, 650, 300)

class Running_Background:
    def __init__(self):
        self.image = load_image('running_BG.png')

    def draw(self):
        self.image.draw(450,350)

class Run_happiness100:
    def __init__(self):
        self.UP = True
        self.hight = 0
        self.jump = False
        self.goup = True # 점프할 때 올라가는지 내려가는지 구분
        self.jump_speed = [n for n in range(0, 20 + 1) if n % 2 == 0]
        self.count_jump_speed = -1
        self.frame = 0
        self.image_up = load_image('run_happiness100.png')
        self.image_down = load_image('run_happiness100_down.png')
        self.image_jump_up = load_image('run_happiness100_jump.png')
        self.image_jump_down = load_image('run_happiness100_jump_down.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.hight += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -11:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100, 0, 100, 100, 200, 360)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100, 0, 100, 100, 200, 240)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.hight)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.hight)


class Run_sadness100:
    def __init__(self):
        self.UP = True
        self.jump = False
        self.goup = True
        self.jump_speed = [n for n in range(0, 20 + 1) if n % 2 == 0]
        self.count_jump_speed = -1
        self.hight = 0
        self.frame = 0
        self.image_up = load_image('run_sadness100.png')
        self.image_down = load_image('run_sadness100_down.png')
        self.image_jump_up = load_image('run_sadness100_jump.png')
        self.image_jump_down = load_image('run_sadness100_jump_down.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.jump:
            if self.goup:
                self.hight += self.jump_speed[self.count_jump_speed]
                self.count_jump_speed -= 1
                if self.count_jump_speed == -11:
                    self.goup = False
            if self.goup == False:
                self.hight -= self.jump_speed[self.count_jump_speed]
                self.count_jump_speed += 1
                if self.count_jump_speed == 1:
                    self.goup = True
                    self.jump = False
                    self.count_jump_speed = -1

    def draw_up(self):
        self.image_up.clip_draw(self.frame * 100 , 0, 100, 100, 200, 360)
    def draw_down(self):
        self.image_down.clip_draw(self.frame * 100 , 0, 100, 100, 200, 240)
    def draw_jump_up(self):
        self.image_jump_up.draw(200, 360 + self.hight)
    def draw_jump_down(self):
        self.image_jump_down.draw(200, 240 - self.hight)


class Path:
    def __init__(self):
        self.x ,self.y = 450, 300
        self.frame = 0
        self.image = load_image('path1350_3.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 45, 0, 900, 20, self.x, self.y)

def handle_events():
    global running
    global starting
    global choosing
    global Big_cursor
    global Big_happy
    global Big_sad
    global selected_character
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
            if Big_happy:
                choosing = False
                running = True
                selected_character = 'happy'
            if Big_sad:
                choosing = False
                running = True
                selected_character = 'sad'
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DELETE and run_sad100.jump == False and run_happy100.jump == False:
                if run_happy100.UP or run_sad100.UP:
                    run_happy100.UP = False
                    run_sad100.UP = False
                elif run_happy100.UP == False or run_sad100.UP == False:
                    run_happy100.UP = True
                    run_sad100.UP = True
            elif event.key == SDLK_j:
                run_happy100.jump = True
                run_sad100.jump = True
            elif event.key == SDLK_ESCAPE:
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
selected_character = 'none' #선택된 캐릭터 이름 저장
runningImage = Running_Background()
path = Path()
run_happy100 = Run_happiness100()
run_sad100 = Run_sadness100()
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

    delay(0.07)

while running:
    handle_events()

    path.update()
    run_happy100.update()
    run_sad100.update()

    clear_canvas()
    runningImage.draw()
    path.draw()
    if selected_character == 'happy':
        if run_happy100.jump:
            if run_happy100.UP:
                run_happy100.draw_jump_up()
            else:
                run_happy100.draw_jump_down()
        else:
            if run_happy100.UP:
                run_happy100.draw_up()
            elif run_happy100.UP == False:
                run_happy100.draw_down()
    elif selected_character == 'sad':
        if run_sad100.jump:
            if run_sad100.UP:
                run_sad100.draw_jump_up()
            else:
                run_sad100.draw_jump_down()
        else:
            if run_sad100.UP:
                run_sad100.draw_up()
            elif run_sad100.UP == False:
                run_sad100.draw_down()
    update_canvas()

    delay(0.05)

# 코드 종료 자리
close_canvas()

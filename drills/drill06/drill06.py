from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global hand_x, hand_y
    global x,y
    global gox,goy
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y=event.x,KPU_HEIGHT - 1 -event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            count=0
            gox=x / 50
            goy=(KPU_HEIGHT - 1 -event.y+50) / 50
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
hand_x,hand_y=0,0
gox,goy=0,0
count=0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8
    if count < 100:
        count +=2
        x += gox
        y += goy
    delay(0.02)
    handle_events()

close_canvas()





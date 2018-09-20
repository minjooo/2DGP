from pico2d import *


def handle_events():
    global running
    global dir
    global last_position

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                last_position = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                last_position = -1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
last_position =0

while running:
    clear_canvas()
    if dir == 1:
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    elif dir == -1:
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    else:
        if last_position == 1:
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 300, 100, 100, x, 90)
        else:
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 200, 100, 100, x, 90)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()


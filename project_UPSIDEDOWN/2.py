from pico2d import*

happy = load_image('run_happiness100.png')
open_canvas()

frame=0
running=True

while running:
    clear_canvas()
    happy.clip_draw(frame * 100, 0, 100, 100, 180, 365)
    update_canvas()
    frame = (frame + 1)%8
    delay(0.05)

close_canvas()

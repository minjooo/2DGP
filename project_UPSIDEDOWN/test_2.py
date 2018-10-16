from pico2d import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

f = open('map.txt', 'r')
u = f.readline()
d = f.readline()
up = u.split()
for i in range(0, len(up)):
    up[i] = int(up[i])
down = d.split()
for i in range(0, len(down)):
    down[i] = int(down[i])
f.close()

print(up)
print(down)
type(up)

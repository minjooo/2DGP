import game_framework
import pico2d

import title_state

pico2d.open_canvas(900, 700, sync = True)
game_framework.run(title_state)
pico2d.close_canvas()

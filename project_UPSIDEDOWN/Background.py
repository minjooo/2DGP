from pico2d import *


class StartBackground:
    image = None
    bgm = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\start_image.png')
        if self.bgm == None:
            self.bgm = load_music('resources\\title.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass


class ChooseBackground:
    image = None
    bgm = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\choose.png')
        if self.bgm == None:
            self.bgm = load_music('resources\\choose.wav')
        self.bgm.set_volume(70)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass

class RunningBackground:
    image = None
    bgm = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\running_BG_bar.png')
        if self.bgm == None:
            self.bgm = load_music('resources\\main.wav')
        self.bgm.set_volume(65)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass


class EndingBackground:
    image = None
    bgm = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('resources/gameover2.png')
        if self.bgm == None:
            self.bgm = load_music('resources/end.wav')
        self.bgm.set_volume(70)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass

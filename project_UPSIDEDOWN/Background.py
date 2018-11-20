from pico2d import *


class StartBackground:

    def __init__(self):
        self.image = load_image('resources\\start_image.png')

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass


class ChooseBackground:

    def __init__(self):
        self.image = load_image('resources\\choose.png')

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass

class RunningBackground:

    def __init__(self):
        self.image = load_image('resources\\running_BG_bar.png')

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass


class EndingBackground:
    def __init__(self):
        self.image = load_image('resources\\gameover2.png')

    def draw(self):
        self.image.draw(450, 350)

    def update(self):
        pass

    def handle_event(self, event):
        pass

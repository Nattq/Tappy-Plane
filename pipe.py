import arcade
from constants import *

class Pipe(arcade.Sprite):
    def __init__(self, image,scale=.5):
        super().__init__(image, scale)
        self.speed = 1

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_pipe(cls):
        pipe = 'images/pipe2.png'
        p = cls(pipe, PIPE_SCALING)
        p.bottom = 20
        p.left  = SCREEN_WIDTH
        return p
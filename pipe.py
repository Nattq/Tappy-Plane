import arcade
from constants import *
import random 
class Pipe(arcade.Sprite):
    def __init__(self, image,scale=.5):
        super().__init__(image, scale)
        self.speed = 1.5
        self.scored = False

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_pipe(cls):
        pipe = 'images/pipe2.png'
        p1 = cls(pipe, PIPE_SCALING)
        p1.bottom = random.randint(-100,200)
        p1.left  = SCREEN_WIDTH

        p2 = cls(pipe, PIPE_SCALING)
        p2.bottom = p1.bottom + PIPE_GAP
        p2.left  = SCREEN_WIDTH       
        return p1,p2
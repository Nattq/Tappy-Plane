import arcade
from constants import *
import random 

class Pipe(arcade.Sprite):
    """class representing pipes/rock obstacles"""
    def __init__(self, image,scale=.5):
        """Creates Pipe"""
        super().__init__(image, scale,hit_box_algorithm='Detailed')
        self.speed = None
        self.scored = False
        self.game_score=None

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_pipe(cls,score):
        """Generates pipe with speed depending on current game score
        @param score: current score
        return: tuple of two Pipe objects(top and bottom one)"""
        cls.game_score = score

        pipe_bottom = 'images/rock.png'
        scale=random.uniform(0.5*PIPE_SCALING,1.5*PIPE_SCALING)
        p1 = cls(pipe_bottom, scale)
        p1.bottom = 0
        p1.center_x = SCREEN_WIDTH+50

        pipe_top = 'images/rockDown.png'
        p2 = cls(pipe_top, PIPE_SCALING*2-scale)
        p2.bottom = p1.top + PIPE_GAP
        p2.center_x = p1.center_x
        p2.height = SCREEN_HEIGHT-p1.height-PIPE_GAP

        cls.speed = 2+(cls.game_score+1)//10/2
        p1.speed = cls.speed
        p2.speed = cls.speed
        return p1,p2
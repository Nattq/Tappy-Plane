import arcade
from constants import *
import random 
class Pipe(arcade.Sprite):
    def __init__(self, image,scale=.5):
        super().__init__(image, scale,hit_box_algorithm='Detailed')
        self.speed = 2.5
        self.scored = False

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_pipe(cls):
        pipe_bottom = 'images/rock.png'
        scale=random.uniform(0.7*PIPE_SCALING,1.3*PIPE_SCALING)
        p1 = cls(pipe_bottom, scale)
        p1.add_spatial_hashes()
        p1.bottom = 0
        p1.left  = SCREEN_WIDTH+50
        #p1.draw_hit_box(line_thickness=4)
        
        pipe_top = 'images/rockDown.png'
        p2 = cls(pipe_top, PIPE_SCALING*2-scale)
        p2.bottom = p1.top + PIPE_GAP
        p2.center_x = p1.center_x
        p2.height = SCREEN_HEIGHT-p1.height-PIPE_GAP
        p2.add_spatial_hashes()
        return p1,p2
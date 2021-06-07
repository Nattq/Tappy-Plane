import arcade
import random
from constants import *
class Coin(arcade.Sprite):
    def __init__(self,image):
        super().__init__(image,scale=0.5,
        hit_box_algorithm='Detailed')
        self.speed = PIPE_SPEED

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_coin(cls):
        coin = cls(':resources:images/items/gold_1.png')
        coin.center_x = SCREEN_WIDTH+50
        coin.center_y = random.randint(int(SCREEN_HEIGHT/3),int(SCREEN_HEIGHT/3*2))
        return coin

        

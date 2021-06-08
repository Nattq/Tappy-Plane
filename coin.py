import arcade
import random
from constants import *

class Coin(arcade.Sprite):
    def __init__(self,image):
        super().__init__(image,scale=0.5,hit_box_algorithm='Detailed')
        self.speed = None
        self.game_score =None

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_coin(cls,score):
        cls.game_score = score
        #cls.speed = 3
        coin = cls(':resources:images/items/gold_1.png')
        coin.center_x = SCREEN_WIDTH+50
        coin.center_y = random.randint(int(SCREEN_HEIGHT/3),int(SCREEN_HEIGHT/3*2))
        print('coin')

        cls.speed = 2+cls.game_score//10/2
            

        coin.speed = cls.speed
        print(cls.game_score,cls.speed)
        return coin

        

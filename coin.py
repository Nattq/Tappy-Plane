import arcade
import random
from constants import *

class Coin(arcade.Sprite):
    """Class that represents coin"""
    def __init__(self,image):
        super().__init__(image,scale=0.5,hit_box_algorithm='Detailed')
        self.speed = None
        self.game_score =None

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_coin(cls,score):
        """Generates coins with speed depending on current score
        @param score: current score
        return: object of class Coin
        """
        cls.game_score = score
        cls.speed = 2+(cls.game_score-1)//10/2

        coin = cls(':resources:images/items/gold_1.png')
        coin.center_x = SCREEN_WIDTH+50
        coin.center_y = random.randint(int(SCREEN_HEIGHT/3),int(SCREEN_HEIGHT/3*2))
        coin.speed = cls.speed
        return coin

        
class Hearts(arcade.Sprite):
    """Class representing lifes"""
    def __init__(self,image):
        super().__init__(image ,2)



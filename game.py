import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'flappybird'

CHARACTER_SCALING = 0.5
PIPE_SCALING = 0.5
COIN_SCALING = 0.5

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        #lists of sprites
        self.coin_list = None
        self.pipe_list = None
        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.BEIGE)
    def setup(self):
        #create the sprite lists
        self.player_list = arcade.SpriteList()
        self.pipe_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        image_bird ='images/ghost.jpg'
        self.player_sprite = arcade.Sprite(image_bird,CHARACTER_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        pipe = arcade.Sprite('images/pipe.png', PIPE_SCALING)
        pipe.position = [400, 400]
        self.pipe_list.append(pipe)
        
    def on_draw(self):
        '''render the screen'''
        arcade.start_render()

        self.player_list.draw()
        self.pipe_list.draw()
        self.coin_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
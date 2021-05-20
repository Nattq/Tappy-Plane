import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'flappybird'

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BEIGE)

    def setup(self):
        pass

    def on_draw(self):
        '''render the screen'''
        arcade.start_render()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
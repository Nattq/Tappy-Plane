import arcade
from pyglet.window.key import SPACE

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
OFFSCREEN_SPACE = 300
SCREEN_TITLE = 'flappybird'

CHARACTER_SCALING = 0.5
PIPE_SCALING = 0.5
COIN_SCALING = 0.5

BIRD_MOVEMENT_SPEED = 5

class Pipe(arcade.Sprite):
    def __init__(self, image,scale=.5):
        super().__init__(image, scale)
        self.speed = 1

    def update(self):
        self.center_x -= self.speed

    @classmethod
    def generate_pipe(cls):
        pipe = 'images/rect2.jpg'
        p = cls(pipe, PIPE_SCALING)
        p.bottom = 20
        p.left  = 450
        return p


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

        #set up bird
        image_bird ='images/ghost.jpg'
        self.player_sprite = arcade.Sprite(image_bird,CHARACTER_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        #create pipes
        #firstpipe = Pipe('images/rect2.jpg', PIPE_SCALING)
        firstpipe = Pipe.generate_pipe()
        self.pipe_list.append(firstpipe)

        #create engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.pipe_list)
        
    def on_draw(self):
        '''render the screen'''
        arcade.start_render()

        self.player_list.draw()
        self.pipe_list.draw()
        self.coin_list.draw()

    def on_key_press(self,key,modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = BIRD_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = -2*BIRD_MOVEMENT_SPEED

    def on_update(self, delta_time):



        next_pipe = None
        for pipe in self.pipe_list:
            if pipe.right < 0:
                pipe.kill()
            elif pipe.right <= 100 and len(self.pipe_list)<=2:
                next_pipe = Pipe.generate_pipe()
        if next_pipe:      
            self.pipe_list.append(next_pipe)
            
        self.physics_engine.update()
        self.pipe_list.update()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
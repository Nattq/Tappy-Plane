import arcade
from pyglet.window.key import SPACE
import menu
from constants import *
from pipe import Pipe
class MyGame(arcade.View):

    def __init__(self):
        super().__init__()
        #lists of sprites
        self.coin_list = None
        self.pipe_list = None
        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.BEIGE)
        
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.pipe_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        image_bird ='images/square2.png'
        self.player_sprite = arcade.Sprite(image_bird,CHARACTER_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        firstpipe = Pipe.generate_pipe()
        self.pipe_list.append(firstpipe)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.pipe_list)
        
    def on_draw(self):
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

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        next_pipe = None
        for pipe in self.pipe_list:
            if pipe.right < 0:
                pipe.kill()
            elif pipe.right <= 100 and len(self.pipe_list) <= 2:
                next_pipe = Pipe.generate_pipe()
        if next_pipe:      
            self.pipe_list.append(next_pipe)
            
        self.physics_engine.update()
        self.pipe_list.update()

        if arcade.check_for_collision_with_list(self.player_sprite,self.pipe_list):
            self.player_sprite.kill()
            view = menu.GameOver()
            self.window.show_view(view)

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    start_view = menu.MenuView()
    window.show_view(start_view)
    #start_view.setup()
    arcade.run()

if __name__ == '__main__':
    main()
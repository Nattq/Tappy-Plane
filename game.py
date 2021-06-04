import arcade
from pyglet.window.key import SPACE
import menu
from constants import *
from pipe import Pipe
from life import Hearts
class MyGame(arcade.View):
    def __init__(self,input_box):
        super().__init__()
        self.coin_list = None
        self.pipe_list = None
        self.player_list = None
        self.player_sprite = None
        self.heart_list = None
        self.user = input_box.text
        self.score = 0
        self.dead = False
        arcade.set_background_color(arcade.csscolor.BEIGE)
        
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.pipe_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.heart_list = arcade.SpriteList(use_spatial_hash=True)
        image_bird =':resources:images/enemies/sawHalf.png'
        self.player_sprite = arcade.Sprite(image_bird,CHARACTER_SCALING)
        self.player_sprite.center_x = BIRD_X
        self.player_sprite.center_y = BIRD_Y
        self.player_list.append(self.player_sprite)
        firstpipe = Pipe.generate_pipe()
        self.pipe_list.append(firstpipe[0])
        self.pipe_list.append(firstpipe[1])       

        for i in range(3):
            h = Hearts("tile_0373.png")
            h.center_x=50
            h.center_y = 600-i*35
            self.heart_list.append(h)
        print(len(self.heart_list))
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.pipe_list)
        
    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
        self.pipe_list.draw()
        self.coin_list.draw()
        self.heart_list.draw()
        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text,100,650,
                            arcade.csscolor.BLACK, 18)
        arcade.draw_text(str(self.user),200,650,
                            arcade.csscolor.BLACK, 18)
    def on_key_press(self,key,modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = BIRD_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = -BIRD_MOVEMENT_SPEED

    #def on_mouse_motion(self, x, y, dx, dy):
        #self.player_sprite.center_x = x
        #self.player_sprite.center_y = y

    def on_update(self, delta_time):
        next_pipe = None
        for pipe in self.pipe_list:
            if pipe.right < 0:
                pipe.kill()
            elif pipe.right <= 100 and len(self.pipe_list) <= 2:
                next_pipe = Pipe.generate_pipe()
        if next_pipe:      
            self.pipe_list.append(next_pipe[0])
            self.pipe_list.append(next_pipe[1])            

        if arcade.check_for_collision_with_list(self.player_sprite,self.pipe_list):
            for pipe in self.pipe_list:
                pipe.center_x = pipe.center_x+200
            self.player_sprite.center_x=BIRD_X
            self.player_sprite.center_y = BIRD_Y
            self.heart_list[-1].kill()
            
        if len(self.heart_list)==0:
            with open('best_scores.txt', 'a') as file:
                score = self.score
                user = self.user
                file.write(user +','+str(score)+"\n")
            view = menu.GameOver()
            self.window.show_view(view)
            self.dead = True

        if self.pipe_list[0].center_x <= BIRD_X and self.pipe_list[0].scored == False:
            self.pipe_list[0].scored = True
            self.pipe_list[1].scored = True
            self.score +=1

        if self.player_sprite.center_y >= MAX_HEIGHT:
            self.player_sprite.center_y = MAX_HEIGHT
        elif self.player_sprite.center_y <= MIN_HEIGHT:
            self.player_sprite.center_y = MIN_HEIGHT

        self.physics_engine.update()
        self.pipe_list.update()
        self.heart_list.update()

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    user = None
    start_view = menu.MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()
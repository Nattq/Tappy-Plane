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
        self.ground = None
        arcade.set_background_color(arcade.csscolor.BEIGE)
        
    def setup(self):
        self.player_list = arcade.SpriteList(use_spatial_hash=True)
        self.pipe_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.heart_list = arcade.SpriteList(use_spatial_hash=True)
        self.ground = arcade.SpriteList(use_spatial_hash=True)
        image_bird ='images/planeRed1.png'

        self.player_sprite = arcade.Sprite(image_bird,CHARACTER_SCALING)
        self.player_sprite.center_x = BIRD_X
        self.player_sprite.center_y = BIRD_Y
        self.player_sprite.angle = 4
        self.player_sprite.speed = 0
        self.player_list.append(self.player_sprite)

        firstpipe = Pipe.generate_pipe()
        self.pipe_list.append(firstpipe[0])
        self.pipe_list.append(firstpipe[1])       

        self.top_ground = arcade.Sprite('images/groundDirt.png',flipped_horizontally=True,hit_box_algorithm ='Detailed')
        self.top_ground.angle=180
        self.top_ground.top = SCREEN_HEIGHT
        self.top_ground.center_x = SCREEN_WIDTH/2
        self.bottom_ground = arcade.Sprite('images/groundDirt.png',hit_box_algorithm ='Detailed')
        self.bottom_ground.bottom = 0
        self.bottom_ground.center_x = SCREEN_WIDTH/2
        self.ground.append(self.top_ground)
        self.ground.append(self.bottom_ground)

        for i in range(3):
            h = Hearts("tile_0373.png")
            h.center_x=50
            h.center_y = 600-i*35
            self.heart_list.append(h)

        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.pipe_list)
        
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.pipe_list.draw()
        self.coin_list.draw()
        self.heart_list.draw()
        self.ground.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text,20,670,
                            arcade.csscolor.BLACK, 18)
        arcade.draw_text(str(self.user),20+100,670,
                            arcade.csscolor.BLACK, 18)

    def on_key_press(self,key,modifiers):
        if key == arcade.key.SPACE:
            #self.player_sprite.change_y = BIRD_MOVEMENT_SPEED
            self.jump()

    #def on_key_release(self, key, modifiers):
       # if key == arcade.key.SPACE:
            #self.player_sprite.change_y = -BIRD_MOVEMENT_SPEED

    def jump(self):
        self.player_sprite.speed = 70
    #def on_mouse_motion(self, x, y, dx, dy):
        #self.player_sprite.center_x = x
        #self.player_sprite.center_y = y

    def on_update(self, delta_time):
        #print( self.player_sprite.top-self.pipe_list[1].bottom )
        next_pipe = None
        for pipe in self.pipe_list:
            if pipe.right < 0:
                pipe.kill()
            elif pipe.right <= 100 and len(self.pipe_list) <= 2:
                next_pipe = Pipe.generate_pipe()
        if next_pipe:      
            self.pipe_list.append(next_pipe[0])
            self.pipe_list.append(next_pipe[1])
            self.pipe_list[0].draw_hit_box()      
        self.pipe_list[0].draw_hit_box()
        hits = arcade.check_for_collision_with_list(self.player_sprite,self.pipe_list) or arcade.check_for_collision_with_list(
            self.player_sprite,self.ground) 
            #or (abs(self.player_sprite.center_x-self.pipe_list[0].center_x) 
            #<2 and self.player_sprite.bottom-self.pipe_list[0].top <1) or (abs(self.player_sprite.center_x-
                    #self.pipe_list[1].center_x) < 3 and self.pipe_list[1].bottom-self.player_sprite.top <1)
        if hits :
            for pipe in self.pipe_list:
                pipe.center_x = pipe.center_x+200
            arcade.pause(1)
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

        if self.player_sprite.speed >0:
            self.player_sprite.center_y += 3
            self.player_sprite.speed -= 3
        else:
            self.player_sprite.center_y -=3


        if self.pipe_list[0].center_x <= BIRD_X and self.pipe_list[0].scored == False:
            self.pipe_list[0].scored = True
            self.pipe_list[1].scored = True
            self.score +=1

        """        if self.player_sprite.center_y >= MAX_HEIGHT:
            self.player_sprite.center_y = MAX_HEIGHT
        elif self.player_sprite.center_y <= MIN_HEIGHT:
            self.player_sprite.center_y = MIN_HEIGHT"""

        #self.physics_engine.update()
        self.pipe_list.update()
        self.heart_list.update()

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    start_view = menu.MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()
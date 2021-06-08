import arcade
import random 
import menu
from constants import *
from pipe import Pipe
from coin import Coin,Hearts

class MyGame(arcade.View):
    def __init__(self,input_box):
        """Create game window"""
        super().__init__()
        self.coin_list = None
        self.pipe_list = None
        self.player_list = None
        self.player_sprite = None
        self.heart_list = None
        self.score = 0
        self.dead = False
        self.ground = None
        arcade.set_background_color(arcade.csscolor.BEIGE)
        if input_box.text != "GIVE USERNAME":
                self.user = input_box.text
        else:
            self.user = "USER"
        
    def setup(self):
        """Setting up"""
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

        firstpipe = Pipe.generate_pipe(self.score)
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
            h = Hearts("images/tile_0373.png")
            h.center_x=50
            h.center_y = 600-i*35
            self.heart_list.append(h)
        
    def on_draw(self):
        """Method that draws sprites and text"""
        arcade.start_render()
        self.player_list.draw()
        self.pipe_list.draw()
        self.coin_list.draw()
        self.heart_list.draw()
        self.ground.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text,20,670,
                            arcade.csscolor.WHITE_SMOKE, 18)
        arcade.draw_text(str(self.user),20+100,670,
                            arcade.csscolor.WHITE_SMOKE, 18)

    def on_key_press(self,key,modifiers):
        """Method to control from keyboard"""
        if key == arcade.key.SPACE:
            self.jump()


    def jump(self):
        """Method used to control movement of player's sprite"""
        self.player_sprite.speed = 70
        self.player_sprite.angle =30

    def on_update(self, delta_time):
        """Method to control game"""
        #generate pipes 
        for pipe in self.pipe_list:
            if pipe.right < 0:
                pipe.remove_from_sprite_lists()
            elif pipe.center_x <= 200 and len(self.pipe_list) <= 2:
                next_pipe = Pipe.generate_pipe(self.score)
                self.pipe_list.append(next_pipe[0])
                self.pipe_list.append(next_pipe[1])
            else:
                pass 

        #generate coins
        if len(self.coin_list)==0  and self.score > 1 and self.pipe_list[0].center_x==250:
            p = random.choices([True,False],[0.3,0.7])
            if p[0]==True:
                coin = Coin.generate_coin(self.score)
                self.coin_list.append(coin)  

        #collecting coins
        coin_hit = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        for coin in coin_hit:
            coin.remove_from_sprite_lists()
            self.score +=1
            arcade.play_sound(SOUNDS['coin'])
        if  len(self.coin_list)>0 and self.coin_list[0].right <0:
            self.coin_list[0].remove_from_sprite_lists() 

        #hits with pipes
        hits = arcade.check_for_collision_with_list(self.player_sprite,self.pipe_list) or arcade.check_for_collision_with_list(
            self.player_sprite,self.ground) 
        if hits :
            if len(self.heart_list) >1:
                arcade.play_sound(SOUNDS['hit'])
                for pipe in self.pipe_list:
                    pipe.center_x = pipe.center_x+200
                arcade.pause(1)
                self.player_sprite.center_x=BIRD_X
                self.player_sprite.center_y = BIRD_Y
                self.heart_list[-1].remove_from_sprite_lists()
            else:
                arcade.play_sound(SOUNDS["game over"])
                with open('best_scores.txt', 'a') as file:
                    score = self.score
                    user = self.user
                    file.write(user +','+str(score)+"\n")
                view = menu.GameOver(self.score)
                view.setup()
                self.window.show_view(view)

        #jumping height
        if self.player_sprite.speed >0:
            self.player_sprite.center_y += 4
            self.player_sprite.speed -= 4
        else:
            self.player_sprite.center_y -=3

        #jumping angle
        if self.player_sprite.angle > -15:
            self.player_sprite.angle -=1.7
        else:
            pass

        #scoring points
        if self.pipe_list[0].center_x <= BIRD_X and self.pipe_list[0].scored == False:
            self.pipe_list[0].scored = True
            self.pipe_list[1].scored = True
            self.score +=1

        self.pipe_list.update()
        self.heart_list.update()
        self.coin_list.update()

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    start_view = menu.MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()
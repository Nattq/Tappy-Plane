#menu.py
from arcade.window_commands import start_render
import game
import arcade
from constants import *
import arcade.gui
from arcade.gui import UIManager
from buttons import ExitButton, RulesButton, ScoreButton, StartButton, UserName,BackToMenu
import sys
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.user = None
        self.ui_manager = UIManager()

    def on_show_view(self):
        self.setup()
        arcade.set_background_color(arcade.color.GAINSBORO)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()

        exitbtn = ExitButton(center_x = SCREEN_WIDTH/2, center_y = 300)
        self.ui_manager.add_ui_element(exitbtn)
        scorebtn = ScoreButton(center_x = SCREEN_WIDTH/2, center_y = 200)
        self.ui_manager.add_ui_element(scorebtn)
        user_name = UserName(SCREEN_WIDTH/2,500,"user_name","podaj nazwe")
        self.ui_manager.add_ui_element(user_name)
        startbtn = StartButton(self,center_x=SCREEN_WIDTH/2, center_y=400,input_box=user_name)
        self.ui_manager.add_ui_element(startbtn)
        rulesbtn = RulesButton(SCREEN_WIDTH/2,center_y=100)
        self.ui_manager.add_ui_element(rulesbtn)
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)


    def on_draw(self):
        arcade.start_render()
        #arcade.draw_text("Menu screen", SCREEN_WIDTH/2,SCREEN_HEIGHT/2, 
        #                    arcade.color.BLACK, anchor_x="center",font_size = 50,)
        #arcade.draw_text("Click to advance",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,arcade.color.BLACK)


    #def on_mouse_press(self,_x,_y,_button,_modifiers):
        #menu_view = game.MyGame()
        #menu_view.setup()
        #self.window.show_view(menu_view)

class GameOver(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        #arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH/2,SCREEN_HEIGHT/2, 
                            arcade.color.RED, anchor_x="center",font_size = 50,)
        arcade.draw_text("Click to go back start menu",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,arcade.color.RED)

    #def on_key_press(self,key,modifiers):
        #if key == arcade.key.SPACE:
            #menu = MenuView()
            #menu.window.show_view(menu)

    def on_mouse_press(self,_x,_y,_button,_modifiers):
        menu_view = MenuView()
        menu_view.window.show_view(menu_view)

class BestScore(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.AQUAMARINE)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        back_btn = BackToMenu(SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.ui_manager.add_ui_element(back_btn)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("BEST SCORES", SCREEN_WIDTH/2,SCREEN_HEIGHT*0.85, 
                            arcade.color.RED, anchor_x="center",font_size = 50,)

        with open('best_scores.txt','r') as file:
            content = file.readlines()

        content = [element.split(",") for element in content]
        content = [[element[0],int(element[1].rstrip("\n"))] for element in content] 
        content = sorted(content, key=lambda x: x[1],reverse=True)
        for i in range(5):
            arcade.draw_text(str(i+1)+".",SCREEN_WIDTH/5, SCREEN_HEIGHT*0.75 - i*30,arcade.color.BLACK_BEAN)
            try:
                arcade.draw_text(content[i][0],SCREEN_WIDTH/5+40, SCREEN_HEIGHT*0.75 - i*30,arcade.color.BLACK_BEAN)
                arcade.draw_text(str(content[i][1]),SCREEN_WIDTH*0.75, SCREEN_HEIGHT*0.75 - i*30,arcade.color.BLACK_BEAN)
                #print(content[i][1])
            except IndexError:
                pass

            


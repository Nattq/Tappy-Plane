#menu.py
import game
import arcade
from constants import *
import arcade.gui
from arcade.gui import UIManager
from buttons import ExitButton
import sys
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()
    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_menager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()

        exitbtn = ExitButton(center_x = 100, center_y = 100)
        self.ui_manager.add_ui_element(exitbtn)

    #def on_show(self):
        #arcade.set_background_color(arcade.color.WHITE)
        #arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)


    def on_draw(self):
        arcade.start_render()
        #arcade.draw_text("Menu screen", SCREEN_WIDTH/2,SCREEN_HEIGHT/2, 
        #                    arcade.color.BLACK, anchor_x="center",font_size = 50,)
        #arcade.draw_text("Click to advance",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,arcade.color.BLACK)


    def on_mouse_press(self,_x,_y,_button,_modifiers):
        menu_view = game.MyGame()
        menu_view.setup()
        self.window.show_view(menu_view)

class GameOver(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH/2,SCREEN_HEIGHT/2, 
                            arcade.color.RED, anchor_x="center",font_size = 50,)
        arcade.draw_text("Click to go back to menu",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,arcade.color.RED)

    def on_mouse_press(self,_x,_y,_button,_modifiers):
        menu_view = MenuView()
        #menu_view.setup()
        self.window.show_view(menu_view)
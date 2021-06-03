import arcade
import sys

from pyglet.libs.win32.constants import IMAGE_COMDAT_SELECT_NODUPLICATES 
import game
import menu

class ExitButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Exit",center_x = center_x, center_y= center_y, width = 300)
    def on_click(self):
        self.window.close_window()
    

class StartButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y,input_box):
        super().__init__(text = "start",center_x = center_x, center_y= center_y, width = 300,input_box=input_box)
        self.input_box = input_box
    def on_click(self):
        menu_view = game.MyGame(self.input_box)
        menu_view.setup()
        menu_view.window.show_view(menu_view)
        #text = input_box.text
        #menu_view.user = text


class ScoreButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Best score",center_x = center_x, center_y= center_y, width = 300)

    def on_click(self):
        score = menu.BestScore()
        score.window.show_view(score)


class UserName(arcade.gui.UIInputBox):
    def __init__(self, center_x, center_y,id,text):
        super().__init__(center_x=center_x,center_y=center_y,text=text,id = id,width=300)
import arcade
import sys

from pyglet.libs.win32.constants import IMAGE_COMDAT_SELECT_NODUPLICATES 
import game
import menu

class ExitButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Exit",center_x = center_x, center_y= center_y, width = 300,height=50)
    def on_click(self):
        arcade.close_window()
    

class StartButton(arcade.gui.UIFlatButton):
    def __init__(self,menu_view,center_x,center_y,input_box):
        super().__init__(text = "START",center_x = center_x, center_y= center_y, width = 300,input_box=input_box,height=50)
        self.input_box = input_box
        self.view = menu_view

    def on_click(self):
        menu_view = game.MyGame(self.input_box)
        menu_view.setup()
        menu_view.window.show_view(menu_view)


class ScoreButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Best score",center_x = center_x, center_y= center_y, width = 300,height =50)

    def on_click(self):
        score = menu.BestScore()
        score.setup()
        score.window.show_view(score)


class UserName(arcade.gui.UIInputBox):
    def __init__(self, center_x, center_y,id,text):
        super().__init__(center_x=center_x,center_y=center_y,text=text,id = id,width=300)

    def on_click(self):
        if self.text == "podaj nazwe":
            self.text = ""

class RulesButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text="Rules",center_x=center_x,center_y=center_y,width=300,height=50)

class BackToMenu(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text="Back to menu",center_x=center_x,center_y=center_y,width=300,heigth=50)

    def on_click(self):
        menu_view = menu.MenuView()
        menu_view.setup()
        menu_view.window.show_view(menu_view)
        #self.kill()

class AboutAuthor(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text="About author",center_x=center_x,center_y=center_y,width=300,height=50)
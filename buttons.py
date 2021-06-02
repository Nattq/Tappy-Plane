import arcade
import sys 
import game
import menu

class ExitButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Exit",center_x = center_x, center_y= center_y, width = 300)
    def on_click(self):
        sys.exit()
    

class StartButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "start",center_x = center_x, center_y= center_y, width = 300)

    def on_click(self):
        menu_view = game.MyGame()
        menu_view.setup()
        menu_view.window.show_view(menu_view)


class ScoreButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Best score",center_x = center_x, center_y= center_y, width = 300)

    def on_click(self):
        score = menu.BestScore()
        score.window.show_view(score)

    
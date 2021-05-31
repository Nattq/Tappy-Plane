import arcade
import sys 
class ExitButton(arcade.gui.UIFlatButton):
    def __init__(self,center_x,center_y):
        super().__init__(text = "Exit",center_x = center_x, center_y= center_y, width = 300)

    def on_click(self):
        sys.exit()


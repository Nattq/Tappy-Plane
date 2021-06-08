#menu.py
#from arcade.window_commands import start_render
import arcade
from arcade.color import BLACK_BEAN
from constants import *
import arcade.gui
from arcade.gui import UIManager
from buttons import ExitButton, RulesButton, ScoreButton, StartButton, UserName,BackToMenu, AboutAuthor

class MenuView(arcade.View):
    def __init__(self):
        """Creates a menu window"""
        super().__init__()
        self.user = None
        self.ui_manager = UIManager()
        self.background = None

    def on_show_view(self):
        self.setup()
        arcade.set_background_color(arcade.color.GAINSBORO)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """setting up elements"""
        self.background = arcade.load_texture("images/background.png")
        self.ui_manager.purge_ui_elements()
        self.text_list = arcade.SpriteList()
        self.text = arcade.Sprite("images/tappy.png")
        self.text.center_x = SCREEN_WIDTH//2
        self.text.top = SCREEN_HEIGHT -10
        self.text.width = SCREEN_WIDTH-100
        self.text.height = 80
        self.text_list.append(self.text)


        exitbtn = ExitButton(center_x = SCREEN_WIDTH/2, center_y = SCREEN_HEIGHT-100-6*70)
        self.ui_manager.add_ui_element(exitbtn)

        scorebtn = ScoreButton(center_x = SCREEN_WIDTH/2, center_y =SCREEN_HEIGHT-100-4*70)
        self.ui_manager.add_ui_element(scorebtn)

        user_name = UserName(SCREEN_WIDTH/2,SCREEN_HEIGHT-100-1*50,"user_name","GIVE USERNAME")
        self.ui_manager.add_ui_element(user_name)

        startbtn = StartButton(self,center_x=SCREEN_WIDTH/2,center_y =SCREEN_HEIGHT-100-2*70,input_box=user_name)
        self.ui_manager.add_ui_element(startbtn)

        rulesbtn = RulesButton(SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT-100-3*70)
        self.ui_manager.add_ui_element(rulesbtn)

        authorbtn = AboutAuthor(center_x =SCREEN_WIDTH/2,center_y =SCREEN_HEIGHT-100-5*70                                                                 )
        self.ui_manager.add_ui_element(authorbtn)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.text.draw()

class GameOver(arcade.View):
    def __init__(self,score):
        """Creates a game over view"""
        super().__init__()
        self.ui_manager = UIManager()
        self.game_score = score

    def setup(self):
        self.text_list = arcade.SpriteList()
        self.text = arcade.Sprite("images/game_over.png")
        self.text.center_x = SCREEN_WIDTH//2
        self.text.top = SCREEN_HEIGHT -10
        self.text.width = SCREEN_WIDTH-100
        self.text.height = 80
        self.text_list.append(self.text)

        self.text2 = arcade.Sprite("images/score.png")
        self.text2.center_x = SCREEN_WIDTH//2
        self.text2.top = SCREEN_HEIGHT -200
        self.text2.width = SCREEN_WIDTH-100
        self.text2.height = 60
        self.text_list.append(self.text2)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f'{self.game_score}', SCREEN_WIDTH//2,SCREEN_HEIGHT//2,arcade.color.RED,bold=True,font_size=40)
        arcade.draw_text("Click to go back start menu",SCREEN_WIDTH/4, SCREEN_HEIGHT/2-75,arcade.color.RED,font_size=20)

        self.text_list.draw()

    def on_mouse_press(self,_x,_y,_button,_modifiers):
        menu_view = MenuView()
        menu_view.window.show_view(menu_view)

class BestScore(arcade.View):
    def __init__(self):
        """Creates a best scores view"""
        super().__init__()
        self.ui_manager = UIManager()
        self.background = None

    def on_show(self):
        arcade.set_background_color(arcade.color.AQUAMARINE)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.background = arcade.load_texture("images/background.png")

        self.text_list = arcade.SpriteList()
        self.text = arcade.Sprite("images/best.png")
        self.text.center_x = SCREEN_WIDTH//2
        self.text.top = SCREEN_HEIGHT -10
        self.text.width = SCREEN_WIDTH-100
        self.text.height = 80
        self.text_list.append(self.text)

        back_btn = BackToMenu(SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.ui_manager.add_ui_element(back_btn)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.text_list.draw()
        with open('best_scores.txt','r') as file:
            content = file.readlines()
        raw_content = [element.split(",") for element in content]
        content = [ [element[0],int(element[1].rstrip("\n")) ] for element in raw_content] 
        content = sorted(content, key=lambda x: x[1],reverse=True)
        for i in range(10):
            arcade.draw_text(str(i+1)+".",SCREEN_WIDTH/5, SCREEN_HEIGHT*0.75 - i*30,arcade.color.BLACK_BEAN,font_size=20)
            try:
                arcade.draw_text(content[i][0],SCREEN_WIDTH/5+40, SCREEN_HEIGHT*0.75 - i*35,arcade.color.BLACK_BEAN,font_size=20)
                arcade.draw_text(str(content[i][1]),SCREEN_WIDTH*0.75, SCREEN_HEIGHT*0.75 - i*35,arcade.color.BLACK_BEAN,font_size=20)
            except IndexError:
                pass

class AuthorPage(arcade.View):
    def __init__(self):
        """Creates an author's page"""
        super().__init__()
        self.ui_manager = UIManager()
        self.background = None

    def setup(self):
        """Setting up"""
        self.background = arcade.load_texture("images/background.png")
        self.text_list = arcade.SpriteList()
        self.text = arcade.Sprite("images/author.png")
        self.text.center_x = SCREEN_WIDTH//2
        self.text.top = SCREEN_HEIGHT -10
        self.text.width = SCREEN_WIDTH-100
        self.text.height = 80
        self.text_list.append(self.text)
        back_btn = BackToMenu(SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.ui_manager.add_ui_element(back_btn)


    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.text_list.draw()
        arcade.draw_text("""Hej!\nNazywam się Natalia i studiuję\nmatematykę stosowaną na\nPolitechnice Wrocławskiej.\n\nTo moja gra przygotowana
        w ramach zajęć z programowania.\nZyczą dużo dobrej zabawy\ni powodzenia!""",SCREEN_WIDTH//7,SCREEN_HEIGHT//2,arcade.color.BLACK_BEAN,font_size=18,align='center')   

class RulesPage(arcade.View):
    def __init__(self):
        """Creates a view with rules"""
        super().__init__()
        self.ui_manager = UIManager()
        self.background = None
        
    def setup(self):
        self.background = arcade.load_texture("images/background.png")

        self.text_list = arcade.SpriteList()
        self.text = arcade.Sprite("images/rules.png")
        self.text.center_x = SCREEN_WIDTH//2
        self.text.top = SCREEN_HEIGHT -10
        self.text.width = SCREEN_WIDTH-100
        self.text.height = 80
        self.text_list.append(self.text)
        back_btn = BackToMenu(SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.ui_manager.add_ui_element(back_btn)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.text_list.draw()           
        for i in range(5):
            arcade.draw_text(str(i+1)+".",SCREEN_WIDTH/8, SCREEN_HEIGHT*0.75 - i*30,
            arcade.color.BLACK_BEAN,font_size=15)
            arcade.draw_text(RULES[i],SCREEN_WIDTH//8+30,SCREEN_HEIGHT*0.75 - i*30,
            arcade.color.BLACK_BEAN,font_size=15)
        arcade.draw_text("""Postaraj się uratować samolot\ni wylecieć z jaskini.
        Może kiedyś ci się uda ;).
        Powodzenia!""",SCREEN_WIDTH//4,SCREEN_HEIGHT//3,arcade.color.BLACK_BEAN,font_size=19,
        align='center')
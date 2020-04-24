import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEW GAME"

class buttons(arcade.TextButton):
    '''Where we get the buttons that we created'''
    def __init__(self,cx,cy,width,height,text,fontSize,fcolor,hcolor,
                 scolor,theme = None):
        super().__init__(cx,cy,width,height,text = text,
                         font_size = fontSize,face_color = fcolor,
                         highlight_color = hcolor,shadow_color = scolor)
        
    '''def check_mouse_press_for_buttons(x, y, button_list):
        """ Given an x, y, see if we need to register any button clicks. """
        for button in button_list:
            if x > button.center_x + button.width / 2:
                continue
            if x < button.center_x - button.width / 2:
                continue
            if y > button.center_y + button.height / 2:
                continue
            if y < button.center_y - button.height / 2:
                continue
            button.on_press()


    def check_mouse_release_for_buttons(_x, _y, button_list):
        """ If a mouse button has been released, see if we need to process
            any release events. """
        for button in button_list:
            if button.pressed:
                button.on_release()'''

        

class MainMenu(arcade.View):
    button = ""
    def on_show(self):
        arcade.set_background_color(arcade.color.WHEAT)
        self.button = buttons(500,250,100,50,
                                        "Click Here",12,arcade.color.GREEN,
                                        arcade.color.GRAY,arcade.color.GRAY)
    def on_draw(self):
        arcade.start_render()
        self.button.draw()
    def on_mouse_press(self,x, y,button, modifiers):
        self.button.check_mouse_press(x, y)
    def on_update(self,delta_time):
        #print(delta_time)
        pass





class GameOver(arcade.View):
    def on_show(self):
        pass
    def on_mouse_press(self,key,modifier):
        pass

class StartGame(arcade.View):
    def on_show(self):
        pass
    def on_mouse_press(self,key,modifier):
        pass

class Puase(arcade.View):
    def on_show(self):
        pass
    def on_mouse_press(self,key,modifier):
        pass
Window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
Window.show_view(MainMenu())
arcade.run()


'''class Customized(arcade.View):
    def on_show(self):
        pass
    def on_mouse_press(self,key,modifier):
        pass
'''

import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEW GAME"
 
class Button():
    def __init__(self,center_x,center_y,width,height,
                 color,text,tilt_angle = 0):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.shadow_color1 = arcade.color.DARK_GRAY
        self.shadow_color2 =arcade.color.WHITE
        self.text = text
        self.text_color = arcade.color.BLACK
    def draw_button(self):
        textLenght = len(self.text)
        deducX = 25
        if textLenght == 5:
            deducX = 25
        elif textLenght > 5:
            times = textLenght - 5
            while times > 0:
                deducX += 5
                times -= 1
        else:
            times = 5 - textLenght
            while times > 0:
                deducX -= 5
                times -= 1
            
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)    
        #Top
        arcade.draw_line(self.center_x - self.width/2,self.center_y + self.height/2,
                         self.center_x + self.width/2,self.center_y + self.height/2,
                         self.shadow_color1,2)
        #Left
        arcade.draw_line(self.center_x - self.width/2,self.center_y + self.height/2,
                         self.center_x - self.width/2,self.center_y - self.height/2,
                         self.shadow_color1,2)
        #Right
        arcade.draw_line(self.center_x + self.width/2,self.center_y + self.height/2,
                         self.center_x + self.width/2,self.center_y - self.height/2,
                         self.shadow_color1,2)
        #buttom
        arcade.draw_line(self.center_x - self.width/2,self.center_y - self.height/2,
                         self.center_x + self.width/2,self.center_y - self.height/2,
                         self.shadow_color1,2)
        
        arcade.draw_text_2(self.text,self.center_x - deducX,self.center_y - self.height * 0.15,arcade.color.BLACK,font_size = 15)
        #print(self.width/2 - self.center_x)
    def on_press(self):
        self.shadow_color2 = arcade.color.DARK_GRAY
        self.shadow_color1 = arcade.color.WHITE
    def on_release(self):
        self.shadow_color1 = arcade.color.DARK_GRAY
        self.shadow_color2 =arcade.color.WHITE

    def check_mouse_press(self,x,y):
        if x > self.center_x - self.width/2 and x < self.center_x + self.width/2 :
            if y > self.center_y - self.height/2 and y < self.center_y + self.height/2 :
                print("Yes")
                self.on_press()
    def check_mouse_release(self,x,y):
        if x > self.center_x - self.width/2 and x < self.center_x + self.width/2 :
            if y > self.center_y - self.height/2 and y < self.center_y + self.height/2 :
                print("Yes")
                self.on_release()
    
        
        

class MainMenu(arcade.View):
    button = Button(100,400,100,50,arcade.color.GRAY,"Start")
    def on_show(self):
        arcade.set_background_color(arcade.color.WHEAT)
    def on_draw(self):
        arcade.start_render()
        self.button.draw_button()

    def on_mouse_press(self,x,y,button,modifiers):
        self.button.check_mouse_press(x,y)
    def on_mouse_release(self,x,y,button,modifiers):
        self.button.check_mouse_release(x,y)
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

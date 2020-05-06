import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEW GAME"
 
class Button():
    def __init__(self,center_x,center_y,width,height,
                 color,text,function,text_color,tilt_angle = 0):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.defualt = color
        self.shadow_color1 = arcade.color.DARK_GRAY
        self.shadow_color2 =arcade.color.WHITE
        self.text = text
        self.text_color = text_color
        self.function = function
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
        arcade.draw_text_2(self.text,(self.center_x - deducX),(self.center_y - self.height * 0.15),self.text_color,font_size = 15)
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
        
        
        
    def on_press(self):
        self.shadow_color2 = arcade.color.DARK_GRAY
        self.shadow_color1 = arcade.color.WHITE
        self.color = (188, 190, 194)
    def on_release(self):
        self.shadow_color1 = arcade.color.DARK_GRAY
        self.shadow_color2 =arcade.color.WHITE
        self.color = self.defualt

    def check_mouse_press(self,x,y):
        if x > self.center_x - self.width/2 and x < self.center_x + self.width/2 :
            if y > self.center_y - self.height/2 and y < self.center_y + self.height/2 :
                self.on_press()
    def check_mouse_release(self,x,y):
        if x > self.center_x - self.width/2 and x < self.center_x + self.width/2 :
            if y > self.center_y - self.height/2 and y < self.center_y + self.height/2 :
                #self.function()
                self.on_release()


class MainMenu(arcade.View): 
    Play = Button(100,550,150,50,arcade.color.AVOCADO,"Play",None,arcade.color.GREEN)
    Help = Button(100,450,150,50,arcade.color.AVOCADO,"Help",None,arcade.color.GREEN)
    Heroes = Button(100,500,150,50,arcade.color.AVOCADO,"Heroes",None,arcade.color.GREEN)
    background0 = arcade.Sprite("../../SpriteLists/tree.png",center_x=200,center_y=300)
    background = arcade.SpriteList()
    button_list = []
    def on_show(self):
        arcade.set_background_color(arcade.color.BISTRE_BROWN)
        self.button_list.append(self.Play)
        self.button_list.append(self.Help)
        self.button_list.append(self.Heroes)
        self.background.append(self.background0)
        
    def on_draw(self):
        arcade.start_render()
        self.Play.draw_button()
        self.Help.draw_button()
        self.Heroes.draw_button()
        self.background.draw()

    def on_mouse_press(self,x,y,button,modifiers):
        for i in self.button_list:
            i.check_mouse_press(x,y)
            
    def on_mouse_release(self,x,y,button,modifiers):
        for i in self.button_list:
            i.check_mouse_release(x,y)

    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        pass
    
    def on_mouse_motion(self,x,y,dx,dy):
        pass

    
    def on_key_press(self, key, modifier):
        pass
            
    def on_key_release(self, key, modifier):
        pass
    def on_update(self,delta_time):
        pass

            
class StartGame(arcade.View):
    def todo():
        pass
    def todo1():
        pass
    def todo2():
        pass
    
    button_list = []
    x_View = 0
    y_View = 0
    change_x = 0
    change_y = 0
    movement_speed = 5
    RIGHT_Boundary = SCREEN_WIDTH
    LEFT_Boundary = 40

    def on_show(self):
        pass

    def on_draw(self):
        pass

    def on_update(self,delta_time):
        pass
        
        '''change = False 
        
        left = self.LEFT_Boundary + self.x_View
        right = self.RIGHT_Boundary + self.x_View
        
        if self.sprite1.center_x < left:
            self.x_View = self.x_View - self.movement_speed
            left = self.LEFT_Boundary - self.x_View
            right = self.RIGHT_Boundary - self.x_View
            change = True
        
        if self.sprite1.center_x > (right-25):
            self.x_View = self.x_View + self.movement_speed
            left = self.LEFT_Boundary - self.x_View
            change = True
        
        if change:
            arcade.set_viewport(self.x_View,SCREEN_WIDTH + self.x_View,0,SCREEN_HEIGHT)'''
Window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
Window.show_view(MainMenu())
arcade.run()





'''class Customized(arcade.View):
    def on_show(self):
        pass
    def on_mouse_press(self,key,modifier):
        pass
'''

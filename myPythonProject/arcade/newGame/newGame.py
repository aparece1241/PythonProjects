import arcade
import os

folder = os.path.dirname(os.path.abspath("wall.png"))
join = os.path.join(folder,"SpriteLists")
folder1 = os.path.dirname(os.path.abspath("head.png"))
join1 = os.path.join(folder1,"arcade")

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
                self.function()
                self.on_release()


class MainMenu(arcade.View):
    def play():
        Window.show_view(StartGame())
        
    Play = Button(305,260,150,50,arcade.color.AVOCADO,"Play",play,arcade.color.GREEN)
    Help = Button(390,200,150,50,arcade.color.AVOCADO,"Help",None,arcade.color.GREEN)
    Heroes = Button(485,260,150,50,arcade.color.AVOCADO,"Heroes",None,arcade.color.GREEN)
    backdrop1 = arcade.Sprite(os.path.join(join,"zombie.png"),center_x = 400,center_y = 400,scale = 0.8)
    hero = arcade.Sprite(os.path.join(join,"hero.page.png"),center_x = 680,center_y = 200)
    zombie = arcade.Sprite(os.path.join(join,"zombie.page.png"),center_x = 150,center_y = 150)
    background = arcade.SpriteList()
    button_list = []
    back = arcade.load_texture(os.path.join(join1,"image","square.png"))
    
    def on_show(self):
        arcade.set_background_color(arcade.color.BISTRE_BROWN)
        self.button_list.append(self.Play)
        self.button_list.append(self.Help)
        self.button_list.append(self.Heroes)
        self.background.append(self.hero)
        self.background.append(self.backdrop1)
        self.background.append(self.zombie)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.back)
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
    
    sprite = arcade.Sprite(os.path.join(join,"cloud1.png"),center_x = 600,center_y = 580)
    tile = arcade.Sprite(os.path.join(join,"tile.png"),center_x = 400,center_y = 150)
    tile1 = arcade.Sprite(os.path.join(join,"tile.png"),center_x = 400,center_y = 77)
    back = arcade.load_texture(os.path.join(join,"backdrop.game.png"))
    
    spritelist = []
    walls = arcade.SpriteList()


    
    #x_View = 0
    #y_View = 0
    change_x = 0
    change_y = 0
    movement_speed = 5
    #RIGHT_Boundary = SCREEN_WIDTH
    #LEFT_Boundary = 40
    
    player_list = arcade.SpriteList()
    player = arcade.AnimatedWalkingSprite()

    
    def setup(self):
        for i in range(0,800):
            if i % 40 == 0:
                self.wall1 = arcade.Sprite(os.path.join(join,"wall1.png"),center_x = i + 20 ,center_y = 205)
                self.wall2 = arcade.Sprite(os.path.join(join,"wall.png"),center_x = i + 20 ,center_y = 65)
                self.walls.append(self.wall1)
                self.walls.append(self.wall2)
                

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.back)
        self.sprite.draw()
        self.tile.draw()
        self.tile1.draw()
        self.walls.draw()

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

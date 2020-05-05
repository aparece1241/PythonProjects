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
                self.function()
                self.on_release()







        
        


class MainMenu(arcade.View):
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
    spriteList = arcade.SpriteList()
    sprite = arcade.AnimatedWalkingSprite()
    sprite.stand_left_textures = []
    sprite.stand_left_textures.append(arcade.load_texture("../../SpriteLists/characters/stickman1.png",mirrored = True))
    sprite.stand_right_textures = []
    sprite.stand_right_textures.append(arcade.load_texture("../../SpriteLists/characters/stickman1.png"))
    sprite.walk_left_textures = []
    sprite.walk_right_textures = []
    for i in range(1,4):
        sprite.walk_right_textures.append(arcade.load_texture(f"../../SpriteLists/characters/stickman{i}.png"))
        sprite.stand_right_textures.append(arcade.load_texture(f"../../SpriteLists/characters/stickman{i}.png"))
        sprite.walk_left_textures.append(arcade.load_texture(f"../../SpriteLists/characters/stickman{i}.png",mirrored = True))

    sprite.center_x = 300
    sprite.center_y = 300
    sprite.scale = 0.5
    spriteList.append(sprite)
    
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        
    def on_draw(self):
        arcade.start_render()
        self.spriteList.draw()
        
    def on_mouse_press(self,x,y,button,modifiers):
        pass
            
    def on_mouse_release(self,x,y,button,modifiers):
        pass

    
    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        pass
    
    def on_mouse_motion(self,x,y,dx,dy):
        pass

    
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.sprite.change_y = self.movement_speed
        if key == arcade.key.DOWN:
            self.sprite.change_y = -self.movement_speed
        if key == arcade.key.LEFT:
            self.sprite.change_x = -self.movement_speed
        if key == arcade.key.RIGHT:
            self.sprite.change_x = self.movement_speed
            
    def on_key_release(self, key, modifier):
        self.sprite.change_y = 0
        self.sprite.change_x = 0
    def on_update(self,delta_time):
        self.spriteList.update_animation()
        self.spriteList.update()



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

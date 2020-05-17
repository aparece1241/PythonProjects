import arcade
from time import sleep
# import os

# folder = os.path.dirname(os.path.abspath("wall.png"))
# join = os.path.join(folder,"SpriteLists")
# join1 = os.path.join(folder,"arcade")

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
        
    Play = Button(305,260,150,50,
    arcade.color.AVOCADO,"Play",
    play,arcade.color.GREEN)
    Help = Button(390,200,150,50,
    arcade.color.AVOCADO,"Help"
    ,None,arcade.color.GREEN)
    Heroes = Button(485,260,150,50,
    arcade.color.AVOCADO,"Heroes",
    None,arcade.color.GREEN)
    backdrop1 = arcade.Sprite("../../SpriteLists/zombie.png"
    ,center_x = 400,center_y = 400,scale = 0.8)
    hero = arcade.Sprite("../../SpriteLists/hero.page.png"
    ,center_x = 680,center_y = 200)
    zombie = arcade.Sprite("../../SpriteLists/zombie.page.png"
    ,center_x = 150,center_y = 150)
    background = arcade.SpriteList()
    button_list = []
    back = arcade.load_texture("../image/head.png")
    
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

            




# class enemyAnimation():
#     def __init__(self,center_x,center_y):
#         self.center_x = center_x
#         self.center_y = center_y
#         self.enemy = None
#         self.enemy_list = None
#         self.lifepoints = 100
#     def setup(self):
#         self.enemy = arcade.AnimatedTimeSprite()
#         self.enemy_list = arcade.SpriteList()
#         self.enemy.textures = []
#         for i in range(1,5):
#             self.enemy.textures.append(arcade.load_texture(f"../../SpriteLists/z{i}.png"))
        
#         self.enemy.center_x =  self.center_x
#         self.enemy.center_y = self.center_y
#         self.enemy.scale = 0.3
#         self.enemy.texture_change_frames = 20
#         self.enemy_list.append(self.enemy)









class StartGame(arcade.View):
    # def todo():
    #     pass
    # def todo1():
    #     pass
    # def todo2():
    #     pass
    

    # enemy = enemyAnimation(100,SCREEN_WIDTH * 0.15)
    cloud = arcade.Sprite("../../SpriteLists/cloud1.png",center_x = 600,center_y = 580)
    tile = arcade.Sprite("../../SpriteLists/tile.png",center_x = 400,center_y = 150)
    tile1 = arcade.Sprite("../../SpriteLists/tile.png",center_x = 400,center_y = 77)
    tile2 = arcade.Sprite("../../SpriteLists/tile.png",center_x = 400,center_y = 14)
    back = arcade.load_texture("../../SpriteLists/backdrop.game.png")
    tiles = arcade.SpriteList()
    tiles.append(tile)
    tiles.append(tile1)
    tiles.append(tile2)

    #enemy
    enemy = arcade.AnimatedTimeSprite()
    enemy_list = arcade.SpriteList()
    enemy.textures = []
    #enemy coming from left side
    for i in range(0,8):
        enemy.textures.append(arcade.load_texture(f"../../SpriteLists/z{i}.png"))
        
    enemy.center_x = 100
    enemy.center_y = SCREEN_HEIGHT * 0.15
    enemy.scale = 0.3
    enemy.texture_change_frames = 50
    enemy_list.append(enemy)
    




    spritelist = []
    walls = arcade.SpriteList()
    
    #x_View = 0
    #y_View = 0
    change_x = 0
    change_y = 0
    movement_speed = 5
    jump_speed = 10
    att = False
    #RIGHT_Boundary = SCREEN_WIDTH
    #LEFT_Boundary = 40
    

    player_list = arcade.SpriteList()
    attack = arcade.AnimatedWalkingSprite()
    player = arcade.AnimatedWalkingSprite()
    player.stand_right_textures = []
    player.stand_left_textures = []
    player.walk_left_textures = []
    player.walk_right_textures = []
    player.stand_left_textures.append(arcade.load_texture("../../SpriteLists/hero.walk.0.png",mirrored=True))
    player.stand_right_textures.append(arcade.load_texture("../../SpriteLists/hero.walk.0.png"))
    attack.stand_left_textures.append(arcade.load_texture("../../SpriteLists/z1.png",mirrored=True))
    attack.stand_right_textures.append(arcade.load_texture("../../SpriteLists/z1.png"))
    physics = None   
    attack.stand_left_textures=[]
    attack.stand_right_textures=[]
    attack.stand_left_textures.append(arcade.load_texture("../../SpriteLists/hero.fire.png"))
    attack.stand_right_textures.append(arcade.load_texture("../../SpriteLists/hero.fire.png",mirrored=True))
    






    for i in range(0,5):
        player.walk_right_textures.append(arcade.load_texture(f"../../SpriteLists/hero.walk.{i}.png"))
        player.walk_left_textures.append(arcade.load_texture(f"../../SpriteLists/hero.walk.{i}.png",mirrored=True))

    player.center_x = SCREEN_WIDTH/2
    player.center_y = SCREEN_WIDTH * 0.15
    player.scale = 0.3
    player_list.append(player)


    def setup(self):
        for i in range(0,800):
            if i % 40 == 0:
                self.wall1 = arcade.Sprite("../../SpriteLists/wall1.png",center_x = i + 20 ,center_y = 205)
                self.wall2 = arcade.Sprite("../../SpriteLists/wall.png",center_x = i + 20 ,center_y = 14)
                self.walls.append(self.wall1)
                self.walls.append(self.wall2)
                self.physics = arcade.PhysicsEngineSimple(self.player,self.walls)
                
               
    # def changes(self):
    #     counter = 0
    #     if self.change:
    #         self.player_list.remove(self.player)
    #         self.player_list.append(self.foo)
    #         counter = 1
    #     else:
    #         if counter == 1:
    #             self.player_list.remove(self.foo)
    #             self.player_list.append(self.player)

        

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.setup()

        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.back)
        self.cloud.draw()
        self.tiles.draw()
        self.walls.draw()
        self.player_list.draw()
        self.enemy_list.draw()
    def on_key_press(self,key,modifier):
        if key == arcade.key.LEFT:
            self.player.change_x = -self.movement_speed
        if key == arcade.key.RIGHT:
            self.player.change_x = self.movement_speed
        if key == arcade.key.UP:
            self.player.change_y = self.movement_speed
        if key == arcade.key.DOWN:
            self.player.change_y = -self.movement_speed
        if key == arcade.key.A:
            self.player_list.remove(self.player)
            self.attack.scale = 0.5
            self.attack.center_x = self.player.center_x
            self.attack.center_y = self.player.center_y
            self.player_list.append(self.attack)
            self.att = True
    def on_key_release(self,key,modifier):
        self.player.change_y = 0
        self.player.change_x = 0
        if key == arcade.key.A:
            self.player_list.remove(self.attack)
            self.player_list.append(self.player)
            self.att = False
    def on_update(self,delta_time):
        self.enemy_list.update()
        self.enemy_list.update_animation()
        self.player_list.update()
        self.player_list.update_animation() 
        self.physics.update() 


        #the running cloud 
        if self.cloud.center_x < -100 :
            self.cloud.center_x = 1000
        else:
            self.cloud.center_x -= 1
        
        if self.att :
            self.attack.update()
            self.attack.update_animation()

            
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

import arcade
import random

WIDTH = 600
HEIGHT = 400
level = {"Easy":0.3,"Medium":0.1,"Hard":0.09}
levels = ["Easy","Meduim","Hard"]

l = 0
class Buttons():
    def __init__(self,center_x,center_y,text,width,height,text_x,text_y,text_color,button_color):
        arcade.draw_rectangle_filled(center_x,center_y,width,height,color = button_color)
        arcade.draw_text(text,text_x,text_y,color = text_color,font_size = 15)
        arcade.draw_rectangle_outline(center_x,center_y,width,height,arcade.color.GRAY)
class Snake():
    def __init__(self):
        self.wall = arcade.SpriteList()
        self.snake_body = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.head = None
        self.head1 = arcade.SpriteList()
        self.location = []
        self.score = 0
    def setup(self):
        self.head = arcade.Sprite("image/head.png",center_x = 300,center_y = 200,scale = 0.0181)
        self.body = arcade.Sprite("image/square.png",center_x = 290,center_y = 200,scale = 0.0181)
        self.head1.append(self.body)
        for i in range(20,481):
            if(i % 10 == 0):
                self.wall1  = arcade.Sprite("image/wall.png",center_x = 120,center_y = i,scale = 0.006)
                self.wall2  = arcade.Sprite("image/wall.png",center_x = 480,center_y = i,scale = 0.006)
                self.wall3  = arcade.Sprite("image/wall.png",center_x = i,center_y = 380,scale = 0.006)
                self.wall4  = arcade.Sprite("image/wall.png",center_x = i,center_y = 20,scale = 0.006)
                if(i < 381):
                    self.wall.append(self.wall1)
                    self.wall.append(self.wall2)
                if(i >= 120):
                    self.wall.append(self.wall3)
                    self.wall.append(self.wall4)
    def random(self):
        while True:
            self.x = random.randrange(130,460)
            self.y = random.randrange(30,380)
            if( self.x % 10 == 0 and self.y % 10 == 0):
                return [self.x,self.y]
            
    def set_food(self):
        self.food = arcade.Sprite("image/food.png",center_x = self.random()[0],center_y = self.random()[1],scale = 0.018)
        self.food_list.append(self.food)
    def add_snake_body(self):
        self.body = arcade.Sprite("image/square.png",center_x = self.location[len(self.location) - 2][0],center_y = self.location[len(self.location) - 2][1],scale = 0.0181)
        self.snake_body.append(self.body)


        
        
            
            

class MainMenu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
    def on_draw(self):
        arcade.start_render()
        Buttons(300,250,"New Game",100,40,258,241,(234,53,3),arcade.color.GREEN)
        #button for level
        Buttons(300,200,"Level",100,40,280,191,(234,53,3),arcade.color.GREEN)
        #button for level
        Buttons(300,150,"Instruction",100,40,258,141,(234,53,3),arcade.color.GREEN)
        
    def on_mouse_press(self,x,y,button,modifier):
        print(x,y)
        #New Game
        if (x <= 350 and x >= 250):
            if(y <= 270 and y >= 230):
                self.Return = StartGame()
                self.window.show_view(self.Return)
        #level
        if (x <= 350 and x >= 250):
            if(y <= 220 and y >= 180):
                self.Return = Level()
                self.window.show_view(self.Return)
        #Instructions
        if (x <= 350 and x >= 250):
            if(y <= 170 and y >= 130):
                self.Return = Instruction()
                self.window.show_view(self.Return)
        
class Instruction(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)
        print(True)
    def on_draw(self):
        arcade.start_render()
        Buttons(50,350,"Back",70,30,33,341,(255,255,8),(35,75,4))
    def on_mouse_press(self,x,y,button,modifier):
        print(x,y)
        #For Back
        if (x <= 83 and x >= 13):
            if(y <= 367 and y >= 337):
                self.Return = MainMenu()
                self.window.show_view(self.Return)
        
class Level(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHEAT)
        print(True)
    def on_draw(self):
        arcade.start_render()
        Buttons(50,350,"Back",70,30,33,341,(255,255,8),(35,75,4))
        Buttons(300,250,"Easy",100,40,285,241,(234,53,3),arcade.color.GREEN)
        Buttons(300,200,"Medium",100,40,270,191,(234,53,3),arcade.color.GREEN)
        Buttons(300,150,"Hard",100,40,285,141,(234,53,3),arcade.color.GREEN)
        
    def on_mouse_press(self,x,y,button,modifier):
        print(x,y)
        #For Back
        if (x <= 83 and x >= 13):
            if(y <= 367 and y >= 337):
                self.Return = MainMenu()
                self.window.show_view(self.Return)
        #Easy
        if (x <= 350 and x >= 250):
            if(y <= 270 and y >= 230):
                self.Return = StartGame()
                self.Return.speed = level["Easy"]
                self.Return.l = 0
                self.Return.choose = True
                self.window.show_view(self.Return)
        #Meduim
        if (x <= 350 and x >= 250):
            if(y <= 220 and y >= 180):
                self.Return = StartGame()
                self.Return.speed = level["Medium"]
                self.Return.l = 1
                self.Return.choose = True
                self.window.show_view(self.Return)
        #Hard
        if (x <= 350 and x >= 250):
            if(y <= 170 and y >= 130):
                self.Return = StartGame()
                self.Return.speed = level["Hard"]
                self.Return.l = 2
                self.Return.choose = True
                self.window.show_view(self.Return)
      

        
class StartGame(arcade.View):
    Snake = Snake()
    Lvl = Level()
    change_x = 0
    change_y = 0
    recentKey = 0
    n = 0
    l = 0
    speed = 0.3
    stop = False
    choose = False
    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.Snake.setup()
        self.Snake.set_food()
        print(True)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300,200,370,370,arcade.color.DARK_GREEN)
        self.Snake.head.draw()
        self.Snake.head1.draw()
        self.Snake.snake_body.draw()
        self.Snake.food_list.draw()
        self.Snake.wall.draw()
        arcade.draw_rectangle_outline(60,220,100,300,arcade.color.WHITE)
        arcade.draw_text("Your Score:",15,350,arcade.color.BLACK,font_size = 15)
        arcade.draw_text(str(self.Snake.score),15,320,arcade.color.BLACK,15)
        
        arcade.draw_text("Your Level:",15,200,arcade.color.BLACK,font_size = 15)
        arcade.draw_text(levels[self.l],15,170,arcade.color.BLACK,15)
        
        arcade.draw_line(10,230,110,230,arcade.color.WHITE)
        arcade.draw_line(10,100,110,100,arcade.color.WHITE)

        arcade.draw_rectangle_outline(545,358,105,50,arcade.color.WHITE)
        arcade.draw_text("Press P to pause",494,350,arcade.color.BLACK)

    def on_mouse_press(self,x,y,button,modifier):
        print(x,y)

    def on_key_press(self,key,modifier):
        if(key == arcade.key.LEFT):
            if(self.recentKey == arcade.key.RIGHT):
                self.change_x = 10
            else:
                self.change_x = -10
                self.change_y = 0
                self.recentKey = key
                self.Snake.location.append([self.Snake.head.center_x,self.Snake.head.center_y])
                self.stop = False
                #print("left")
        if(key == arcade.key.RIGHT):
            if(self.recentKey == arcade.key.LEFT):
                self.change_x = -10
            else:
                self.change_x = 10
                self.change_y = 0
                self.recentKey = key
                self.Snake.location.append([self.Snake.head.center_x,self.Snake.head.center_y])
                self.stop = False
                #print("right")
        if(key == arcade.key.UP):
            if(self.recentKey == arcade.key.DOWN):
                self.change_y = -10
            else:
                self.change_x = 0
                self.change_y = 10
                self.recentKey = key
                self.Snake.location.append([self.Snake.head.center_x,self.Snake.head.center_y])
                self.stop = False
                #print("up")
        if(key == arcade.key.DOWN):
            if(self.recentKey == arcade.key.UP):
                self.change_y = 10
            else:
                self.change_x = 0
                self.change_y = -10
                self.recentKey = key
                self.Snake.location.append([self.Snake.head.center_x,self.Snake.head.center_y])
                self.stop = False
                #print("down")
        self.Snake.location.pop()
        self.n = 0
        
        #This part here when the player will going to pause the game
        if key == arcade.key.P:
           self.change_x = 0
           self.change_y = 0
           self.n = len(self.Snake.head1)
           self.stop = True
        
    def on_update(self,delta_time):
        arcade.pause(self.speed)
        self.Snake.head.center_x += self.change_x
        self.Snake.head.center_y += self.change_y
        
        ###########################################
        if self.stop == False:
            self.Snake.location.append([self.Snake.head.center_x,self.Snake.head.center_y])
        self.lenght = len(self.Snake.location)
        
        
        self.Snake.head1[0].center_x = self.Snake.location[self.lenght - 2][0]
        self.Snake.head1[0].center_y = self.Snake.location[self.lenght - 2][1]
            
        for i in range(self.n,len(self.Snake.snake_body)):
            self.Snake.snake_body[i].center_x = self.Snake.location[self.lenght - (i+2)][0]
            self.Snake.snake_body[i].center_y = self.Snake.location[self.lenght - (i+2)][1]

        #check for collision in food
        if(arcade.check_for_collision_with_list(self.Snake.head,self.Snake.food_list)):
            self.Snake.food_list[0].kill()
            self.Snake.score += 1
            self.Snake.set_food()

            
            #Adding the body of the snake
            if(self.Snake.score % 2 == 0):
                self.Snake.add_snake_body()
            if self.choose == False:
                if self.Snake.score == 10:
                    self.l = 1
                    self.speed = level["Medium"]
                if self.Snake.score == 20:
                    self.l = 2
                    self.speed = level["Hard"]
                
        #check for collision if Game over
        if(arcade.check_for_collision_with_list(self.Snake.head,self.Snake.wall) or arcade.check_for_collision_with_list(self.Snake.head,self.Snake.snake_body)):
            arcade.pause(0.5)
            self.Snake.food_list = arcade.SpriteList()
            self.Snake.snake_body = arcade.SpriteList()
            self.Snake.score = 0
            self.Snake.head1[0].kill()
            self.Return = GameOver()
            self.window.show_view(self.Return)
            
          
class GameOver(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.VIOLET)
        print(True)
    def on_draw(self):
        arcade.start_render()
        Buttons(250,180,"Restart",70,30,226,170,(255,255,8),(35,75,4))
        Buttons(370,180,"Back",70,30,350,170,(255,255,8),(35,75,4))
        
    def on_mouse_press(self,x,y,button,modifier):
        print(x,y)
        #For Back
        if (x <= 404 and x >= 334):
            if(y <= 196 and y >= 166):
                self.Return = MainMenu()
                self.window.show_view(self.Return)
                
        #For Restart
        if (x <= 284 and x >= 214):
            if(y <= 196 and y >= 166):
                self.Return = StartGame()
                self.window.show_view(self.Return)
                



window = arcade.Window(WIDTH,HEIGHT,"Snake")
main = MainMenu()  
window.show_view(main)
arcade.run()

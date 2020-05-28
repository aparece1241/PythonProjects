#
# import arcade
# from time import sleep
# import random
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 800
# SCREEN_TITLE = "Snake"
# score_storage = [12,21,42]
#
# class Snake:
#     def __init__(self,center_x,center_y,width,height):
#         self.position_x = center_x
#         self.position_y = center_y
#         self.width = width
#         self.height = height
#         self.s_position_x = self.position_x/2
#         self.s_position_y = self.position_y/2
#         self.new_x = self.position_x/2
#         self.new_y = self.position_y/2 - 20
#         self.sprite = None
#         self.sprite1 = None
#         self.sprite2 = None
#         self.location = []
#         self.score = 0
#         self.sprite_no = 2
#         self.check = False
#         self.x = 0
#         self.y = 0
#         self.snake_body = arcade.SpriteList()
#         self.number = 0
#         self.wall = arcade.SpriteList()
#         self.message = ""
#         self.message1 = ""
#         self.message2 = ""
#
#
#     def draw(self):
#         arcade.draw_rectangle_filled(self.position_x,self.position_y,height = self.height,
#                                      width = self.width,color = arcade.color.LIGHT_BLUE)
#         arcade.draw_text("Your score: " + str(self.score), 320,770,arcade.color.WHITE)
#         arcade.draw_text(self.message,330,330,arcade.color.RED)
#         arcade.draw_text(self.message1,150,250,arcade.color.BLACK)
#         arcade.draw_text(self.message2, 450,250,arcade.color.BLUE)
#
#     def snake(self):
#             self.sprite = arcade.Sprite("image/head.png",center_x = self.s_position_x,
#                                      center_y = self.s_position_y,scale = 0.035)
#             self.sprite1 = arcade.Sprite("image/square.png",center_x = self.new_x,
#                                      center_y = self.new_y,scale = 0.035)
#
#     def set(self):
#             if(self.score != 0):
#                 if(self.score % 2 == 0):
#                     self.sprite2 = arcade.Sprite("image/square.png",center_x = self.x,
#                                      center_y = self.y,scale = 0.035)
#                     self.snake_body.append(self.sprite2)
#                     self.number += 1
#                     #print(self.number)
#                     #print(self.snake_body[0].center_x,self.snake_body[0].center_y)
#
#
#
#
#
# class myWindow(arcade.Window):
#
#     def __init__(self,width,height,title):
#         super().__init__(width,height,title)
#         arcade.set_background_color(arcade.color.BLACK)
#         self.Snake = Snake(width/2,height/2,width - 100,height - 100)
#         self.change_x = 0
#         self.change_y = 0
#         self.key = 0
#         self.key1 = 0
#         self.minusX = 0
#         self.minusY = -20
#         self.food_list = arcade.SpriteList()
#         self.width = width
#         self.height = height
#         self.loc_length = 0
#         self.speed = 20
#         self.game_state = False
#
#
#
#
#
#     def restart(self):
#         self.Snake.score = 0
#         self.Snake.location = []
#         self.Snake.s_position_x = self.width/4
#         self.Snake.s_position_y = self.height/4
#         self.Snake.snake_body = arcade.SpriteList()
#         self.Snake.new_x = self.Snake.position_x/2
#         self.Snake.new_y = self.Snake.position_y/2 - 20
#         self.Snake.message = ""
#         self.Snake.message1 = ""
#         self.Snake.message2 = ""
#         self.change_x = 0
#         self.change_y = 0
#         self.Snake.wall = arcade.SpriteList()
#
#
#     def on_draw(self):
#         arcade.start_render()
#         self.Snake.draw()
#         self.Snake.snake()
#         self.Snake.sprite.draw()
#         self.Snake.sprite1.draw()
#         self.food_list.draw()
#         self.Snake.snake_body.draw()
#         self.Snake.wall.draw()
#
#
#     def on_key_press(self,key,modifier):
#
#         if(key == arcade.key.LEFT):
#             if(self.key == arcade.key.RIGHT):
#                 self.change_x = 20
#             else:
#                 self.change_x = -self.speed
#                 self.change_y = 0
#                 self.key = key
#                 self.Snake.new_x = self.Snake.s_position_x
#                 self.Snake.new_y = self.Snake.s_position_y
#                 self.minusX = 20
#                 self.minusY = 0
#                 self.Snake.location.append([self.Snake.s_position_x,self.Snake.s_position_y])
#
#         elif(key == arcade.key.RIGHT):
#             if(self.key == arcade.key.LEFT):
#                 self.change_x = -20
#             else:
#                 self.change_x = self.speed
#                 self.change_y = 0
#                 self.key = key
#                 self.Snake.new_x = self.Snake.s_position_x
#                 self.Snake.new_y = self.Snake.s_position_y
#                 self.minusX = -20
#                 self.minusY = 0
#                 self.Snake.location.append([self.Snake.s_position_x,self.Snake.s_position_y])
#
#         elif(key == arcade.key.UP):
#             if(self.key == arcade.key.DOWN):
#                 self.change_y = -20
#             else:
#                 self.change_y = self.speed
#                 self.change_x = 0
#                 self.key = key
#                 self.Snake.new_x = self.Snake.s_position_x
#                 self.Snake.new_y = self.Snake.s_position_y
#                 self.minusX = 0
#                 self.minusY = -20
#                 self.Snake.location.append([self.Snake.s_position_x,self.Snake.s_position_y])
#
#         elif(key == arcade.key.DOWN):
#             if(self.key == arcade.key.UP):
#                 self.change_y = 20
#             else:
#                 self.change_y = -self.speed
#                 self.change_x = 0
#                 self.key = key
#                 self.Snake.new_x = self.Snake.s_position_x
#                 self.Snake.new_y = self.Snake.s_position_y
#                 self.minusX = 0
#                 self.minusY = 20
#                 self.Snake.location.append([self.Snake.s_position_x,self.Snake.s_position_y])
#         self.Snake.location.pop()
#         if(self.game_state):
#             score_storage.append(self.Snake.score)
#             if(key == arcade.key.R):
#                 self.Snake.check = True
#             elif(key == arcade.key.SPACE):
#                 print(self.game_state)
#                 self.restart()
#                 arcade.close_window()
#
#
#
#
#     def setup(self):
#         while True:
#             self.food_x = random.randrange(80,720)
#             self.food_y = random.randrange(80,720)
#             if(self.food_x % 20 == 0 and self.food_y % 20 == 0):
#                 self.food = arcade.Sprite("image/food.png",center_x = self.food_x,center_y = self.food_y,scale = 0.035)
#                 break;
#             else:
#                 continue;
#         for i in range(1):
#             self.food_list.append(self.food)
#
#     def wall(self):
#         # this is for the left wall
#         for i in range(60,760):
#             if(i % 20 == 0):
#                 self.wall1 = arcade.Sprite("image/wall.png",center_x = 60,center_y = i,scale = 0.0211)
#                 self.wall2 = arcade.Sprite("image/wall.png",center_x = 740,center_y = i,scale = 0.0211)
#                 self.wall3 = arcade.Sprite("image/wall.png",center_x = i,center_y = 60,scale = 0.0211)
#                 self.wall4 = arcade.Sprite("image/wall.png",center_x = i,center_y = 740,scale = 0.0211)
#                 self.Snake.wall.append(self.wall1)
#                 self.Snake.wall.append(self.wall2)
#                 self.Snake.wall.append(self.wall3)
#                 self.Snake.wall.append(self.wall4)
#
#     def Update(self):
#         if(self.Snake.score > 1):
#             for i in range(self.Snake.number):
#                 self.Snake.snake_body[i].center_x = self.Snake.location[self.loc_length - (i+2)][0]
#                 self.Snake.snake_body[i].center_y = self.Snake.location[self.loc_length - (i+2)][1]
#
#
#
#     def on_update(self,delta_time):
#         # this part controls the speed of my snake
#         self.Snake.location.append([self.Snake.s_position_x,self.Snake.s_position_y])
#         sleep(0.1)
#         self.Snake.s_position_x += self.change_x
#         self.Snake.s_position_y += self.change_y
#         self.loc_length = len(self.Snake.location)
#         self.Snake.x = self.Snake.location[self.loc_length -1][0]
#         self.Snake.y = self.Snake.location[self.loc_length -1][1]
#         self.food_list.update()
#         self.Update()
#
#
#
#
#         # This is the logic when the snake turn to left,right,up,or down
#         if(self.Snake.s_position_x <= self.Snake.new_x or self.Snake.s_position_y <= self.Snake.new_y):
#             self.Snake.new_x = self.Snake.s_position_x + self.minusX
#             self.Snake.new_y = self.Snake.s_position_y + self.minusY
#         else:
#             self.Snake.new_x = 0
#             self.Snake.new_y = 0
#         self.Snake.snake()
#
#         # This part checks the collision of the head of th snake to the sprite food
#         if arcade.check_for_collision_with_list(self.Snake.sprite,self.food_list):
#             self.food_list[0].kill()
#             self.Snake.score += 1
#             self.setup()
#             self.Snake.set()
#
#
#         # When the snake hit the wall or When the head collides with its body #
#         if arcade.check_for_collision_with_list(self.Snake.sprite,self.Snake.wall) or arcade.check_for_collision_with_list(self.Snake.sprite,self.Snake.snake_body):
#             self.Snake.message = "Game Over!"
#             self.Snake.message1 = "Press any key except R to exit"
#             self.Snake.message2 = "Press R to Restart"
#             self.speed = 0
#             self.change_x = 0
#             self.change_y = 0
#             arcade.pause(seconds = 0.5)
#             self.game_state = True
#
#         if(self.Snake.check):
#             self.restart()
#             arcade.close_window()
#             self.Snake.check = False
#             self.game_state = False
#             window = myWindow(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
#             window.setup()
#             window.wall()
#             arcade.run()
#         self.Snake.snake_body.update()
#
# def start():
#     window = myWindow(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
#     window.setup()
#     window.wall()
#     arcade.run()
# start()
#
#
#
#

# ts= []
# class testing():
#     def __init__(self,num):
#         self.num = num
#
#     def printNum(self):
#         print(self.num)
#
# for i in range(10):
#     t = testing(i)
#     ts.append(t)
#
# ts[1].printNum()

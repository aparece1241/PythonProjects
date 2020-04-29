import arcade

class Button(arcade.TextButton):
    '''Where we get the buttons that we created'''
    def __init__(self,cx,cy,width,height,text,fontSize,fcolor,hcolor,
                 scolor,theme = None):
        super().__init__(cx,cy,width,height,text = text,
                         font_size = fontSize,face_color = fcolor,
                         highlight_color = hcolor,shadow_color = scolor)
        
class Testing(arcade.Window):
    def __init__(self,width,height,text):
        super().__init__(width,height,text)
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHEAT)
        self.button = Button(400,300,100,50,"Click me",15,arcade.color.GREEN,arcade.color.GRAY,
                             arcade.color.GRAY)
        

    def on_draw(self):
        arcade.start_render()
        self.button.draw()
    def on_update(self,delta_time):
        pass;
    def on_mouse_press(self,x,y,button,modifier):
        self.button.check_mouse_press(x,y)

Testing(800,600,"Testing")
arcade.run()

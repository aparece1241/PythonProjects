from tkinter import *
import json
from os import path

########DATA AND FUNCTION ######
Screen = Tk()
data =[{
    "user":"admin",
    "pass":"1234"
    }
    ]

file =[]

def exist():
    with open("data.txt","r+") as read:
       arr = json.load(read)
       return arr


def run(message):
    l3 = Label(Screen,text = message)
    l3.place(x= 60,y=120)
    Screen.withdraw()

def player():
    window = Tk()
    window.title("Welcome")
    window.resizable(0,0)
    l1= Label(window,text = "Welcome Player")
    l1.place(x=50,y=5)
    l2 = Label(window,text = " Snake Game")
    l2.place(x = 10,y=20)
    b1 = Button(window,bg="#336f91",fg = "white",text = "Snake", command = lambda:startGame())
    b1.place(x=10,y=50)
    window.mainloop()

def admin():
    window = Tk()
    window.title("Welcome")
    window.resizable(0,0)
    l1= Label(window,text = "Welcome Manager")
    l1.place(x=45,y=40)
    window.mainloop()

def creat():
    with open("data.txt","w+") as created:
        json.dump(data , created)
    
if path.exists("data.txt"):
    print("reading")
    file = exist()
else:
    print("creating")
    creat()
    file = exist()

def startGame():
    snake.start()
    print(snake.score_storage)

def check(array,userIn,passwrd):
     for i in array:
         if "admin" == userIn and "1234" == passwrd:
               message = "connected"
               run(message)
               admin()
         else:
             if i["user"] == userIn and i["pass"] == passwrd:
                 message = "connected"
                 run(message)
                 player()
                 
             else:
                 message = "password or user name is wrong"
                 l3 = Label(Screen,text = message)
                 l3.place(x=10,y=120)
                 
             message = ""

def click(user,passwd):
    check(file,user.get(),passwd.get())

def getAndAdd(user,passwd,window):
    print(user,passwd)
    acc = {"user":"","pass":""}
    acc["user"] = user
    acc["pass"] = passwd
    file.append(acc)
    with open("data.txt","w+") as created:
        json.dump(file , created)
    window.withdraw()
    Screen.deiconify()
    message = "Sign in to your account now"
    l3 = Label(Screen,text = message)
    l3.place(x=25,y=130)
    
def signUpForm():
    Screen.withdraw()
    window1 = Tk()
    window1.title("Sign up")
    window1.resizable(0,0)
    l1 = Label(window1,text ="Sign Up Here", bg="green",fg ="yellow")
    l1.place(x=65,y=20)
    l2 = Label(window1,text="Enter User Name",fg ="grey")
    l2.place(x=55,y=50)
    e1 = Entry(window1,fg="green")
    e1.place(x=40,y=70)
    l3 = Label(window1,text = "Enter Password",fg ="grey")
    l3.place(x=55,y=90)
    e2 = Entry(window1,fg="green")
    e2.place(x=40,y=110)
    b1 = Button(window1,text="Submit",command = lambda: getAndAdd(e1.get(),e2.get(),window1))
    b1.place(x=75,y=140)
    window1.mainloop()
    

def start():
    Screen.title("Login")
    Screen.resizable(0,0)
    l1 = Label(Screen,text="Enter your Username",fg="grey")
    l1.place(x=40,y=10)
    e1 = Entry(Screen,fg = "green")
    e1.place(x=40, y = 30)
    l2 = Label(Screen,text="Enter Password",fg="grey")
    l2.place(x = 40,y = 50)
    e2 = Entry(Screen,show ="*", fg = "green")
    e2.place(x = 40,y=70)
    b1 = Button(Screen,bg = "#339156",fg = "white",text = "Sign in", command = lambda: click(e1,e2))
    b1.place(x = 40,y = 100)
    b2 = Button(Screen,bg="#336f91",fg = "white",text = "Sign up",command = lambda: signUpForm())
    b2.place(x = 110,y=100)
    Screen.mainloop()
    
start()

######################################################














from tkinter import *
from os import access, close, path, read
from tkinter.colorchooser import *
import tkinter.messagebox
from typing import Counter, Sized
from tkinter.filedialog import *
import winsound
import time
from PIL import ImageTk, Image
from functools import partial
#from operator import itemgetter
import pickle
from time import time

'''
text = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh']
word = text[0]
ip = ""
index = 0
num = 0
start_pic = True
game = Tk()
state = "idle"


class GameInput:
    
    def __init__(self, key):
        self.active_animation = True
        self.c = Label(game, bg = "#E9E8C8")
        for i in range(0, 3):
            Label(game, text = "",background="#E9E8C8").grid(row = i, column = 0)
        self.showWord()
        animation.run()

    def showWord(self):
        global word
        for n in range(0, 20):
            Label(game, text = " ", font = "30",background="#E9E8C8").grid(row = 3, column = n)
        for n in range(0, len(word)):
            Label(game, text = word[n], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = n)
        Label(game, text = '                                      ', font = "30",background="#E9E8C8").place(x = 0, y = 90)
        Label(game, text = f'Next word : {text[num + 1]}', font = "30",background="#E9E8C8").place(x = 0, y = 90)

    def onKeyPress(self, event):
        global index, ip
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(game, text = word[index], font = "30", fg = "black",background="#E9E8C8").grid(row = 3, column = index)
            else:
                Label(game, text = word[index], font = "30", fg = "red",background="#E9E8C8").grid(row = 3, column = index)
            index += 1
        print(event.char)

    def pressBackSpace(self, event):
        global index, ip
        print("backspace")
        if index != 0:
            index -= 1
            ip = ip[:-1]
            Label(game, text = word[index], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = index)
        
    def pressEnter(self, event):
        global index, num, word, ip, start_pic, state
        Label(game, text = '                   ', font = "30",background="#E9E8C8").place(x = 0, y = 35)
        start_pic = False
        if ip == word:
            state = "good"
            print("correct")
            Label(game, text = "correct", fg = "green", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()

        else:
            state = "bad"
            print("incorrect")
            Label(game, text = "incorrect", fg = "red", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()

        ip = ""
        index = 0
        num += 1
        word = text[num]
        self.showWord()


class App(GameInput):

    def __init__(self, key):
        self.currentFrame_good = 0
        self.currentFrame_bad = 179
        self.currentFrame_default = 255

        self.break_good = 0
        self.pinPhoto = Label(game, bg = "#E9E8C8")


   # def playsong(self):
    #    winsound.PlaySound("//Users//Pun Punyawat//OneDrive//Desktop//2D//datastr//game//song_noodle.wav",winsound.SND_ASYNC)
        

    def run(self):
        global state, start_pic
        if state == "idle":
            #print("idle work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_default += 1
            image=Image.open("pic_png/animation_png/default/eat-"+str(self.currentFrame_default)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_default == 271:
                self.currentFrame_default = 255
                #state = "idle"
                print(state)
            if state == "idle":
                game.after(10, self.run)

        elif state == "good":
            #print("good work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_good += 1
            image=Image.open("pic_png/animation_png/good//eat-"+str(self.currentFrame_good)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_good == 40:
                self.currentFrame_good = 0
                state = "idle"
                #start_pic = True
                print(state)
                return 
            if state == "good":
                game.after(10, self.run)

        elif state == "bad":
            #print("bad work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_bad += 1
            image=Image.open("pic_png//animation_png//bad//eat-"+str(self.currentFrame_bad)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_bad == 220:
                self.currentFrame_bad = 179
                state = "idle"
                #start_pic = True
                print(state)
                return
            if state == "bad":
                game.after(10, self.run)

    def countdowntime(self,count_time):
        labeltime = Label(game,text=count_time,background="#E9E8C8");
        labeltime.place(x=250,y=150);

        if(count_time > 0):
            game.after(1000,self.countdowntime,count_time-1);

        else:
            confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
            if(confirm=="ok"):
                game.destroy()   # ani.countdowntime(15) #นับเวลา


'''

#https://stackoverflow.com/questions/23949906/highscores-using-python-saving-10-highscores-and-ordering-them    hiscore

def highscore_read():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def highscore_write():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def sc():
    global score
    print(score)
    score +=1

def validateLogin(username):
   print("username entered :", username.get())
   return

def quit1():
        root.destroy()

def quit2():
        window2.destroy()
def quit3():
        window1.destroy()

def showMainMenu():
    global root

    global pinPhoto1
    root = Tk()
    root.geometry("1000x400")
    pinPhoto1 = Label(root,bg = "#E9E8C8")
    #bg1 = PhotoImage(file = "pic/st2.png")

    root.title("Game")
    pinPhoto1.place(x = 0, y = 0)
    image=Image.open("pic/st2.png")
    #image = image.resize((1000, 400), Image.ANTIALIAS)
    picture = ImageTk.PhotoImage(image)
    pinPhoto1["image"] = picture
    pinPhoto1.image = picture
    #canvas1 = Canvas( root, width = 1000,height = 400)
    #canvas1.pack(fill = "both", expand = True)
    #canvas1.create_image( 0, 0, image = bg1,  anchor = "nw")
    usernameLabel = Label(root, text="User Name",fg="#FAAF30",font=('Tahoma', 15, 'bold'),bg="#FFF6F0").place(x=427, y=100)
    
    global username
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username).place(x=547, y=110)
    buttonN()
    global validateLogin
    validateLogin = partial(validateLogin, username)
    cWin()
    root.mainloop()

def showWindowMenu1():
    global window1 
    window1 = Tk()  
    pinPhotomode = Label(window1,bg = "#E9E8C8")
    window1.geometry('1000x400')  
    window1.title('PLAY')
    #bg3 = PhotoImage(file = "pic/mode.png")

    pinPhotomode.place(x = 0, y = 0)
    image=Image.open("pic/mode.png")
    #image = image.resize((1000, 400), Image.ANTIALIAS)
    picture = ImageTk.PhotoImage(image)
    pinPhotomode["image"] = picture
    pinPhotomode.image = picture

    #canvas3 = Canvas( window1, width = 1000,height = 400)
    #canvas3.pack(fill = "both", expand = True)
    #canvas3.create_image( 0, 0, image = bg3,  anchor = "nw")
    #window1.after(1000,sc())
    #window1.after(1000,sc())

    user = Label(window1,text = username.get()+"    Score :     "+str(score),font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    '''
    myMenu1 = Menu()
    menuItem1 = Menu(tearoff=0)
    menuItem1.add_command(label="Hard" , command=lambda:[quit2(),showWindowMenu4()])
    menuItem1.add_command(label="Normal")
    menuItem1.add_command(label="Easy")
    myMenu1.add_cascade(label="Mode",menu=menuItem1,)
    window1.config(menu=myMenu1)
    '''
    myLable5 = Button(text="PLAY",fg="#FFF6F0",font=('Tahoma', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[quit3(),showMainMenu()]).place(x=880, y=320)
    window1.mainloop()

def hide(x):
    x.pack_forget()

def showWindowMenu2():
    global window2
    window2 =Tk()
    pinPhotohowto = Label(window2,bg = "#E9E8C8")
    window2.title("HOW TO")
    window2.geometry("1000x400")
    #bg2 = PhotoImage(file = "pic/howto.png")
    pinPhotohowto.place(x = 0, y = 0)
    image=Image.open("pic/howto.png")
    #image = image.resize((1000, 400), Image.ANTIALIAS)
    picture = ImageTk.PhotoImage(image)
    pinPhotohowto["image"] = picture
    pinPhotohowto.image = picture
    #canvas2 = Canvas( window2, width = 1000,height = 400)
    #canvas2.pack(fill = "both", expand = True)
    #canvas2.create_image( 0, 0, image = bg2,  anchor = "nw")
 
    global myLable4
    myLable4 = Button(text="BACK",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quit2(),showMainMenu()]).place(x=30, y=320)

    window2.mainloop()
def showWindowMenu3():
    window3 =Tk()
    window3.title("SCORE")
    window3.geometry("1000x400")
    window3.mainloop()
def showWindowMenu4():
    window4 =Tk()
    window4.title("HARD")
    window4.geometry("1000x400")
    user = Label(window4,text = username.get()+"    Score :",font=('Tahoma', 20, 'bold')).place(x=0,y=0)
    window4.mainloop()
    myMenu2 = Menu()
    menuItem2 = Menu(tearoff=0)
    menuItem2.add_command(label="Food")
    menuItem2.add_command(label="Animal")
    menuItem2.add_command(label="Fruit")
    menuItem2.add_command(label="Internal Organs")
    menuItem2.add_command(label="Family")
    menuItem2.add_command(label="Occupations")
    menuItem2.add_command(label="Places")
    myMenu2.add_cascade(label="Category",menu=menuItem2)
    window4.config(menu=myMenu2)
    window4.mainloop()
def cWin():
    global check
    if check == True:
        print("window on")
        root.geometry("1000x400")
        check = False
    return check

def buttonN():
    myLable1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[validateLogin(),quit1(),showWindowMenu1()]).place(x=537, y=175)
    myLable2 = Button(text="HOW TO",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quit1(),showWindowMenu2()]).place(x=514, y=245)
    myLable3 = Button(text="EXIT",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quit1).place(x=539, y=315)
    return

def main():
    animation = App(game)
    inp = GameInput(game)
   

    game.bind("<Return>", inp.pressEnter)
    game.bind("<BackSpace>", inp.pressBackSpace)
    game.bind("<KeyPress>", inp.onKeyPress)

    game.title("Noodle game")
    game.geometry("1000x800")

    game.config(bg = "#E9E8C8")

# animation.playsong()
    animation.countdowntime(15)
    game.mainloop()


#https://stackoverflow.com/questions/23949906/highscores-using-python-saving-10-highscores-and-ordering-them 

#-----------------------------------------------Main

check = True
score = 0
highscore_read()
showMainMenu()

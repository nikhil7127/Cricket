from tkinter import *
from tkinter import font


window = Tk() 
def login():
    i=0
    def account():
        import signup
    with open("account_info.txt","r") as acc:
        acc = acc.read()
        acc = acc.split("\n")
        user = acc[0]
        password = acc[1]
        if (user!=enter_user.get()):
            Label(window,text="wrong username",bg ="#F78181").place(x=200,y=210)
            i-=1
        if(user==enter_user.get()):
            Label(window,text="                                           ",bg ="#81DAF5").place(x=200,y=210)
            i +=1
        if(password!=enter_pass.get()):
            Label(window,text="wrong password",bg ="#F78181").place(x=200,y=240)
            i-=1
        if(password==enter_pass.get()):
            Label(window,text="                                           ",bg ="#81DAF5").place(x=200,y=240)
            i+=1
        if(i<2):
            Label(window,text="Username and Password doesn't match",bg="#81DAF5").place(x=150,y=270)
            Button(window,text="Create Account",command=account).place(x=200,y=300)
        if(i==2):
            Label(window,text="                                                                          ",bg="#81DAF5").place(x=150,y=270)
            Label(window,text="                                                                          ",bg="#81DAF5",height=2).place(x=200,y=300)
            import MainGame
def display():
    
    #main_window
    global enter_user,enter_pass
    window.geometry("500x350")
    window.title("login")
    window["bg"] = "#81DAF5"
    Font = font.Font(family='Times', size=12, weight='bold',slant="italic",underline=1)
    Label(window,font=Font,text="LOGIN DETAILS",bg = "#81DAF5",fg ="#000000").pack()
    Label(window,text="",bg="#81DAF5").pack()
    #user name
    Label(window,text=" USERNAME ",height = 1,width=17,bg="#81DAF5").pack()
    enter_user = Entry(window)
    enter_user.pack()
    Label(window,text="",bg = "#81DAF5").pack()

    #password
    Label(window,text=" PASSWORD ",height = 1,width=17,bg="#81DAF5").pack()
    enter_pass = Entry(window,show="*")
    enter_pass.pack()
    Label(window,text=" ",bg = "#81DAF5").pack()

    #button
    Button(window,text="submit!",command=login,height=1,width=10,activebackground="#088A08").pack()
    window.mainloop()
   

display()

from tkinter import *


window = Tk()
window.geometry("500x400")
window.title("Main Menu")
def rules():
    import Rules
def login():
  import Login
def signin():
    import signup
def toss_choose():
    import MainGame
def button():
    Label(window,text="------MAIN MENU----------").pack()
    Label(window,text="      ").pack()
    Button(window,text="Rules",width='15',height="1",command=rules).pack()
    Label(window,text="      ").pack()
    Button(window,text="newGame",width='15',height="1",command=toss_choose).pack()
    Label(window,text="      ").pack()
    Button(window,text="Login",width='15',height="1",command =login).pack()
    Label(window,text="      ").pack()
    Button(window,text="Create Account",width='15',height="1",command=signin).pack()
    Label(window,text="      ").pack()
    Button(window,text="Exit",width='15',height="1",command=window.quit).pack()
    window.mainloop()
if __name__ == "__main__":
    button()




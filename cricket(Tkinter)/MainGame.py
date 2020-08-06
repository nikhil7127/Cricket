from tkinter import *
from tkinter import font
import random as r 

window =Tk()
window.geometry("700x600")
def toss():
    Label(window,text=" ",height=10,width=600).place(x=0,y=0)
    def head():
        toss_c=["Head","Tail"]
        a = r.randint(0,1)
        toss = toss_c[a]
        b_bo = ["BAT","BOWL"]
        b = r.randint(0,1)
        b_b = b_bo[b]
        if toss=="Head":
            Label(window,text=f"YOU WON THE TOSS  ").place(x=180,y=200)
            Label(window,text=" SELECT YOUR OPTION ",font=text).place(x=100,y=20)
            b1["state"] = DISABLED
            b2["state"] = DISABLED
            Button(window,text="BAT",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=bat).place(x=30,y=100)
            Button(window,text="BOWl",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=bowl).place(x=450,y=100)
        else:
            Label(window,text=f"YOU LOSS THE TOSS").place(x=180,y=200)
            Label(window,text=f"OPPONENT SELECT TO {b_b} first",font=text).place(x=100,y=450)
            if(b_b == "BAT"):
                bat()
            if(b_b == "BOWL"):
                bowl()
    def tail():
        toss_c=["Head","Tail"]
        a = r.randint(0,1)
        toss = toss_c[a]
        b_bo = ["BAT","BOWL"]
        b = r.randint(0,1)
        b_b = b_bo[b]
        if toss=="Tail":
            Label(window,text=f"YOU WON THE TOSS  ").place(x=180,y=200)
            Label(window,text=f" SELECT YOUR OPTION ").place(x=380,y=200)
            Button(window,text="BAT",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=bat).place(x=30,y=100)
            Button(window,text="BOWl",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=bowl).place(x=450,y=100)
        else:
            Label(window,text=f"YOU LOSS THE TOSS").place(x=380,y=200)
            Label(window,text=f"OPPONENT SELCET TO {b_b} FIRST",font=text).place(x=10,y=350)
            if(b_b == "BAT"):
                bat()
            if(b_b == "BOWL"):
                bowl()
    
    text= font.Font(family="Serif",size=30,underline=1)
    Label(window,text=" IT'S TOSS TIME ",font=text).place(x=180,y=20)
    b1 =Button(window,text="Head",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=head)
    b1.place(x=30,y=100)
   
    b2 = Button(window,text="Tail",width=20,height=2,bg="#0B0B3B",fg="white",activebackground="green",command=tail)
    b2.place(x=450,y=100)
def helps():
    import Rules
def bat():
    import bat
def bowl():
    print("bowl")
   
def select_mode():
    texts= font.Font(family="Serif",size=30,underline=1)
    Label(window,text="select number of over",font=texts).pack()
    b_help=Button(window,text="?",command=helps,width=3)
    b_help.place(x=660,y=10)
    b_help.bind("<Enter>",lambda e : Label(window,text="help").place(x=660,y=40))
    b_help.bind("<Leave>",lambda e : Label(window,text="           ").place(x=660,y=40))
    Button(window,text="1 Over",command=levels,width=10).place(x=10,y=100)
    Button(window,text="2 Over",command=levels,width=10).place(x=148,y=100)
    Button(window,text="5 Over",command=levels,width=10).place(x=306,y=100)
    Button(window,text="10 Over",command=levels,width=10).place(x=464,y=100)
    Button(window,text="20 Over",command=levels,width=10).place(x=610,y=100)
def levels():
    Label(window,text="  " ,width=700,height=10).place(x=0,y=0)
    texts= font.Font(family="Serif",size=30,underline=1)
    Label(window,text=" Choose Level ",font=texts).place(x=200,y=10)
    b_help=Button(window,text="?",command=helps,width=3)
    b_help.place(x=660,y=10)
    b_help.bind("<Enter>",lambda e : Label(window,text="help").place(x=660,y=40))
    b_help.bind("<Leave>",lambda e : Label(window,text="           ").place(x=660,y=40))
    Button(window,text="EASY",width=10,command=toss,bg="green").place(x=10,y=100)
    Button(window,text="MEDIUM",width=10,command=toss,bg="yellow").place(x=306,y=100)
    Button(window,text="HARD",width=10,command=toss,bg="red").place(x=610,y=100)
    
if __name__ == "__main__":
    select_mode()
    window.mainloop()  


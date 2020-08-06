from tkinter import *
from tkinter import font
def rules_all():
    window = Tk()
    window.geometry("500x500")
    window.title("login")
    window["bg"] = "#F2E480"
    Font_head = font.Font(family='Times', size=25, weight='bold',slant="italic",underline=1)
    Label(window,font=Font_head,text="- - - - - - - RULES - - - - - -",bg = "#F2E480",fg ="#000000").pack()
    Label(window,text=" ",bg="#F2E480").pack()
    font_h1=font.Font(family="Serif",size=14,slant="italic",underline=1)
    Label(window,text="Format ",font=font_h1,bg="#F2E480",fg="red").pack()
    Label(window,text="--> FIVE TYPES OF FORMATS : ",bg="#F2E480").place(x=0,y=100)

    def one():
        Label(window,text="--------------- EASY ---------------",bg="#F2E480").place(x=150,y=265)
        Label(window,text="OVERS ----VS---- WICKETS",bg="#F2E480").place(x=180,y=285)
        Label(window,text="    1             -----           2",bg="#F2E480").place(x=180,y=305)
        Label(window,text="    2             -----           3",bg="#F2E480").place(x=180,y=325)
        Label(window,text="    5             -----           4",bg="#F2E480").place(x=180,y=345)
        Label(window,text="   10             -----          5",bg="#F2E480").place(x=180,y=365)
        Label(window,text="   20            -----           10",bg="#F2E480").place(x=180,y=385)
    def two():
        Label(window,text="--------------- MEDIUM ---------------",bg="#F2E480").place(x=150,y=265)
        Label(window,text="OVERS ----VS---- WICKETS",bg="#F2E480").place(x=180,y=285)
        Label(window,text="    1             -----           2",bg="#F2E480").place(x=180,y=305)
        Label(window,text="    2             -----           2",bg="#F2E480").place(x=180,y=325)
        Label(window,text="    5             -----           3",bg="#F2E480").place(x=180,y=345)
        Label(window,text="   10             -----          4",bg="#F2E480").place(x=180,y=365)
        Label(window,text="   20            -----           8  ",bg="#F2E480").place(x=180,y=385)
    def thr():
        Label(window,text="--------------- HARD ---------------",bg="#F2E480").place(x=150,y=265)
        Label(window,text="OVERS ----VS---- WICKETS",bg="#F2E480").place(x=180,y=285)
        Label(window,text="    1             -----           1",bg="#F2E480").place(x=180,y=305)
        Label(window,text="    2             -----           2",bg="#F2E480").place(x=180,y=325)
        Label(window,text="    5             -----           2",bg="#F2E480").place(x=180,y=345)
        Label(window,text="   10             -----          4",bg="#F2E480").place(x=180,y=365)
        Label(window,text="   20            -----           6   ",bg="#F2E480").place(x=180,y=385)

    #button_format
    Button(window,text="1 Over",fg="#3B0B24",bg="#F781BE").place(x=10,y=135)
    Button(window,text="2 Overs",bg="#F781BE",fg="#DF0174").place(x=115,y=135)
    Button(window,text="5 Overs",bg="#FA58AC",fg="white").place(x=220,y=135)
    Button(window,text="10 Overs",fg="#F781BE",bg="#DF0174").place(x=325,y=135)
    Button(window,text="20 Overs",bg="#3B0B24",fg="#F781BE").place(x=430,y=135)
    Label(window,text=" ",bg="#F2E480").pack()
    Label(window,text=" --> GAME LEVELS : ",bg="#F2E480").place(x=0,y=185)

    def enter1(e):
        Label(window,text="click for more info...",bg="#F2E480").place(x=10,y=245)
    def leave1(e):
        Label(window,text="                                              ",bg="#F2E480").place(x=10,y=245)
    def enter2(e):
        Label(window,text="click for more info...",bg="#F2E480").place(x=210,y=245)
    def leave2(e):
        Label(window,text="                                                                              ",bg="#F2E480").place(x=120,y=245)
    def enter3(e):
        Label(window,text="click for more info...",bg="#F2E480").place(x=370,y=245)
    def leave3(e):
        Label(window,text="                                              ",bg="#F2E480").place(x=370,y=245)
    b1=Button(window,text="EASY",width=10,bg="green",command=one)
    b1.place(x=10,y=215)
    b1.bind("<Enter>",enter1)
    b1.bind('<Leave>',leave1)
    b2=Button(window,text="MEDIUM",width=10,bg="yellow",command=two)
    b2.place(x=210,y=215)
    b2.bind("<Enter>",enter2)
    b2.bind('<Leave>',leave2)
    b3=Button(window,text="HARD",width=10,bg="red",command=thr)
    b3.place(x=410,y=215)
    b3.bind("<Enter>",enter3)
    b3.bind('<Leave>',leave3)
    window.mainloop()

rules_all()

from tkinter import *
from tkinter import font
import random as r
sc_list =[1,2,3,4,6]
window = Tk() 
window.geometry("700x600")
texts = font.Font(family="Serif",size=30,underline=1,slant="italic")
def batting():
    window.title("HAND CRICKET")
    window["bg"] = "#B45F04"
    global score_type
    score_type = font.Font(family="Serif",size=27)
    global over_type
    over_type = font.Font(family="Serif",size=17)
    global opp
    opp = font.Font(size=70)
    global score,wicket,over
    score=0
    wicket=0
    over=5
    Label(window,text="let's start the game".upper(),font=texts,bg="#B45F04").pack()
    level_text=font.Font(family="Serif",size=16,slant="italic")
    enter_text=font.Font(family="Serif",size=16,slant="italic",underline=1)
    over_text=font.Font(family="Serif",size=16,slant="italic")
    score_text=font.Font(family="Serif",size=22,slant="italic")
    line_text=font.Font(family="Serif",size=40,slant="italic")
    Label(window,text="level : ",font=level_text,bg="#B45F04").place(x=10,y=75)
    Label(window,text="balls-left : ",font=over_text,bg="#B45F04").place(x=540,y=75)
    Label(window,text="SCORE : ",font=score_text,bg="#B45F04").place(x=200,y=130)
    Label(window,text="-",font=line_text,bg="#B45F04").place(x=390,y=115)
    def zero():
        global score,over,wicket
        score +=0
        over -=1
        Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
        Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
        Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
    def one():
        global sc_list
        rnd = r.randint(0,4)
        rnd = sc_list[rnd]
        global score,over,wicket
        if(rnd!=1):
            score +=1
            over -=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
        else:
            wicket +=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
    def two():
        global sc_list
        rnd = r.randint(0,4)
        rnd = sc_list[rnd]
        global score,over,wicket
        if(rnd!=2):
            score +=2
            over -=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
        else:
            wicket +=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
    def thr():
        global sc_list
        rnd = r.randint(0,4)
        rnd = sc_list[rnd]
        global score,over,wicket
        if(rnd!=3):
            score +=3
            over -=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
        else:
            wicket +=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
           
    def four():
        global sc_list
        rnd = r.randint(0,4)
        rnd = sc_list[rnd]
        global score,over,wicket
        if(rnd!=4):
            score +=4
            over -=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
        else:
            wicket +=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
           
    def six():
        global sc_list
        rnd = r.randint(0,4)
        rnd = sc_list[rnd]
        global score,over,wicket
        if(rnd!=6):
            score +=6
            over -=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
        else:
            wicket +=1
            Label(window,text=f"{score}",font=score_type,bg="#B45F04").place(x= 325,y=127)
            Label(window,text= f"{wicket}",font=score_type,bg="#B45F04").place(x=420,y=127)
            Label(window,text =f"{over}      ",font=over_type,bg="#B45F04").place(x=640,y=75)
            Label(window,text =f"{rnd}        ",font= opp,bg="#B45F04").place(x=510,y=290)
            if(over ==0):
                print(12)
            
    Label(window,text="Enter Your Choice",font=enter_text,bg="#B45F04",fg="#04B4AE").place(x=50,y=200)
    Label(window,text="Opponent  Choice",font=enter_text,bg="#B45F04",fg="#04B4AE").place(x=470,y=190)
    Button(window,text="0",width=7,command=zero).place(x=100,y=250)
    Button(window,text="1",width=7,command=one).place(x=100,y=300)
    Button(window,text="2",width=7,command=two).place(x=100,y=350)
    Button(window,text="3",width=7,command=thr).place(x=100,y=400)
    Button(window,text="4",width=7,command=four).place(x=100,y=450)
    Button(window,text="6",width=7,command=six).place(x=100,y=500)
    window.mainloop()
batting()

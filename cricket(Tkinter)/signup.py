from tkinter import *
from tkinter import font
import random as r
import email_sender
import time as t
window = Tk()
def mains():
    #main
    window.geometry("650x750")
    window.title("Signup")
    window["bg"] = "#00FFBF"
    Font = font.Font(family='Display', size=15, weight='bold',slant="italic",underline=1)
    Label(window,text="CREATE ACCOUNT",font=Font,bg="#00FFBF",fg="red").pack()
    Label(window,text=" ",bg="#00FFBF").pack()
    global f,l,p,email,user_name_c,user_pass,user_pass_re
    
    #first name
    Label(window,text="First Name : ",bg="#00FFBF").pack()
    f = Entry(window)
    f.pack()
    Label(window,text="  ",bg="#00FFBF",height=0).pack()
    
    #last name
    Label(window,text="Last Name(optional) : ",bg="#00FFBF").pack()
    l= Entry(window)
    l.pack()
    Label(window,text="  ",bg="#00FFBF",height=0).pack()

    #phone number
    Label(window,text="Phone Number: ",bg="#00FFBF").pack()
    p = Entry(window)
    p.pack()

    #mail id
    default = StringVar()
    default.set("@gmail.com")
    Label(window,bg="#00FFBF",height=0).pack()
    Label(window,text="Email Address: ",bg="#00FFBF").pack()
    email = Entry(window,textvariable=default)
    email.pack()
    Label(window,bg="#00FFBF",height=0).pack()

    #user name
    Label(window,text="User name: ",bg="#00FFBF").pack()
    user_name_c = Entry(window)
    user_name_c.pack()
    Label(window,bg="#00FFBF",height=0).pack()

    #password
    Label(window,text="Password",bg="#00FFBF").pack()
    user_pass = Entry(window)
    user_pass.pack()
    Label(window,text=" ",bg="#00FFBF").pack()

    #password_re
    Label(window,text="Re-enter Password",bg="#00FFBF").pack()
    user_pass_re = Entry(window,show="*")
    user_pass_re.pack()
    Label(window,text=" ",bg="#00FFBF").pack()

    Button(window,text="submit!",command=check_all).pack()
    window.mainloop()
def check_all():
    global all_check
    all_check=0

    #first name
    if(len(f.get())<6):
        b1 = Button(window,text="  first name  ",bg="red",width=15,height=1,fg="white")
        b1.place(x=265,y=520)
        b1.bind("<Enter>",lambda e : Label(window,text="First name must be atleast 6 characters",bg = "#00FFBF").place(x=385,y=520) )
        b1.bind("<Leave>",lambda e :  Label(window,text="                                                                    ",bg="#00FFBF").place(x=385,y=520))
    if(len(f.get())>=6):
        Button(window,text="  first name  ",bg="green",width=15,height=1,fg="white",state=DISABLED).place(x=265,y=520)
        all_check +=1
        
    #phone number
    a1 = all(f.isdigit() for f in str(p.get())) 
    c1 = len(p.get()) == 10
    d1 = a1 and c1
    if(d1):
        Button(window,text="  phone number  ",bg="green",width=15,height=1,fg="white",state=DISABLED).place(x=265,y=550)
        all_check +=1
    if(d1 == False):
        b2 = Button(window,text="  phone number ",bg="red",width=15,height=1,fg="white")
        b2.place(x=265,y=550)
        b2.bind("<Enter>",lambda e : Label(window,text="phone number must have  10 numbers ",bg = "#00FFBF").place(x=385,y=550))
        b2.bind("<Leave>",lambda e :  Label(window,text="                                                                             ",bg="#00FFBF").place(x=385,y=550))
   
   
   
    #email id
    a2 = email.get()
    a2 = a2[::-1]
    a2 = a2[:10]
    a2 = a2[::-1]
    a2 = a2.lower()
    if(a2 == "@gmail.com"):
        Button(window,text="  Email Id  ",bg="green",width=15,height=1,fg="white",state=DISABLED).place(x=265,y=580)
        all_check +=1
    if(a2!= "@gmail.com"):
        b3 =Button(window,text="  Email Id  ",bg="red",width=15,height=1,fg="white")
        b3.place(x=265,y=580)
        b3.bind("<Enter>",lambda e : Label(window,text="Email must be in abc@gmail.com format",bg = "#00FFBF").place(x=385,y=580))
        b3.bind("<Leave>",lambda e :  Label(window,text="                                                                           ",bg="#00FFBF").place(x=385,y=580))

    #username
    num = any(char.isdigit() for char in user_name_c.get())
    low = any(low.islower()  for low in user_name_c.get())
    lent = len(user_name_c.get())>=6
    nl = num and low and lent
    def enter4(e):
        num = any(char.isdigit() for char in user_name_c.get())
        low = any(low.islower()  for low in user_name_c.get())
        lent = len(user_name_c.get())>=6
        if(num == False):
            Label(window,text="Username must have atleast one number",bg="#00FFBF").place(x= 5,y=610)
        if(low == False):
            Label(window,text="Username must have atleast one lowercase",bg="#00FFBF").place(x=5,y=630)
        if (lent == False):
            Label(window,text="Username must have be atleast 6 characters",bg="#00FFBF").place(x=5,y=650)

    def leave4(e):
        Label(window,text="                                                                           ",bg="#00FFBF").place(x=5,y=610)
        Label(window,text="                                                                           ",bg="#00FFBF").place(x=5,y=630)
        Label(window,text="                                                                            ",bg="#00FFBF").place(x=5,y=650)
    if(nl):
         Button(window,text="  Username  ",bg="green",width=15,height=1,fg="white",state=DISABLED).place(x=265,y=610)
         all_check +=1
    if(nl ==False):
        b4 = Button(window,text="  Username  ",bg="red",width=15,height=1,fg="white")
        b4.place(x=265,y=610)
        b4.bind("<Enter>",enter4)
        b4.bind("<Leave>",leave4)

    
    #password
    num = any(char.isdigit() for char in user_pass.get())
    up  = any(up.isupper()  for up in user_pass.get())
    low = any(low.islower()  for low in user_pass.get())
    lent = len(user_pass.get()) >=6
    two_c = user_pass.get() == user_pass_re.get()
    n2 = num and up and low and lent and two_c
    def enter5(e):
        num = any(char.isdigit() for char in user_pass.get())
        up  = any(up.isupper()  for up in user_pass.get())
        low = any(low.islower()  for low in user_pass.get())
        lent = len(user_pass.get()) >=6
        two_c = user_pass.get() == user_pass_re.get()
        if(num == False):
            Label(window,text="Password must have atleast one number",bg="#00FFBF").place(x= 385,y=620)
        if(low == False):
            Label(window,text="Password must have atleast one lowercase",bg="#00FFBF").place(x=385,y=640)
        if (not up):
            Label(window,text="password must have be atleast one Uppercase",bg="#00FFBF").place(x=385,y=660)
        if (lent == False):
            Label(window,text="Username must have be atleast 6 characters",bg="#00FFBF").place(x=385,y=680)
        if (not two_c):
            Label(window,text="Both passwords must match",bg="#00FFBF").place(x=385,y=700)
    
    def leave5(e):
        Label(window,text="                                                                           ",bg="#00FFBF").place(x=385,y=620)
        Label(window,text="                                                                           ",bg="#00FFBF").place(x=385,y=640)
        Label(window,text="                                                                                 ",bg="#00FFBF").place(x=385,y=660)
        Label(window,text="                                                                              ",bg="#00FFBF").place(x=385,y=680)
        Label(window,text="                                                                               ",bg="#00FFBF").place(x=385,y=700)
      

    if(n2):
         Button(window,text="  password  ",bg="green",width=15,height=1,fg="white",state=DISABLED).place(x=265,y=640)
         all_check +=1
    if(n2 ==False):
         b5 = Button(window,text="  password  ",bg="red",width=15,height=1,fg="white")
         b5.place(x=265,y=640)
         b5.bind("<Enter>",enter5)
         b5.bind('<Leave>',leave5)

    if(all_check == 5):
        with open("account_info.txt","w") as acc:
            acc.write(user_name_c.get())
            acc.write("\n")
            acc.write(user_pass.get())
            try:
                e = email_sender.email()
                e.sender(email.get(),f.get()+" " + l.get())
                print("sent")
            except:
                Label(window,text="Check Internet Connection").place(x=250,y=675)

mains()




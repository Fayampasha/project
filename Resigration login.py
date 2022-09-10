from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("1000x1000")
top.resizable(0,0)
top.title("Form")
top.configure(background="lightgreen")

#Frame
f1=Frame(top,bg="lightblue",highlightbackground="black",highlightthickness=4,width=400,height=350)
f1.place(x=0,y=40)

f2=Frame(top,bg="lightblue",highlightbackground="black",highlightthickness=4,width=400,height=350)
f2.place(x=450,y=40)

#Function    
def register():
    a=aa.get()
    b=ab.get()
    c=ac.get()
    d=ad.get()
    out.set(a)
    out.set(b)
    out.set(c)
    out.set(d)
    at="Submit Your Detail Successfully"
    messagebox.showinfo("Detail",at)
  
def reset():
    en.delete(0,END)
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)

def login():
    n=ae.get()
    p=af.get()
    if(n=="Utkarsh" and p=="123"):
        ai="Login Successfully"
        messagebox.showinfo("Detail",ai)
    else:
        ai="Login Invalid"
        messagebox.showinfo("Detail",ai)
        

def reset1():
    en4.delete(0,END)
    en5.delete(0,END)    

aa=StringVar()
ab=StringVar()
ac=StringVar()
ad=IntVar()
ae=StringVar()
af=StringVar()
out=StringVar()

#Label
lb=Label(f1,text="Registration User",fg="yellow",bg="red",font=('namespace',20))
lb.place(x=100,y=10)

lb1=Label(f1,text="Enter Name")
lb1.place(x=20,y=60)

lb2=Label(f1,text="Enter E-mail")
lb2.place(x=20,y=100)

lb3=Label(f1,text="Enter Password")
lb3.place(x=20,y=150)

lb4=Label(f1,text="Enter Phone Number")
lb4.place(x=20,y=200)

lb5=Label(f2,text="Login User",fg="yellow",bg="red",font=('namespace',20))
lb5.place(x=100,y=10)

lb6=Label(f2,text="Enter Name")
lb6.place(x=20,y=60)

lb7=Label(f2,text="Enter Password")
lb7.place(x=20,y=100)

lb8=Label(textvariable=out)
lb8.place(x=20,y=450)

#Entry
en=Entry(f1,textvariable=aa)
en.place(x=150,y=60)

en1=Entry(f1,textvariable=ab)
en1.place(x=150,y=100)

en2=Entry(f1,textvariable=ac)
en2.place(x=150,y=150)

en3=Entry(f1,textvariable=ad)
en3.place(x=150,y=200)

en4=Entry(f2,textvariable=ae)
en4.place(x=150,y=60)

en5=Entry(f2,textvariable=af)
en5.place(x=150,y=100)

#Button
btn=Button(f1,text="Submit",command=register)
btn.place(x=50,y=250)

btn1=Button(f1,text="Reset",command=reset)
btn1.place(x=180,y=250)

btn2=Button(f2,text="Login",command=login)
btn2.place(x=50,y=150)

btn3=Button(f2,text="Clear",command=reset1)
btn3.place(x=180,y=150)

top.mainloop()

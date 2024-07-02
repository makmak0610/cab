
from tkinter import *

from PIL import ImageTk

def logout():
 welcome1.destroy()


def admin_page():

    welcome1.destroy()
    import admin

def login_page():
    welcome1.destroy()
    import l


def signup_page():
    welcome1.destroy()
    import singup


welcome1=Tk()
welcome1.configure(background='WHITE')
welcome1.geometry('1500x800')


welcome1.title("WELCOME PAGE ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(welcome1,image=bgImage)
bgLabel.place(x=0,y=80)

heading=Label(welcome1,text='WELCOME ',font=('Arial black',35,'bold'),fg='firebrick1')
heading.place(x=800,y=180)


login=Button(welcome1,text=' LOGIN ',font=('Arial black', 12,'bold '),fg='firebrick1',command=login_page,bd=0)
login.place(x=1050,y=0)

signup=Button(welcome1,text=' SIGNUP ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(welcome1,text=' ADMIN ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(welcome1,text=' LOGOUT ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=logout,bd=0)
logout.place(x=1270,y=0)




welcome1.mainloop()
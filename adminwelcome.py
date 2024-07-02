
from tkinter import *

from PIL import ImageTk

def logout():
 adminwelcome1.destroy()

def mysql():
    adminwelcome1.destroy()
    import mysql

def mysql1():
    adminwelcome1.destroy()
    import mysql1


def admin_page():

    adminwelcome1.destroy()
    import admin


adminwelcome1=Tk()
adminwelcome1.configure(background='WHITE')
adminwelcome1.geometry('1500x800')


adminwelcome1.title("adminwelcome PAGE ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(adminwelcome1,image=bgImage)
bgLabel.place(x=0,y=80)

heading=Label(adminwelcome1,text='Admin welcome ',font=('Arial black',35,'bold'),fg='firebrick1')
heading.place(x=800,y=180)

ml=Button(adminwelcome1,text=' SEE ALL USERS  ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql,bd=0)
ml.place(x=850,y=350)

ml1=Button(adminwelcome1,text=' SEE ALL USERS CONVERTING VALUES ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql1,bd=0)
ml1.place(x=850,y=450)

admin=Button(adminwelcome1,text=' ADMIN ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=admin_page,bd=0)
admin.place(x=1150,y=0)

logout=Button(adminwelcome1,text=' LOGOUT ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=logout,bd=0)
logout.place(x=1250,y=0)




adminwelcome1.mainloop()
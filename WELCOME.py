from tkinter import *
from PIL import ImageTk


def admin_page():

    WELCOME_window.destroy()
    import  admin

def login_page():
    WELCOME_window.destroy()
    import l

def signup_page():
    WELCOME_window.destroy()
    import singup

WELCOME_window=Tk()
WELCOME_window.configure(background='white')
WELCOME_window.geometry('1300x700')


WELCOME_window.title("WELCOME PAGE ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(WELCOME_window,image=bgImage)
bgLabel.place(x=0,y=80)


heading=Label(WELCOME_window,text='WELCOME ',font=('Arial black',35,'bold'),bg='white',fg='firebrick1')
heading.place(x=800,y=180)

login=Button(WELCOME_window,text=' LOGIN ',font=('Arial black', 12,'bold '),bg='white',fg='firebrick1',command=login_page,bd=0)
login.place(x=1050,y=0)

signup=Button(WELCOME_window,text=' SIGNUP ',font=('Arial black', 12,'bold  '),bg='white',fg='firebrick1',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(WELCOME_window,text=' ADMIN ',font=('Arial black', 12,'bold  '),bg='white',fg='firebrick1',command=admin_page,bd=0)
admin.place(x=1200,y=0)


amount_input = Entry(WELCOME_window,width=20,bg='firebrick1',font=('Arial black', 11,'bold  '))
amount_input.place(x=690,y=320)


def AMOUNT ():
    Label.config(text=clicked.get())


# Dropdown menu options
options = ["INR RUPEES", "US DOLLOR", "ashok vihar", "pitampura", "jankpuri", "kanhaiya nagar", "goa"]
# datatype of menu text
clicked = StringVar()
clicked.set("INR RUPEES")
# Create Dropdown menu
drop = OptionMenu(WELCOME_window, clicked, *options)
drop.place(x=900, y=320)

amount_input = Entry(WELCOME_window,width=20,bg='firebrick1',font=('Arial black', 11,'bold  '))
amount_input.place(x=690,y=420)






















WELCOME_window.mainloop()
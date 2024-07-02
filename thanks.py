from tkinter import *
from PIL import ImageTk
import webbrowser


def welcome():
    thank.destroy()
    import welcome1

def logout():
   thank.destroy()


thank=Tk()
thank.configure(background='white')
thank.geometry('1300x700')


thank.title("Thank You ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(thank,image=bgImage)
bgLabel.place(x=0,y=80)
heading=Label(thank,text=' Thanks ',font=('Arial black',35,'bold'),bg='white',fg='firebrick1')
heading.place(x=900,y=180)
heading=Label(thank,text=' For Converting  ',font=('Arial black',35,'bold'),bg='white',fg='firebrick1')
heading.place(x=800,y=250)


welcome=Button(thank,text='WELCOME',font=('Arial black', 12,'bold '),bg='white',fg='firebrick1',command=welcome,bd=0)
welcome.place(x=1150,y=0)

logout=Button(thank,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='white',fg='firebrick1',command=logout,bd=0)
logout.place(x=1250,y=0)
thank.mainloop()
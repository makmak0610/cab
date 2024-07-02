
from tkinter import *

from PIL import ImageTk

def logout():
 view1.destroy()



def wel_page():
    view1.destroy()
    import welcome1


view1=Tk()
view1.configure(background='WHITE')
view1.geometry('1500x800')


view1.title("view PAGE ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(view1,image=bgImage)
bgLabel.place(x=0,y=80)

heading=Label(view1,text='view ',font=('Arial black',35,'bold'),fg='firebrick1',background='white')
heading.place(x=800,y=10)

admin=Button(view1,text=' WELCOME ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=wel_page,bd=0)
admin.place(x=1150,y=0)


logout=Button(view1,text=' LOGOUT ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=logout,bd=0)
logout.place(x=1270,y=0)




view1.mainloop()
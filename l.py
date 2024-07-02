from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql



def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
      messagebox.showerror('error','all field required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()
        except:
            messagebox.showerror('error','not establish connection')
            return


        query = 'use converter'
        mycursor.execute(query)

        query='select * from data1 where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error','invalid ')
        else:
            login_window.destroy()
            import converter



def singup_page():
    login_window.destroy()
    import singup

def admin_page():
    login_window.destroy()
    import admin


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



def on_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)

def on_enter1(event):
    if passwordEntry.get()=='password':
        passwordEntry.delete(0,END)

login_window=Tk()
login_window.configure(background='white')
login_window.geometry('1300x700')

login_window.title("LOGIN PAGE ")
bgImage=ImageTk.PhotoImage(file='img1 .jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=300,y=200)




heading=Label(login_window,text='USER LOGIN ',width=13,font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=695,y=200)

usernameEntry=Entry(login_window,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=695,y=300)
usernameEntry.insert(0,'username')
usernameEntry.bind('<FocusIn>',on_enter)
Frame(login_window,width=255,height=3,bg='firebrick1').place(x=695,y=322)

passwordEntry=Entry(login_window,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=695,y=360)
passwordEntry.insert(0,'password')
passwordEntry.bind('<FocusIn>',on_enter1)
Frame(login_window,width=255,height=3,bg='firebrick1').place(x=695,y=382)
openeye=PhotoImage(file='openeye.png')

eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=920,y=355)



loginButton=Button(login_window,text='login',font=('Open Sans', 16,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=login_user)
loginButton.place(x=695,y=480)

signupLabel=Label(login_window,text='dont have an account ?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=695,y=560)


newaccountButton=Button(login_window,text=' create new account ',font=('Open Sans', 9,'bold underline '),fg='blue',bg='white',activeforeground='blue',bd=0,command=singup_page)
newaccountButton.place(x=835,y=560)


adminButton=Button(text='admin login ',font=('Microsoft Yahei UI Light',9,'bold','underline'),fg='blue',bg='white',bd=0,cursor='hand2',activeforeground='white',activebackground='blue',command=admin_page )
adminButton.place(x=835,y=580)

login_window.mainloop()
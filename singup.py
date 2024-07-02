from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import re
def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('error','all fields required')

    elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',emailEntry.get() ) is None:
        messagebox.showinfo('error', 'invalid mail')

    elif usernameEntry.get() < '8':
        messagebox.showinfo('error', 'username must be character and less then 8 character')

    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showinfo('error', 'password mismatched ')

    elif passwordEntry.get() < '8':
        messagebox.showinfo('error', 'password length must be less then 8')


    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showinfo('error','password mismatched ')
    elif check.get() == 0:
        messagebox.showinfo('error','please accept t&c')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='saloni')
            mycursor = con.cursor()

        except:
                messagebox.showinfo('error','database connectivity issue ')
                return
        try:
            query='create database converter'
            mycursor.execute(query)
            query='use converter'
            mycursor.execute(query)
            query='create table data1(id int auto_increment primary key not null, email varchar(50) , username varchar(55), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use converter')


        query='select * from data1 where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showinfo('erroe', 'username already exist')
        else:
            query='insert into data1(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','registeration successful')
            clear()
            signup_window.destroy()
            import l




def login_page():
    signup_window.destroy()
    import l





def admin_page():
    signup_window.destroy()
    import admin




signup_window=Tk()
signup_window.configure(background='white')
signup_window.geometry('1300x700')

signup_window.title("SINGUP PAGE ")
bgImage=ImageTk.PhotoImage(file='img1 .jpg')
bgLabel=Label(signup_window,image=bgImage)
bgLabel.place(x=250,y=200)


frame=Frame(signup_window,bg='white')
frame.place(x=700,y=150)

heading=Label(frame,text='Create Account',width=15,font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)


emailLbabel=Label(frame,text='email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLbabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame, width=30,text='email', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLbabel=Label(frame,text='username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLbabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,text='username',font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLbabel=Label(frame,text='password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLbabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,text='password',font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmLbabel=Label(frame,text='Confirm_Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmLbabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,text='Confirm_Password',font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
tandc=Checkbutton(frame,text='I agree the terms and conditions ',font=('Microsoft Yahei UI Light',9,'bold'),bg='white',fg='firebrick1',activeforeground='firebrick1',activebackground='white',cursor='hand2',variable=check)
tandc.grid(row=9,column=0,sticky='w',padx=15,pady=10)

signupButton=Button(frame,text='signup ',font=('Microsoft Yahei UI Light',12,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alredyaccount=Label(frame,text="Don't have an account" ,font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white')
alredyaccount.grid(row=11,column=0,sticky='w',padx=15,pady=10)

loginButton=Button(frame,text='log in ',font=('Microsoft Yahei UI Light',9,'bold','underline'),fg='blue',bg='white',bd=0,cursor='hand2',activeforeground='white',activebackground='blue',command=login_page)
loginButton.place(x=170,y=410)

adminButton=Button(frame,text='admin login ',font=('Microsoft Yahei UI Light',9,'bold','underline'),fg='blue',bg='white',bd=0,cursor='hand2',activeforeground='white',activebackground='blue',command=admin_page)
adminButton.place(x=215,y=410)



signup_window.mainloop()


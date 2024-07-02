from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()

    if email =='laksh@gmail.com' and password == '1234':
        admin_window.destroy()
        import converter
    else:
        messagebox.showinfo('error login fail')


def back():
    admin_window.destroy()
    import welcome1


admin_window=Tk()
admin_window.configure(background='white')
admin_window.geometry('1300x700')

admin_window.title("LOGIN PAGE ")
bgImage=ImageTk.PhotoImage(file='img1 .jpg')
bgLabel=Label(admin_window,image=bgImage)
bgLabel.place(x=300,y=200)

heading=Label(admin_window,text='ADMIN LOGIN ',width=13,font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=695,y=200)


email_label =Label(admin_window,text='Enter Email',fg='firebrick1',bg='white' )
email_label.place(x=650,y=300)
email_label.config(font=('verdana',12))

email_input = Entry(admin_window,width=20,bg='firebrick1')
email_input.place(x=750,y=300)
email_input.config(font=('verdana',12))


password_label = Label(admin_window,text='Enter Password',fg='firebrick1',bg='white' )
password_label.place(x=620,y=400)
password_label.config(font=('verdana',12))

password_input = Entry(admin_window,width=20,bg='firebrick1')
password_input.place(x=750,y=400)
password_input.config(font=('verdana',12))

login_btn = Button(admin_window,text= 'Login ',fg ='firebrick1',bg='white' ,command=handle_login)
login_btn.place(x=750,y=450)
login_btn.config(font=('verdana',12))

back=Button(admin_window,text=' BACK ',font=('Arial black', 12,'bold  '),bg='white',fg='firebrick1',command=back,bd=0)
back.place(x=1250,y=0)


admin_window.mainloop()

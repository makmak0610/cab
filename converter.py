import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from forex_python.converter import CurrencyRates
import pymysql
def logout():
 con_window.destroy()


def admin_page():

    con_window.destroy()
    import admin

def login_page():
    con_window.destroy()
    import l



def clear():
      username.delete(0, END)


def signup_page():
    con_window.destroy()
    import singup

def connect():

    if username.get() == '':
        messagebox.showerror('error','all fields required')

    elif username.get() < '8':
        messagebox.showinfo('error', 'username must be character and less then 8 character')

    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='saloni')
            mycursor = con.cursor()

        except:
                messagebox.showinfo('error','database connectivity issue ')
                return

        query = 'use converter'
        mycursor.execute(query)
        query = 'select * from data1 where username=%s '
        mycursor.execute(query, (username.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error', 'invalid username')
        else:
            query='insert into data2(username,from_cur , to_cur , amount ,conv_amt ) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(username.get(),variable1.get(),variable2.get(),amount.get(),txt.get()))
            messagebox.showinfo('done', ' submit ')
            con.commit()
            con.close()
            con_window.destroy()
            import thanks












con_window=customtkinter.CTk()
con_window.configure(background='WHITE')
con_window.geometry('1500x800')


con_window.title("WELCOME PAGE ")
bgImage=ImageTk.PhotoImage(file='con.jpg')
bgLabel=Label(con_window,image=bgImage)
bgLabel.place(x=0,y=80)

heading=Label(con_window,text='WELCOME ',font=('Arial black',35,'bold'),fg='firebrick1')
heading.place(x=800,y=180)
username=Label(con_window,text='username',font=('Arial black',20,'bold'),fg='firebrick1')
username.place(x=650,y=250)
username=Entry(con_window,width=30,text='username',font=('Arial black',15,'bold'),fg='white',bg='firebrick1')
username.place(x=650,y=300)

login=Button(con_window,text=' LOGIN ',font=('Arial black', 12,'bold '),fg='firebrick1',command=login_page,bd=0)
login.place(x=1050,y=0)

signup=Button(con_window,text=' SIGNUP ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(con_window,text=' ADMIN ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(con_window,text=' LOGOUT ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=logout,bd=0)
logout.place(x=1270,y=0)


from_label=customtkinter.CTkLabel(con_window,text="FROM",font=('arial',25,'bold'),text_color='firebrick1')
from_label.place(x=650, y=420)

to_label=customtkinter.CTkLabel(con_window,text="TO",font=('arial',25,'bold'),text_color='firebrick1')
to_label.place(x=1100, y=420)

result_label=customtkinter.CTkLabel(con_window,text="Result After converting ",font=('arial',25,'bold'),text_color='firebrick1')
result_label.place(x=800, y=608)


currency_list=["INR","USD","CAD","EUR","GBP"]
variable1=StringVar()
variable2=StringVar()
txt=StringVar()

def convert():
    from_currency=variable1.get()
    to_currency=variable2.get()
    c = CurrencyRates()
    amt = c.convert(from_currency,to_currency,float(amount.get()))
    amount1 = float("{:.3f}".format(amt))
    txt.set(amount1)
    result=customtkinter.CTkLabel(con_window,textvariable=txt,font=('arial',15,'bold'),fg_color='firebrick1',text_color='black',width=50)
    result.place(x=1105, y=608)


def reset():
    amount.delete(0,END)




from_menu=customtkinter.CTkComboBox(con_window,variable=variable1,values=currency_list,font=('arial',15,'bold'),dropdown_font=('arial',15,'bold'),fg_color='firebrick1',text_color='black',button_color='firebrick1',button_hover_color='firebrick1',border_color='BLACK',dropdown_text_color='BLACK',dropdown_hover_color='PINK',dropdown_fg_color='white')
from_menu.place(x=750, y=420)
to_menu=customtkinter.CTkComboBox(con_window,variable=variable2,values=currency_list,font=('arial',15,'bold'),dropdown_font=('arial',15,'bold'),fg_color='firebrick1',text_color='black',button_color='firebrick1',button_hover_color='firebrick1',border_color='BLACK',dropdown_text_color='BLACK',dropdown_hover_color='PINK',dropdown_fg_color='white')
to_menu.place(x=1150, y=420)

amount=customtkinter.CTkEntry(con_window,font=('arial',15,'bold'),fg_color='firebrick1',text_color='BLACK')
amount.place(x=905, y=480)

convert=customtkinter.CTkButton(con_window,command=convert,text='convert',font=('arial',15,'bold'),fg_color='firebrick1',text_color='white')
convert.place(x=905, y=518)

submit=customtkinter.CTkButton(con_window,command=connect,text='submit',font=('arial',15,'bold'),fg_color='firebrick1',text_color='white')
submit.place(x=905, y=558)

reset=customtkinter.CTkButton(con_window,command=reset,text='reset',font=('arial',15,'bold'),fg_color='firebrick1',text_color='white')
reset.place(x=1105, y=518)

con_window.mainloop()
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("300x300")

name = tk.Label(text = "Name:", background = "white", fg="black")
name.place(x=100,y=20)  

email = tk.Label(text = "Email:", background = "white", fg="black")
email.place(x=100,y=50)

password = tk.Label(text = "Password:",background = "white", fg="black")
password.place(x=100,y=80)

box4 = 0
box5 = 0

def enter():
     e = box2.get()
     ee = box4.get()
     p = box3.get()
     pp = box5.get()
     if e == ee and p == pp:
       messagebox.showinfo("box","Login Successful")
     else: 
         messagebox.showerror("box","Incorrect Email or Password")
           
    

def display(): 
    global box4
    global box5
    window2 = tk.Tk()
    window2.geometry("250x250")
    login = tk.Label(window2, text = "Login", background = "white", fg = "black")
    login.place(x=100,y=10)
    email2 = tk.Label(window2, text= "Email:", bg = "white", fg = "black")
    email2.place(x=70,y=50)
    password2 = tk.Label(window2, text= "Password:", bg = "white", fg = "black")
    password2.place(x=70,y=80)
    box4 = tk.Entry(window2,width=10)
    box4.place(x=120,y=47)
    box5 = tk.Entry(window2,width=10)
    box5.place(x=140,y=77)
    login2 = tk.Button(window2, text = "Login", background = "white", fg = "black", command=enter)
    login2.place(x=100,y=120)




register = tk.Button(window, text= "Register", background = "white", fg="black", command=display)
register.place(x=130,y=110)

box = tk.Entry(window,width=10)
box.place(x=155,y=17)

box2 = tk.Entry(window,width=10)
box2.place(x=155,y=45)

box3 = tk.Entry(window,width=10)
box3.place(x=170,y=80)









window.mainloop()
import tkinter as tk
from tkinter import messagebox,ttk
from PIL import ImageTk


def toggle_password_visibility():
    global is_password_visible

    is_password_visible = not is_password_visible

    if is_password_visible:
        passwordEntry.config(show=' ')
    else:
        passwordEntry.config(show='*')

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fiels cannot be empty')
    elif usernameEntry.get()=='Neha' and (is_password_visible or passwordEntry.get()=='1234'):
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror(('Error'),'Please enter correct credentials')


window=tk.Tk()

window.geometry('1700x1700+0+0')
window.title('Login Page')

bgImage=ImageTk.PhotoImage(file='bg.png')

bgLabel=tk.Label(window,image=bgImage)
bgLabel.place(x=0,y=0)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

s='Linkedin Management System'
sliderLabel=tk.Label(window,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=410,y=0)
slider()

loginFrame=tk.Frame(window,bg='white')
loginFrame.place(x=460,y=190)

logoImage=tk.PhotoImage(file='linkedin.png')

logoLabel=tk.Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=1,columnspan=4,pady=20)
usernameImage=tk.PhotoImage(file='user.png')
usernameLabel=tk.Label(loginFrame,image=usernameImage,text='Username',compound=tk.LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=tk.Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=tk.PhotoImage(file='password.png')
passwordLabel=tk.Label(loginFrame,image=passwordImage,text='Password',compound=tk.LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

# Add the "see or not see" button
see_password_button = ttk.Button(loginFrame, text='See Password', command=toggle_password_visibility)
see_password_button.grid(row=2, column=1, sticky='ew')

is_password_visible = False



passwordEntry=tk.Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue', show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=tk.Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()

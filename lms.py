from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def exit_button():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    print(url)
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
        
    table=pandas.DataFrame(newlist,columns=['Id','CId','Name','Email','Connections', 'Post_Content', 'Likes', 'Institute_Name', 'Passing_year', 'Skills','Job_Role','Company_Name','Industry','Salary'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is exported successfully.')



def update_user():
    def update_data():
        query='update ldms set cid=%s,name=%s, email=%s, connections=%s, post_content=%s, likes = %s, institute_name=%s, passing_year=%s, skills=%s, job_role=%s, company_name=%s, industry=%s, salary=%s where id=%s'
        mycursor.execute(query,(cidEntry.get(),nameEntry.get(),emailEntry.get(),connectionsEntry.get(),post_contentEntry.get(),likesEntry.get(),institute_nameEntry.get(),passing_yearEntry.get(),skillsEntry.get(),job_roleEntry.get(),company_nameEntry.get(),industryEntry.get(),salaryEntry.get(),idEntry.get()))
        lms1.commit()
        messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully.',parent=update_window)
        update_window.destroy()
        show_users()



    update_window = Toplevel()
    update_window.title('Update User')
    update_window.grab_set()
    update_window.resizable(False, False)
    idLabel = Label(update_window, text='Id', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    cidLabel = Label(update_window, text='CId', font=('times new roman', 15, 'bold'))
    cidLabel.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    cidEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    cidEntry.grid(row=1, column=1, padx=10, pady=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=2, column=1, padx=10, pady=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 15, 'bold'))
    emailLabel.grid(row=4, column=0, padx=20, pady=10, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=4, column=1, padx=10, pady=10)

    connectionsLabel = Label(update_window, text='Connections', font=('times new roman', 15, 'bold'))
    connectionsLabel.grid(row=5, column=0, padx=20, pady=10, sticky=W)
    connectionsEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    connectionsEntry.grid(row=5, column=1, padx=10, pady=10)

    post_contentLabel = Label(update_window, text='Post_Content', font=('times new roman', 15, 'bold'))
    post_contentLabel.grid(row=6, column=0, padx=20, pady=10, sticky=W)
    post_contentEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    post_contentEntry.grid(row=6, column=1, padx=10, pady=10)

    likesLabel = Label(update_window, text='Likes', font=('times new roman', 15, 'bold'))
    likesLabel.grid(row=7, column=0, padx=20, pady=10, sticky=W)
    likesEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    likesEntry.grid(row=7, column=1, padx=10, pady=10)

    institute_nameLabel = Label(update_window, text='Institute_Name', font=('times new roman', 15, 'bold'))
    institute_nameLabel.grid(row=8, column=0, padx=20, pady=10, sticky=W)
    institute_nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    institute_nameEntry.grid(row=8, column=1, padx=10, pady=10)

    passing_yearLabel = Label(update_window, text='Passing_Year', font=('times new roman', 15, 'bold'))
    passing_yearLabel.grid(row=9, column=0, padx=20, pady=10, sticky=W)
    passing_yearEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    passing_yearEntry.grid(row=9, column=1, padx=10, pady=10)

    skillsLabel = Label(update_window, text='Skills', font=('times new roman', 15, 'bold'))
    skillsLabel.grid(row=10, column=0, padx=20, pady=10, sticky=W)
    skillsEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    skillsEntry.grid(row=10, column=1, padx=10, pady=10)

    job_roleLabel = Label(update_window, text='Job_Role', font=('times new roman', 15, 'bold'))
    job_roleLabel.grid(row=11, column=0, padx=20, pady=10, sticky=W)
    job_roleEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    job_roleEntry.grid(row=11, column=1, padx=10, pady=10)

    company_nameLabel = Label(update_window, text='Company_Name', font=('times new roman', 15, 'bold'))
    company_nameLabel.grid(row=12, column=0, padx=20, pady=10, sticky=W)
    company_nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    company_nameEntry.grid(row=12, column=1, padx=10, pady=10)

    industryLabel = Label(update_window, text='Industry', font=('times new roman', 15, 'bold'))
    industryLabel.grid(row=13, column=0, padx=20, pady=10, sticky=W)
    industryEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    industryEntry.grid(row=13, column=1, padx=10, pady=10)

    salaryLabel = Label(update_window, text='Salary', font=('times new roman', 15, 'bold'))
    salaryLabel.grid(row=14, column=0, padx=20, pady=10, sticky=W)
    salaryEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    salaryEntry.grid(row=14, column=1, padx=10, pady=10)

    update_user_button = ttk.Button(update_window, text='UPDATE USER', command=update_data)
    update_user_button.grid(row=15, columnspan=2, pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    cidEntry.insert(0,listdata[1])
    nameEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    connectionsEntry.insert(0,listdata[4])
    post_contentEntry.insert(0,listdata[5])
    likesEntry.insert(0,listdata[6])
    institute_nameEntry.insert(0,listdata[7])
    passing_yearEntry.insert(0,listdata[8])
    skillsEntry.insert(0,listdata[9])
    job_roleEntry.insert(0,listdata[10])
    company_nameEntry.insert(0,listdata[11])
    industryEntry.insert(0,listdata[12])
    salaryEntry.insert(0,listdata[13])

def show_users():
    query = 'select * from ldms'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_user():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from ldms where id=%s'
    mycursor.execute(query,content_id)
    lms1.commit()
    messagebox.showinfo('Deleted',f'User with Id {content_id} is deleted successfully')
    query = 'select * from ldms'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def search_user():
    def search_data():
        query='select * from ldms where id=%s or cid=%s or name=%s or email=%s or connections=%s or post_content=%s or likes = %s or institute_name=%s or passing_year=%s or skills=%s or job_role=%s or company_name=%s or industry=%s or salary=%s'
        mycursor.execute(query,(idEntry.get(),cidEntry.get(),nameEntry.get(),emailEntry.get(),connectionsEntry.get(),post_contentEntry.get(),likesEntry.get(),institute_nameEntry.get(),passing_yearEntry.get(),skillsEntry.get(),job_roleEntry.get(),company_nameEntry.get(),industryEntry.get(),salaryEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)
    search_window = Toplevel()
    search_window.title('Search User')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Id', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    cidLabel = Label(search_window, text='CId', font=('times new roman', 15, 'bold'))
    cidLabel.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    cidEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    cidEntry.grid(row=1, column=1, padx=10, pady=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=2, column=1, padx=10, pady=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 15, 'bold'))
    emailLabel.grid(row=4, column=0, padx=20, pady=10, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=4, column=1, padx=10, pady=10)

    connectionsLabel = Label(search_window, text='Connections', font=('times new roman', 15, 'bold'))
    connectionsLabel.grid(row=5, column=0, padx=20, pady=10, sticky=W)
    connectionsEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    connectionsEntry.grid(row=5, column=1, padx=10, pady=10)

    post_contentLabel = Label(search_window, text='Post_Content', font=('times new roman', 15, 'bold'))
    post_contentLabel.grid(row=6, column=0, padx=20, pady=10, sticky=W)
    post_contentEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    post_contentEntry.grid(row=6, column=1, padx=10, pady=10)

    likesLabel = Label(search_window, text='Likes', font=('times new roman', 15, 'bold'))
    likesLabel.grid(row=7, column=0, padx=20, pady=10, sticky=W)
    likesEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    likesEntry.grid(row=7, column=1, padx=10, pady=10)

    institute_nameLabel = Label(search_window, text='Institute_Name', font=('times new roman', 15, 'bold'))
    institute_nameLabel.grid(row=8, column=0, padx=20, pady=10, sticky=W)
    institute_nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    institute_nameEntry.grid(row=8, column=1, padx=10, pady=10)

    passing_yearLabel = Label(search_window, text='Passing_Year', font=('times new roman', 15, 'bold'))
    passing_yearLabel.grid(row=9, column=0, padx=20, pady=10, sticky=W)
    passing_yearEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    passing_yearEntry.grid(row=9, column=1, padx=10, pady=10)

    skillsLabel = Label(search_window, text='Skills', font=('times new roman', 15, 'bold'))
    skillsLabel.grid(row=10, column=0, padx=20, pady=10, sticky=W)
    skillsEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    skillsEntry.grid(row=10, column=1, padx=10, pady=10)

    job_roleLabel = Label(search_window, text='Job_Role', font=('times new roman', 15, 'bold'))
    job_roleLabel.grid(row=11, column=0, padx=20, pady=10, sticky=W)
    job_roleEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    job_roleEntry.grid(row=11, column=1, padx=10, pady=10)

    company_nameLabel = Label(search_window, text='Company_Name', font=('times new roman', 15, 'bold'))
    company_nameLabel.grid(row=12, column=0, padx=20, pady=10, sticky=W)
    company_nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    company_nameEntry.grid(row=12, column=1, padx=10, pady=10)

    industryLabel = Label(search_window, text='Industry', font=('times new roman', 15, 'bold'))
    industryLabel.grid(row=13, column=0, padx=20, pady=10, sticky=W)
    industryEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    industryEntry.grid(row=13, column=1, padx=10, pady=10)

    salaryLabel = Label(search_window, text='Salary', font=('times new roman', 15, 'bold'))
    salaryLabel.grid(row=14, column=0, padx=20, pady=10, sticky=W)
    salaryEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    salaryEntry.grid(row=14, column=1, padx=10, pady=10)

    search_user_button = ttk.Button(search_window, text='SEARCH USER', command=search_data)
    search_user_button.grid(row=15, columnspan=2, pady=15)


def add_newuser():
    def add_data():
        if idEntry.get() == '' or cidEntry.get() == '' or nameEntry.get() == '' or emailEntry.get() == '' or connectionsEntry.get() == '' or post_contentEntry.grid == '' or likesEntry.grid == '' or institute_nameEntry.get() == '' or passing_yearEntry.get() == '' or skillsEntry.get() == '' or job_roleEntry.get() == '' or company_nameEntry.get() == '' or industryEntry.get() == '' or salaryEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required', parent=add_window)
        else:
            try:
                query='insert into ldms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),cidEntry.get(),nameEntry.get(),emailEntry.get(),connectionsEntry.get(),post_contentEntry.get(),likesEntry.get(),institute_nameEntry.get(),passing_yearEntry.get(),skillsEntry.get(),job_roleEntry.get(),company_nameEntry.get(),industryEntry.get(),salaryEntry.get()))
                lms1.commit()
                result=messagebox.askyesno('Confirm','Data added Successfully. Do you want to clean the form?',parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    cidEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    connectionsEntry.delete(0, END)
                    post_contentEntry.delete(0, END)
                    likesEntry.delete(0, END)
                    institute_nameEntry.delete(0, END)
                    passing_yearEntry.delete(0, END)
                    skillsEntry.delete(0, END)
                    job_roleEntry.delete(0, END)
                    company_nameEntry.delete(0, END)
                    industryEntry.delete(0, END)
                    salaryEntry.delete(0, END)
                else:
                    pass

            except:
                messagebox.showerror('Error','Id cannot be repeated or data entered is too long.',parent=add_window)
                return

            query='select * from ldms'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)


    add_window=Toplevel()
    add_window.title('Add New User')
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='Id',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=20,pady=10,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=10,pady=10)

    cidLabel=Label(add_window,text='CId',font=('times new roman',15,'bold'))
    cidLabel.grid(row=1,column=0,padx=20,pady=10,sticky=W)
    cidEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    cidEntry.grid(row=1,column=1,padx=10,pady=10)

    nameLabel=Label(add_window,text='Name',font=('times new roman',15,'bold'))
    nameLabel.grid(row=2,column=0,padx=20,pady=10,sticky=W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=2,column=1,padx=10,pady=10)

    emailLabel=Label(add_window,text='Email',font=('times new roman',15,'bold'))
    emailLabel.grid(row=4,column=0,padx=20,pady=10,sticky=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=4,column=1,padx=10,pady=10)

    connectionsLabel=Label(add_window,text='Connections',font=('times new roman',15,'bold'))
    connectionsLabel.grid(row=5,column=0,padx=20,pady=10,sticky=W)
    connectionsEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    connectionsEntry.grid(row=5,column=1,padx=10,pady=10)

    post_contentLabel=Label(add_window,text='Post_Content',font=('times new roman',15,'bold'))
    post_contentLabel.grid(row=6,column=0,padx=20,pady=10,sticky=W)
    post_contentEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    post_contentEntry.grid(row=6,column=1,padx=10,pady=10)

    likesLabel=Label(add_window,text='Likes',font=('times new roman',15,'bold'))
    likesLabel.grid(row=7,column=0,padx=20,pady=10,sticky=W)
    likesEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    likesEntry.grid(row=7,column=1,padx=10,pady=10)

    institute_nameLabel=Label(add_window,text='Institute_Name',font=('times new roman',15,'bold'))
    institute_nameLabel.grid(row=8,column=0,padx=20,pady=10,sticky=W)
    institute_nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    institute_nameEntry.grid(row=8,column=1,padx=10,pady=10)

    passing_yearLabel=Label(add_window,text='Passing_Year',font=('times new roman',15,'bold'))
    passing_yearLabel.grid(row=9,column=0,padx=20,pady=10,sticky=W)
    passing_yearEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    passing_yearEntry.grid(row=9,column=1,padx=10,pady=10)

    skillsLabel=Label(add_window,text='Skills',font=('times new roman',15,'bold'))
    skillsLabel.grid(row=10,column=0,padx=20,pady=10,sticky=W)
    skillsEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    skillsEntry.grid(row=10,column=1,padx=10,pady=10)

    job_roleLabel=Label(add_window,text='Job_Role',font=('times new roman',15,'bold'))
    job_roleLabel.grid(row=11,column=0,padx=20,pady=10,sticky=W)
    job_roleEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    job_roleEntry.grid(row=11,column=1,padx=10,pady=10)

    company_nameLabel=Label(add_window,text='Company_Name',font=('times new roman',15,'bold'))
    company_nameLabel.grid(row=12,column=0,padx=20,pady=10,sticky=W)
    company_nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    company_nameEntry.grid(row=12,column=1,padx=10,pady=10)

    industryLabel=Label(add_window,text='Industry',font=('times new roman',15,'bold'))
    industryLabel.grid(row=13,column=0,padx=20,pady=10,sticky=W)
    industryEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    industryEntry.grid(row=13,column=1,padx=10,pady=10)

    salaryLabel=Label(add_window,text='Salary',font=('times new roman',15,'bold'))
    salaryLabel.grid(row=14,column=0,padx=20,pady=10,sticky=W)
    salaryEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    salaryEntry.grid(row=14,column=1,padx=10,pady=10)

    add_user_button=ttk.Button(add_window,text='ADD NEW USER',command=add_data)
    add_user_button.grid(row=15, columnspan=2,pady=15)


def connect_database():
    def connect():
        global mycursor, lms1
        try:
            lms1=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password='mySQL@2112')
            mycursor=lms1.cursor()

        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
            return
        try:
            query='create database linkedinms'
            mycursor.execute(query)
            query='use linkedinms'
            mycursor.execute(query)
            query='create table ldms(id int not null primary key, cid varchar(3) not null, name varchar(20) not null, email varchar(25) not null, connections int,  post_content varchar(45), likes int, institute_name varchar(20), passing_year int not null,skills varchar(30) not null, job_role varchar(25),company_name varchar(20),industry varchar(20) not null, salary int not null)'
            mycursor.execute(query)
        except:
            query='use linkedinms'
            mycursor.execute(query)
            
        messagebox.showinfo('Success', 'DataBase Connected', parent=connectWindow)
        connectWindow.destroy()
        addnewuserButton.config(state=NORMAL)
        searchuserButton.config(state=NORMAL)
        updateuserButton.config(state=NORMAL)
        showusersButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)
        deleteuserButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('480x250+730+200')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name: ',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('arial', 15, 'bold'),bd=1)
    hostEntry.grid(row=0, column=1, padx=8,pady=20)

    usernameLabel = Label(connectWindow, text='User Name:', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('arial', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=8, pady=20)

    passwordLabel = Label(connectWindow, text='Password:', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('arial', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=8, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT', command=connect)
    connectButton.grid(row=3,columnspan=2)

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

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    print(date,currenttime)
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('itft1')

root.geometry('1700x1700+0+0')

root.title('Linkedin Management System')

datetimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Linkedin Management System'
sliderLabel=Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=350,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=1350,y=20)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='download.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0,padx=20)

addnewuserButton=ttk.Button(leftFrame,text='Add New User',width=30,state=DISABLED,command=add_newuser)
addnewuserButton.grid(row=1,column=0,pady=20)

searchuserButton=ttk.Button(leftFrame,text='Search User',width=30,state=DISABLED,command=search_user)
searchuserButton.grid(row=2,column=0,pady=20)

deleteuserButton=ttk.Button(leftFrame,text='Delete User',width=30,state=DISABLED,command=delete_user)
deleteuserButton.grid(row=3,column=0,pady=20)

updateuserButton=ttk.Button(leftFrame,text='Update User',width=30,state=DISABLED,command=update_user)
updateuserButton.grid(row=4,column=0,pady=20)

showusersButton=ttk.Button(leftFrame,text='Show User',width=30,state=DISABLED,command=show_users)
showusersButton.grid(row=5,column=0,pady=20)

exportdataButton=ttk.Button(leftFrame,text='Export data',width=30,state=DISABLED,command=export_data)
exportdataButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit User',width=30,state=DISABLED,command=exit_button)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=1150,height=700)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
studentTable=ttk.Treeview(rightFrame,columns=('Id','CId','Name','Email','Connections', 'Post_Content', 'Likes', 'Institute_Name', 'Passing_year', 'Skills','Job_Role','Company_Name','Industry','Salary'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)


scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('CId',text='CId')
studentTable.heading('Name',text='Name')
studentTable.heading('Email',text='Email')
studentTable.heading('Connections',text='Connections')
studentTable.heading('Post_Content',text='Post_Content')
studentTable.heading('Likes',text='Likes')
studentTable.heading('Institute_Name',text='Institute_Name')
studentTable.heading('Passing_year',text='Passing_year')
studentTable.heading('Skills',text='Skills')
studentTable.heading('Job_Role',text='Job_Role')
studentTable.heading('Company_Name',text='Company_Name')
studentTable.heading('Industry',text='Industry')
studentTable.heading('Salary',text='Salary')

studentTable.column('Id',width=70,anchor=CENTER)
studentTable.column('CId',width=70,anchor=CENTER)
studentTable.column('Name',width=160)
studentTable.column('Email',width=250)
studentTable.column('Connections',width=120,anchor=CENTER)
studentTable.column('Passing_year',width=150,anchor=CENTER)
studentTable.column('Salary',width=80,anchor=CENTER)
studentTable.column('Likes',width=80,anchor=CENTER)
studentTable.column('Post_Content',width=360)
studentTable.column('Skills',width=200)
style=ttk.Style()
style.configure('Treeview',rowheight=20,font=('Times new roman',12,'bold'),foreground='black',background='sky blue',fieldbackground='sky blue')
style.configure('Treeview.Heading',font=('Times new roman',18,'bold'),background='sky blue')


studentTable.config(show='headings')




root.mainloop()

from tkinter import *


root = Tk()
root.geometry('400x200')
root.title('Welcome to our Login System')
root.config(bg='lightblue')



def login():
    u = username.get()
    p = password.get()
    
    file = open('login.txt','r')
    for line in file:
        #移除 line 字串開頭和結尾的所有換行符號（\n），將字串切開並轉換成一個字串清單
        data = line.strip("\n").split(', ')
        if data[0] == u:
            if data[1] == p:
                print('Login Successful')
                exit()
            else:
                print('Login Unsuccessful')
                exit()
    print("Don't have this user.")
          


Login_txt = Label(root, text='Username:', bg='lightblue',font=('Times New Roman',12))
Login_txt.pack()
username = Entry(root)
username.pack()



Password_txt = Label(root, text='Password:', bg='lightblue',font=('Times New Roman',12))
Password_txt.pack()
password = Entry(root)
password.pack()


login_btn = Button(root, text='Login', command=login, bg='lightgrey',font=('Times New Roman',12))
login_btn.pack()

input_txt1 = Label(root, text = 'Please input your username and password!', bg='lightblue')
input_txt1.config(pady=10)
input_txt1.pack()

input_txt2 = Label(root, text = 'Welcome to Cat World Service!', bg='lightblue',font=('Script MT Bold',16))
input_txt2.config(pady=3)
input_txt2.pack()

root.mainloop()
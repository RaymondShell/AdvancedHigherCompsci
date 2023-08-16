from tkinter import *
from MySqlDatabase import closeDatabase, Add_Data
from functions import *
window = Tk()
window.geometry("340x440")
signUpConfirmation = False
loginConfirmation = False
def unloadAll():
    Starter.pack_forget()
    gotoLogin.pack_forget()
    gotoSignup.pack_forget()
    labelUsr.grid_forget()
    username.grid_forget()
    labelPswrd.grid_forget()
    password.grid_forget()
    SignUp.grid_forget()
def prepLogin():
    window.geometry("420x231")
    unloadAll()

def prepSignup():
    window.geometry("340x440")
    unloadAll()
    labelUsr.grid(row=1, column=0)
    username.grid(row=1, column=1)
    labelPswrd.grid(row=2, column=0)
    password.grid(row=2, column=1)
    SignUp.grid(row=3, column=1, columnspan=2)
    window.mainloop()

def getData_AddData():
    global signUpConfirmation
    global loginConfirmation
    usrname = username.get()
    pssword = password.get()
    signUpConfirmation = Add_Data(usrname, pssword)
    if signUpConfirmation == True:
        unloadAll()
        prepLogin()
    if loginConfirmation == True:
        unloadAll()



Starter = Label(text="Would you like to Login Or Signup?")
gotoLogin = Button(text="Login", command=prepLogin)
gotoSignup = Button(text="Signup", command=prepSignup)
SignUp = Button(window, text="Sign Up", command=getData_AddData)
username = Entry(window)
password = Entry(window, show="*")
labelUsr = Label(window, text="Username")
labelPswrd = Label(window, text="Password")
Starter.pack()
gotoSignup.pack()
gotoLogin.pack()
window.mainloop()

closeDatabase()
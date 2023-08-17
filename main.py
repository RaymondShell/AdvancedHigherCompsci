from tkinter import *
from MySqlDatabase import closeDatabase, Add_Data, check_Data
from functions import *
window = Tk()
window.geometry("340x440")
signUpConfirmation = False
def unloadAll():
    Starter.pack_forget()
    gotoLogin.pack_forget()
    gotoSignup.pack_forget()
    labelUsr.grid_forget()
    username.grid_forget()
    labelPswrd.grid_forget()
    password.grid_forget()
    SignUp.grid_forget()
    SignIn.grid_forget()
def prepLogin():
    window.geometry("420x231")
    unloadAll()
    labelUsr.grid(row=1, column=0)
    username.grid(row=1, column=1)
    labelPswrd.grid(row=2, column=0)
    password.grid(row=2, column=1)
    SignIn.grid(row=3, column=1, columnspan=2)
    window.mainloop()

def prepSignup():
    window.geometry("340x440")
    unloadAll()
    labelUsr.grid(row=1, column=0)
    username.grid(row=1, column=1)
    labelPswrd.grid(row=2, column=0)
    password.grid(row=2, column=1)
    SignUp.grid(row=3, column=1, columnspan=2)
    window.mainloop()

def signUp():
    signUpConfirmation = False
    usrname = username.get()
    pssword = password.get()
    if len(usrname) > 0 and len(pssword) > 0:
        signUpConfirmation = Add_Data(usrname, pssword)
        print(signUpConfirmation)
        if signUpConfirmation == True:
            unloadAll()
            prepLogin()
        if signUpConfirmation == "EXISTS":
            openPopup("Username already Exists Please Try A New One")
    else:
        openPopup("Please Ensure the Username and password boxes are not empty")

def loginCheck():
    signInConfirmation = False
    usrname = username.get()
    pssword = password.get()
    signInConfirmation = check_Data(usrname, pssword)
    if signInConfirmation == True:
        unloadAll()
        prepMain()

def openPopup(text):
    top = Toplevel(window)
    top.geometry("1000x100")
    top.title("Child Window")
    def exit_btn():
        top.destroy()
        top.update()
    Label(top, text=text, font=('Mistral 18 bold'), anchor='center').pack()
    Button(top, text="ok", command=exit_btn, width=10).pack()
def prepMain():
    print("Goat")


Starter = Label(text="Would you like to Login Or Signup?")
gotoLogin = Button(text="Login", command=prepLogin)
gotoSignup = Button(text="Signup", command=prepSignup)
SignUp = Button(window, text="Sign Up", command=signUp)
SignIn = Button(window, text="Sign In", command=loginCheck)
username = Entry(window)
password = Entry(window, show="*")
labelUsr = Label(window, text="Username")
labelPswrd = Label(window, text="Password")
Starter.pack()
gotoSignup.pack()
gotoLogin.pack()
window.mainloop()

closeDatabase()
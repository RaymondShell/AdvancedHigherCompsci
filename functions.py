def prepLogin():
    window.geometry("420x231")
    Starter.pack_forget()
    gotoLogin.pack_forget()
    gotoSignup.pack_forget()

def prepSignup():
    window.geometry("420x231")
    Starter.pack_forget()
    gotoLogin.pack_forget()
    gotoSignup.pack_forget()
    SignUp = Button(window, text="Sign Up", command=getData_AddData)
    SignUp.pack()
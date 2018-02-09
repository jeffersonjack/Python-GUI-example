from tkinter import *
from tkinter import messagebox

import users

class Login:
    def verifyLogin(self, key=None):
        print(users.users)
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        
        print("Username: " + username + "\nPassword: " + password)
        
        # clear the form
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)
        self.usernameEntry.focus_set()

        # check credentials
        status = users.verify(username, password)
        if status == 0:    # success
            self.statusLabel.config(text="", fg="black")
            messagebox.showinfo("Information", "Login successful")
        else:              # fail
            self.statusLabel.config(text="Incorrect username/password", fg="red")

    def __init__(self, master):
        # create a new frame to hold the login form
        form = Frame(master)
        # make the frame visible
        form.pack()

        # define some elements...
        self.usernameLabel = Label(form, text="Username")
        self.usernameEntry = Entry(form)
        self.passwordLabel = Label(form, text="Password")
        self.passwordEntry = Entry(form, show="*")
        self.statusLabel = Label(form)
        self.loginButton = Button(form, text="Log in", command=self.verifyLogin)

        # ...and make them visible by adding them to the grid
        self.usernameLabel.grid(row=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1)
        self.passwordEntry.grid(row=1, column=1)
        self.statusLabel.grid(row=2, columnspan=2)
        self.loginButton.grid(row=3, columnspan=2)
        self.usernameEntry.focus_set()
        
        # Effectively bind the Return key to the "log in" button
        master.bind("<Return>", self.verifyLogin)

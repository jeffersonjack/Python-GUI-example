from tkinter import *

from login import *
import users

if __name__ == '__main__':
    # load the users
    users.loadUsers()
    users.addUser("user", "pw")
    
    window = Tk()
    window.title("Log in")
    window.geometry("300x100")
    loginForm = Login(window)
    
    window.mainloop()
    users.saveUsers()

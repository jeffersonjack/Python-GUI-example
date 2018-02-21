from tkinter import *

class Form:
    ## This is the constructor, it is run when you create a new Form object
    ## e.g. myform = Form(...)
    ## Everything that you see on the form needs to be defined in here
    def __init__(self, master):
        # All of the objects need to go inside of a frame
        form = Frame(master)
        # Make the frame visible
        form.pack()

        #### Elements are defined here ####
        self.label1 = Label(form, text="Look, a text box:")   # The `(form)` bit means "this
        self.textEntry1 = Entry(form)                           # element is to be put on the
                                                                # form (which we defined above)
        self.label2 = Label(form, text="Password")
        self.textEntry2 = Entry(form, show="*")   # `show="*"` means that * will be displayed
        
        self.label3 = Label(form, text="I'm blue and in the middle", fg="blue")

        self.check1 = Checkbutton(form, text="Tick me")
        ###################################

        
        ### Now make everything visible ###
        self.label1.grid(row=0)                # The first row is row 0, the second is row 1
        self.textEntry1.grid(row=0, column=1)

        self.label2.grid(row=1)                # Because we want the first column, we don't have to specify it
        self.textEntry2.grid(row=1, column=1)

        self.label3.grid(row=2, columnspan=2)  # This spans 2 columns, so it's in the middle

        self.check1.grid(row=3)
        ###################################
        
window = Tk()
f = Form(window)
window.mainloop()

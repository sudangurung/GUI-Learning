from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "Enter your name.")

def myclick():
    mylabel = Label(root, text="Hello " + e.get())
    mylabel.pack()

myButton = Button(root, text="Enter your name.", command=myclick)
myButton.pack()

root.mainloop()
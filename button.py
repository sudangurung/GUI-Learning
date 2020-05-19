from tkinter import *

root = Tk()

def myclick():
    mylabel = Label(root, text="Look! I clicked a button!!!")
    mylabel.pack()

myButton = Button(root, text="Click Me!", command=myclick)
myButton.pack()

root.mainloop()
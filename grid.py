from tkinter import *

root = Tk()

# creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="My name is Sudan Gurung.")
# instead shoving it onto the screen we use the grid function to put the labels in a grid.
myLabel1.grid(row=0, column=0)
mylabel2.grid(row=1,column=0)

root.mainloop()
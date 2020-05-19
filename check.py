from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")
root.geometry("400x400")

def show():
    mylabel = Label(root, text=var.get()).pack()

var = StringVar()

#You can change the values of the check by passing the onvalue and offvalue.
c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

mylabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
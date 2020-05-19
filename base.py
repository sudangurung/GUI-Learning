from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")

def open():
    top = Toplevel()
    top.title("My second window.")
    top.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")
    lbl = Label(top, text="Hello World").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()
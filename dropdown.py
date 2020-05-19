from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")
root.geometry("400x400")

# Drop Down Boxes
def show():
    mylabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked,*options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
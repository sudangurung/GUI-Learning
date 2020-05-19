from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")

#creates a variable r and set it at 2
#r = IntVar()
#r.set("2")

#creates a list with tuples
MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

#creates a fucntion to show the value of the option being clicked.
def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

#creats a radio button
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#creates a label to showcase the option being clicked
mylabel = Label(root, text=pizza.get())
mylabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
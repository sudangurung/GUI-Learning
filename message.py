from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")

#You can create different messagebox. Just replace the showinfo with followng:
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my popup!", "Hello world!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You have clicked yes!").pack()
    else:
        Label(root, text="You have clicked no!!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()
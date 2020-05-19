from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/grgsu/PycharmProjects/GUI/Images",
                                               title="Select a File",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    mylabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text="Open File", command=open).pack()

root.mainloop()
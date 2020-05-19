from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("My favourite legends.")
root.iconbitmap("C:/Users/grgsu/PycharmProjects/GUI/Wattson.ico")

#creates a frame
frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

#puts the button in the frame
b = Button(frame, text="Don't click this button!!")
b.pack()







root.mainloop()
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames whatever that is')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0)

b2 = Button(frame, text="..or click here")
b2.grid(row=1, column=1)








root.mainloop()
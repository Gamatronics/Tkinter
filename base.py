from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Create more windows')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')

def open():
    global my_image
    top = Toplevel()
    top.title('aleluya')
    top.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')
    my_image = ImageTk.PhotoImage(Image.open("C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/pass.png"))
    label = Label(top, image=my_image).pack()
    button2 = Button(top, text="close window", command=root.destroy).pack()

button = Button(root, text="Open second window", command=open).pack()












root.mainloop()
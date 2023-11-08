from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Sliders')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')
root.geometry("400x400")

def show():
    my_label = Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])
#Need a start before the list for the options for some reason
drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text="Show Selection", command=show).pack()




root.mainloop()
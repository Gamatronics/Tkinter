from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Sliders')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_label= Label(root, text=horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()




my_button = Button(root, text="Click me", command=slide).pack()










root.mainloop()
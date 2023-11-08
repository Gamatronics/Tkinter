from tkinter import *

root = Tk()

# Creating a label widget
my_label = Label(root, text="Hello World!").grid(row=0, column=0)
my_label2 = Label(root, text="My Name is Gaston Motola").grid(row=1, column=5)

# Shoving it onto screen
""" my_label.grid(row=0, column=0)
my_label2.grid(row=1, column=5) """


root.mainloop()

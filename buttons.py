from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="Look! I clicked a button")
    my_label.pack()


my_button = Button(root, text="Click Me!", command=my_click, fg="blue", bg="#00FF00")

my_button.pack()

root.mainloop()

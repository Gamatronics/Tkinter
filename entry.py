from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Entre Your Name: ")


def my_click():
    hello = f"Hello {e.get()}"
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="Enter your name", command=my_click)

my_button.pack()

root.mainloop()

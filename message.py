from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Messages')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/cocktail.ico')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
   response = messagebox.showinfo("This is my pop-up", "Hello World!")
   Label(root, text=response).pack()
"""    if response == "yes":
        Label(root, text="you clicked yes").pack()
   else:
        Label(root, text="you clicked no").pack() """

Button(root, text="pop-up", command=popup).pack()












root.mainloop()
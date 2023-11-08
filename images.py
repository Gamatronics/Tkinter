from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Hola que tal icono")
#root.iconbitmap('cocktail.ico')
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/toy_airplane.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/compu.png'))
my_label = Label(image = my_image)
my_label.pack()







button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()







root.mainloop()
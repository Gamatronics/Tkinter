from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Image Viewer")
root.iconbitmap('C:/Users/gmoto/Documents/PythonScripts/Tkinter/toy_airplane.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/compu.png'))
my_image1 = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/marketing.png'))
my_image2 = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/pass.png'))
my_image3 = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/logo.png'))
my_image4 = ImageTk.PhotoImage(Image.open('C:/Users/gmoto/Documents/PythonScripts/Tkinter/images/bluelogo.png'))

image_list = [my_image, my_image1, my_image2, my_image3, my_image4 ]

status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image = my_image)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text='>>', state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    



def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", command=back, state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)







root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\leone\\Desktop\\Python\\TKinter\\TKinter', title='Select File', filetypes=(('png files', '*.png'),('all files', '*.*')))
    my_label = Label(root).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

root = Tk()



button = Button(root, text='Open File', command=open).pack()

mainloop()
from tkinter import *
from PIL import ImageTk, Image

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(f'{horizontal.get()}x{vertical.get()}')


root = Tk()
root.geometry('400x400')

vertical = Scale(root, from_=400, to=0)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# my_label = Label(root, text=horizontal.get()).pack()

my_button = Button(root, text='Click Me!', command=slide).pack()

mainloop()
from tkinter import *
from PIL import ImageTk, Image 

def open():
    top = Toplevel()
    top.title('Second window')
    label = Label(top, text='Hello World!').pack()
    button2 = Button(top, text='Close window', command=quit).pack(padx=10, pady=10)

root = Tk()

button = Button(root, text='Open Second Window', command=open).pack(padx=50, pady=50)

mainloop()
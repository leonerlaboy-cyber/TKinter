from tkinter import *

def show():
    my_label = Label(root, text=var.get()).pack()


root = Tk()
root.geometry('400x400')

var = StringVar()

c = Checkbutton(root, text='Click this box for super size!', variable=var, onvalue= "Super Size", offvalue="Regular Size")
c.deselect()
c.pack()

button = Button(root, text='Meal size', command=show)
button.pack()

mainloop()
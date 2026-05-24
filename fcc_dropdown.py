from tkinter import *

def show():
    my_label = Label(root, text=clicked.get())
    my_label.pack()

root = Tk()
root.geometry('400x400')

options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

button = Button(root, text='Show Selection', command=show)
button.pack()

mainloop()
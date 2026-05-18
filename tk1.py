from tkinter import *
from PIL import Image, ImageTk

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk() 

image = Image.open('cow.png')
image = image.resize((120, 120))
photo = ImageTk.PhotoImage(image)

button = Button(window,
                text='Click me!',
                command=click,
                font=('Comic Sans', 30),
                fg='green',
                bg='black',
                activeforeground='white',
                activebackground='black',
                image=photo,
                compound='bottom')

button.pack()


window.mainloop()
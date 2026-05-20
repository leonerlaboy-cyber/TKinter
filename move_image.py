from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x() - 10, y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x() + 10, y=label.winfo_y())

# window = Tk()
# window.geometry('500x500')

# window.bind('<w>', move_up)
# window.bind('<s>', move_down)
# window.bind('<a>', move_left)
# window.bind('<d>', move_right)

# my_image = PhotoImage(file='pizza.png')
# label = Label(window, image=my_image)
# label.place(x=0,y=0)

# window.mainloop()


# ---------------------------------------------------------------------------
                 # This section is to learn how to move an image on a canvas


def move_up(event):
    canvas.move(my_image, 0,-10)

def move_down(event):
    canvas.move(my_image, 0,10)

def move_left(event):
    canvas.move(my_image, -10,0)

def move_right(event):
    canvas.move(my_image, +10, 0)

window = Tk()

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

image = PhotoImage(file='pizza.png')
my_image = canvas.create_image(0,0,image=image, anchor=NW)



window.mainloop()
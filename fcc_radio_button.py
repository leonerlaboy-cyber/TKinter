from tkinter import *

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

root = Tk()
root.title('Learn to code')

# r = IntVar()
# r.set('2')

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# my_label = Label(root, text=pizza.get())
# my_label.pack()

my_button = Button(root, text='Click Me!', command=lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()
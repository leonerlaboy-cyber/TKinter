from tkinter import *

def submit():

    food = []

    for index in list_box.curselection():
        food.insert(index, list_box.get(index))

    # print(f'You have ordered {list_box.get(list_box.curselection())} ')
    print('You have ordered: ')
    for index in food:
        print(index)

def add():
    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height=list_box.size())

def delete():
    # list_box.delete(list_box.curselection())
    for index in reversed(list_box.curselection()):
        list_box.delete(index)

    list_box.config(height=list_box.size())

window = Tk()

list_box = Listbox(window,
                   bg='#f7ffde',
                   font=('Constantia',35),
                   width=12,
                   selectmode=MULTIPLE)
list_box.pack()

list_box.insert(1, 'pizza')
list_box.insert(2, 'pasta')
list_box.insert(3, 'garlic bread')
list_box.insert(4, 'soup')
list_box.insert(5, 'salad')

list_box.config(height=list_box.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text='Submit', command=submit)
submit_button.pack()

add_button = Button(window,
                       text='add', command=add)
add_button.pack()

delete_button = Button(window,
                       text='delete', command=delete)
delete_button.pack()

window.mainloop()
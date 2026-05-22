from tkinter import *

def myClick():
    hello = 'Hello ' + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()

def escape():
    root.destroy()

root = Tk()
root.geometry('500x500')

e = Entry(root, width=50)
e.pack()
# e.insert(0, 'Enter your name')

my_button = Button(root, font=('Arial', 15), text='Enter your name', command=myClick, fg='orange', bg='purple')
my_button.pack()

exit_button = Button(root, text='Exit', command=escape)
exit_button.pack()

root.mainloop()








# my_label = Label(root, text='Hello World!')
# my_label2 = Label(root, text='My name is John Elder')

# my_label.grid(row=0, column=0)
# my_label2.grid(row=1, column=0)
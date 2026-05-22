from tkinter import *

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    num1 = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(num1)
    e.delete(0, END)

def button_equal():
    num2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(num2))
    elif math == 'subtraction':
        e.insert(0, f_num - int(num2))
    elif math == 'multiplication':
        e.insert(0, f_num * int(num2))
    elif math == 'division':
        e.insert(0, f_num / int(num2))

def button_subtract():
    num1 = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(num1)
    e.delete(0, END)

def button_multiply():
    num1 = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(num1)
    e.delete(0, END)

def button_divide():
    num1 = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(num1)
    e.delete(0, END)
    

def escape():
    root.destroy()


root = Tk()
# root.geometry('500x500')
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# e.insert(0, '')

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
add_button = Button(root, text='+', padx=40, pady=20, command= button_add)
equal_button = Button(root, text='=', padx=91, pady=20, command=button_equal)
clear_button = Button(root, text='Clear', padx=79, pady=20, command=button_clear)

subtract_button = Button(root, text='-', padx=41, pady=20, command= button_subtract)
multiply_button = Button(root, text='*', padx=40, pady=20, command= button_multiply)
divide_button = Button(root, text='/', padx=42, pady=20, command= button_divide)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
clear_button.grid(row=4, column=1, columnspan=2)
add_button.grid(row=5, column=0)
equal_button.grid(row=5, column=1, columnspan=2)

subtract_button.grid(row=6, column= 0)
multiply_button.grid(row=6, column= 1)
divide_button.grid(row=6, column= 2)

# my_button = Button(root, font=('Arial', 15), text='Enter your name', command=myClick, fg='orange', bg='purple')


# exit_button = Button(root, text='Exit', command=escape)
# exit_button.grid()

root.mainloop()
from tkinter import *

root= Tk()
root.title('Learn to Code')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

label = Label(frame, text='Hello aliens!')
label.pack()

b = Button(frame, text='Don\'t click here!')
b.pack()


root.mainloop()
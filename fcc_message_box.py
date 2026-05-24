from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno     

def popup():
    response = messagebox.askyesno('This is my popup', 'Hello World!')
    # Label(root, text=response).pack()

    if response == 1:
        Label(root, text='You clicked Yes!').pack()
    else:
        Label(root, text='You clicked No!').pack()

root = Tk()
root.title('Learn to code')

Button(root, text='Popup', command=popup).pack()



root.mainloop()
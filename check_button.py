from tkinter import *
from PIL import Image, ImageTk

def display():
    if(x.get()==1):
        print('You agree!')
    else:
        print('You don\'t agree :(')

window = Tk()

x = IntVar()

image = Image.open('python.png')
image = image.resize((120, 120))
python_photo = ImageTk.PhotoImage(image)

check_button = Checkbutton(window,
                           text='I agree to something',
                           variable= x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='Green',
                           bg='Black',
                           activeforeground='Green',
                           activebackground='Black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound=LEFT)
check_button.pack()



window.mainloop()
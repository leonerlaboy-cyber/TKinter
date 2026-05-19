from tkinter import *

def submit():
    user_input = text.get('1.0', END)
    print(user_input)

window = Tk()

text = Text(window,
            bg='Light Yellow',
            font=('Ink Free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='Purple')

text.pack()
button = Button(window,text='submit',command=submit)
button.pack()



window.mainloop()
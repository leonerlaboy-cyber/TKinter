from tkinter import *

def submit():
    username = entry.get()
    print(f'Hello {username}')
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg='Green',
              bg='Black',
              show='*')

entry.insert(0,'Spongebob')
entry.pack(side=LEFT)

submit_bttn = Button(window, text= 'Submit', command=submit)
submit_bttn.pack(side=RIGHT)

delete_bttn = Button(window, text= 'Delete', command=delete)
delete_bttn.pack(side=RIGHT)

backspace_bttn = Button(window, text= 'Backspace', command=backspace)
backspace_bttn.pack(side=RIGHT)

window.mainloop()
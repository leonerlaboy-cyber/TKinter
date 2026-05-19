from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir='C:\\Users\\leone\\Desktop\\Python\\TKinter\\TKinter',
                                           title='Open file okay?',
                                           filetypes=(('text files','*.txt'),
                                           ('all files', '*.*')))
    with open(file_path, 'r') as file:
        print(file.read())

window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()


window.mainloop()

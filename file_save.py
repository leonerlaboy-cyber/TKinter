from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\leone\\Desktop\\Python\\TKinter\\TKinter',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*'),])
    # file_text = input('Enter some text: ') This is for using the console instead of the text widget to enter text
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()


window.mainloop()
from tkinter import * 
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir='C:\\Users\\leone\\Desktop\\Python\\TKinter\\TKinter',
                                           title='Open file okay?',
                                           filetypes=(('text files','*.txt'),
                                           ('all files', '*.*')))
    if file_path:
        with open(file_path, 'r') as file:
            contents = file.read()

        text.delete('1.0', END)      # clear old text
        text.insert('1.0', contents) # put file text into the box

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\leone\\Desktop\\Python\\TKinter\\TKinter',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*'),])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

window = Tk()

menu_bar = Menu(window)
window.config(menu=menu_bar) 

file_menu = Menu(menu_bar, tearoff=0, font=('MV Boli', 15))
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command= openFile)
file_menu.add_command(label='Save', command=saveFile)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

edit_menu = Menu(menu_bar, tearoff=0, font=('MV Boli', 15))
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command= cut)
edit_menu.add_command(label='Copy', command= copy)
edit_menu.add_command(label='Paste', command= paste)

text = Text(window)
text.pack()

window.mainloop()
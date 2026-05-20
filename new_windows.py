from tkinter import *

def create_window():
    # new_window = Toplevel() # new window 'on top' of other windows, linked to a bottom window. Closing a bottom level window causes any top levels above it to close as well.
    new_window = Tk() # new INDEPENDENT window

    original_window.destroy() #'.destroy' closes a window

original_window = Tk()

Button(original_window, text='create new window', command=create_window).pack()    



original_window.mainloop()
from tkinter import *

def doSomething(event):
    print(f'You clicked coordinate: {event.x},{event.y}')

window = Tk()

# window.bind('<Button-1>', doSomething) #Button-1 is left mouse button
# window.bind('<Button-2>', doSomething) # scoll wheel click
# window.bind('<Button-3>', doSomething) # right mouse button
# window.bind('<ButtonRelease>', doSomething) # does an action on release of a button
# window.bind('<Enter>', doSomething)#  #does an action when mouse enters window
# window.bind('<Leave>', doSomething) #does an action when mouse leaves window
window.bind('<Motion>', doSomething) #action when mouse moved

window.mainloop()
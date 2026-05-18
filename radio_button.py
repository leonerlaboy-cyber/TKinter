from tkinter import *

food = ['Pizza', 'Hamburger', 'Hotdog']

def order():
    if(x.get()==0):
        print('You ordered pizza!')
    elif(x.get()==1):
        print('You ordered a burger!')
    elif(x.get()==2):
        print('You ordered a hotdog!')
    else:
        print('huh?')


window = Tk()


pizzaImage = PhotoImage(file='pizza.png')
burgerImage = PhotoImage(file='burger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, burgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                               text=food[index], #adds text to radio buttons
                               variable=x, #groups radiobuttons together if share same variable
                               value=index,
                               padx=25,
                               font=('Impact', 50), #assigns each radiobutton a different value
                               image = foodImages[index], #adds image to radiobutton
                               compound='left',
                               command=order)
                            #    indicatoron=0,
                            #    width= 375) 

    radiobutton.pack(anchor=W)

window.mainloop()
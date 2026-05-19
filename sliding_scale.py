from tkinter import *

def submit():
    print(f'The temperature is: {scale.get()} degrees C')

window = Tk()

hotImage = PhotoImage(file='flame.png')
hotImage = hotImage.subsample(6, 6)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, from_=100, to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval= 10,
            #   showvalue= 0,
              resolution= 5,
              troughcolor= '#69FAFF',
              fg='#FF1C00',
              bg='#111111')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file='snowflake.png')
coldImage = coldImage.subsample(2, 2)
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import time

WIDTH = 500
HEIGHT = 500 
x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

image = Image.open("winter_landscape.png")
image = image.resize((WIDTH, HEIGHT))
background_photo = ImageTk.PhotoImage(image)

background = canvas.create_image(0, 0, image=background_photo, anchor=NW)


my_image = PhotoImage(file='snowflake.png')
my_image = my_image.subsample(3,3)
image = canvas.create_image(0,0,image=my_image, anchor=NW)

image_width = my_image.width()
image_height = my_image.height()

while True:
    coordinates = canvas.coords(image)
    print(coordinates)
    if (coordinates[0] >= WIDTH - image_width) or  coordinates[0] < 0:
        x_velocity = -x_velocity
    
    if (coordinates[1] >= HEIGHT - image_height) or  coordinates[1] < 0:
        y_velocity = -y_velocity

    canvas.move(image, x_velocity, y_velocity)
    # canvas.move(image, 0, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
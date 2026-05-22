from tkinter import *
from PIL import ImageTk, Image

def forward(img_num):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num - 1])
    forward_button = Button(root, text='>>', command=lambda: forward(img_num + 1))
    back_button = Button(root, text='<<', command=lambda: back(img_num - 1))

    if img_num == len(img_list):
        forward_button = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)


def back(img_num):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num - 1])
    forward_button = Button(root, text='>>', command=lambda: forward(img_num + 1))
    back_button = Button(root, text='<<', command=lambda: back(img_num - 1))

    if img_num == 1:
        back_button = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

root = Tk()
root.title('Make images')
root.iconphoto(True, PhotoImage(file='pizza.png'))
#root.iconbitmap() was used in tutorial

my_img1 = ImageTk.PhotoImage(Image.open('pizza.png'))
my_img2 = Image.open('flame.png')
my_img2 = my_img2.resize((300, 300))
my_img2 = ImageTk.PhotoImage(my_img2)
my_img3 = ImageTk.PhotoImage(Image.open('hotdog.png'))
my_img4 = ImageTk.PhotoImage(Image.open('burger.png'))
my_img5 = ImageTk.PhotoImage(Image.open('python.png'))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

back_button = Button(root, text='<<', command=back, state=DISABLED)
exit_button = Button(root, text='Exit Program', command=root.quit)
forward_button = Button(root, text='>>', command=lambda: forward(2))

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()
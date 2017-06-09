from tkinter import *

from PIL import Image, ImageTk

root = Tk()

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=900, width=1600, relief=RAISED, bg='black')
canvas.grid() #Puts the canvas in the main Tk window

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, './resources/screens/loading.bmp')
filename2 = os.path.join(directory, './resources/screens/test.jpg')

# open the image file and convert to an ImageTk object

img = Image.open(filename)
photo = ImageTk.PhotoImage(img)
label = Label(image=photo)
label.place(x=0, y=0)
label.image = photo

img2 = Image.open(filename2)
photo2 = ImageTk.PhotoImage(img2)

def changeimage():
    label.configure(image=photo2)


button = Button(root, text="start", command=changeimage)
button.place(x=0, y=0)

root.mainloop()
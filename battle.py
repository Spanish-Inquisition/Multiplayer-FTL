from tkinter import *
root = Tk()

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=1000, width=2000, relief=RAISED, bg='black')
canvas.grid() #Puts the canvas in the main Tk window

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, './resources/screens/fight.bmp')

# open the image file and convert to an ImageTk object
import PIL.Image, PIL.ImageTk

width, height = canvas.size()
img = PIL.Image.open(filename)  # create a PIL.Image from the jpg file
img = img.resize((2000, 1000))

tkimg = PIL.ImageTk.PhotoImage(img)  # convert the PIL.Image to a PIL.TkImage

# add the ImageTk object to the canvas
icon = canvas.create_image(1000, 500, image=tkimg)

root.mainloop()
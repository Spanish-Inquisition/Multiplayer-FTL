from tkinter import *

root = Tk()

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=900, width=1600, relief=RAISED, bg='black')
canvas.grid() #Puts the canvas in the main Tk window

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, './resources/screens/fight.bmp')

# open the image file and convert to an ImageTk object
import PIL.Image, PIL.ImageTk

bg = PIL.Image.open(filename)  # create a PIL.Image from the jpg file
bg = bg.resize((1600, 900))

ship1 = PIL.Image.open("./resources/images/Stealth.PNG")
ship1 = ship1.resize((700, 400))
ship1 = ship1.rotate(180)

ship2 = PIL.Image.open("./resources/images/Federation.PNG")
ship2 = ship2.resize((700, 400))

bgimg = PIL.ImageTk.PhotoImage(bg)  # convert the PIL.Image to a PIL.TkImage
s1img = PIL.ImageTk.PhotoImage(ship1)
s2img = PIL.ImageTk.PhotoImage(ship2)

# add the ImageTk object to the canvas
background = canvas.create_image(800, 450, image=bgimg)
redship = canvas.create_image(400, 450, image=s2img)
blueship = canvas.create_image(1200, 450, image=s1img)



root.mainloop()
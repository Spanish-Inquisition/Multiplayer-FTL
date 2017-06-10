from tkinter import *
from PIL import Image, ImageTk

root = Tk()

red_ship_scrap = 800
blue_ship_scrap = 800

"""SYSTEMS"""
red_shield_lvl = 0
blue_shield_lvl = 0
shield_lvl_cost = [125, 20, 30, 40, 60, 80, 100]

red_engine_lvl = 0
blue_engine_lvl = 0
engine_lvl_cost = [0, 10, 15, 30, 40, 60, 80, 120]

red_wep_lvl = 0
blue_wep_lvl = 0
wep_lvl_cost = [0, 10, 25, 30, 45, 60, 80, 100]

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=900, width=1600, relief=RAISED, bg='black')
canvas.grid()  # Puts the canvas in the main Tk window

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
start_filename = os.path.join(directory, './resources/screens/start.bmp')
redsetup_filename = os.path.join(directory, './resources/screens/redSetup.bmp')
bluesetup_filename = os.path.join(directory, './resources/screens/blueSetup.bmp')
# open the image file and convert to an ImageTk object

start_img = Image.open(start_filename)
start_img = start_img.resize((1600, 900))
start_photo = ImageTk.PhotoImage(start_img)
background = Label(image=start_photo)
background.place(x=0, y=0)
background.image = start_photo

redsetup_img = Image.open(redsetup_filename)
redsetup_img = redsetup_img.resize((1600, 900))
redsetup_photo = ImageTk.PhotoImage(redsetup_img)

bluesetup_img = Image.open(bluesetup_filename)
bluesetup_img = bluesetup_img.resize((1600, 900))
bluesetup_photo = ImageTk.PhotoImage(bluesetup_img)

oldy = -100
newy = 678


def changeimagefirst():
    background.configure(image=redsetup_photo)
    button.configure(command=changeimageblue, text="<Red End Turn> ")



def changeimageblue():
    background.configure(image=bluesetup_photo)
    button.configure(command=changeimagered, text="<Blue End Turn>")



def changeimagered():
    background.configure(image=redsetup_photo)
    button.configure(command=changeimageblue, text="<Red End Turn> ")


button = Button(root, text="START", command=changeimagefirst, bd=8, font=("Fixedsys", 40), bg="black", fg="white")
button.place(x=720, y=700)

"""COSTS AND STUFF"""

red_scrap = Label(text=" RED SCRAP: " + str(red_ship_scrap))
red_scrap.place(x=0, y=oldy)

blue_scrap = Label(text="BLUE SCRAP: " + str(blue_ship_scrap), state=DISABLED)
blue_scrap.place(x=1500, y=oldy)


root.mainloop()

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

canvas = Canvas(root, height=900, width=1600, relief=RAISED, bg='black')
canvas.grid()

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
start_filename = os.path.join(directory, './resources/screens/start.bmp')
redsetup_filename = os.path.join(directory, './resources/screens/redSetup.bmp')
bluesetup_filename = os.path.join(directory, './resources/screens/blueSetup.bmp')
# filenames and stuff

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

oldy = -800 #moves buttons from offscreen to on screen. Negative values make them 'invisible'
scrap_newy = 16
shield_newy = 678
engine_newy = 748
wep_newy = 818


def changeimagefirst():
    redturn()
    button.place(x=540, y=670)
    red_scrap.place(y=scrap_newy)
    blue_scrap.place(y=scrap_newy)


def changeimageblue(): #NEED TO DISABLE OTHER TEAMS BUTTONS WHEN IT CHANGES
    blueturn()

def changeimagered():
    redturn()
    background.configure(image=redsetup_photo)
    button.configure(command=changeimageblue, text="<Red End Turn>")
    button.place(x=540)

button = Button(root, text="START", command=changeimagefirst, bd=8, font=("Fixedsys", 40), bg="black", fg="white")
button.place(x=680, y=700)

def redturn():
    background.configure(image=redsetup_photo)
    button.configure(command=changeimageblue, text="<Red End Turn>")
    button.place(x=540, y=670)
    #reverse all buttons
    #red
    redshieldbutton.place(x=10, y=shield_newy)
    redenginebutton.place(x=10, y=engine_newy)
    redwepbutton.place(x=10, y=wep_newy)
    #blue
    blueshieldbutton.place(x=10, y=oldy)
    blueenginebutton.place(x=10, y=oldy)
    bluewepbutton.place(x=10, y=oldy)

def blueturn():
    background.configure(image=bluesetup_photo)
    button.configure(command=changeimagered, text="<Blue End Turn>")
    button.place(x=535)
    #reverse all buttons
    #red
    redshieldbutton.place(x=10, y=oldy)
    redenginebutton.place(x=10, y=oldy)
    redwepbutton.place(x=10, y=oldy)
    #blue
    blueshieldbutton.place(x=10, y=shield_newy)
    blueenginebutton.place(x=10, y=engine_newy)
    bluewepbutton.place(x=10, y=wep_newy)

"""COSTS AND STUFF"""

red_scrap = Label(text="RED SCRAP: " + str(red_ship_scrap), bd=8, font=("Fixedsys", 20), bg="red", fg="black")
red_scrap.place(x=10, y=oldy)

blue_scrap = Label(text="BLUE SCRAP: " + str(blue_ship_scrap), bd=8, font=("Fixedsys", 20), bg="blue", fg="black")
blue_scrap.place(x=1330, y=oldy)

"""

SYSTEM UPGRADES

"""


"""
SHIELD
"""

def redupgradeshield():  #MAY WANT TO PRINT COST OF NEXT UPGRADE
    global red_shield_lvl
    global red_ship_scrap
    if red_shield_lvl == 5:
        red_shield_lvl += 1
        red_ship_scrap -= shield_lvl_cost[red_shield_lvl]
        redshieldbutton.configure(text="Shield Level: " + str(red_shield_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
    elif red_shield_lvl < 6 and (red_ship_scrap - shield_lvl_cost[red_shield_lvl]) > 0:
        red_shield_lvl += 1
        red_ship_scrap -= shield_lvl_cost[red_shield_lvl]
        redshieldbutton.configure(text="Shield Level: " + str(red_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[red_shield_lvl + 1]))
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
        if red_shield_lvl == 6:
            redshieldbutton.configure(state=DISABLED)
    else:
        print("NOPE")


redshieldbutton = Button(root, width=32, text="Shield Level: " + str(red_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[red_shield_lvl + 1]), command=redupgradeshield, bd=2, font=("Fixedsys", 18), bg="red", fg="black")
redshieldbutton.place(x=10, y=oldy)

def blueupgradeshield():
    global blue_shield_lvl
    global blue_ship_scrap
    if blue_shield_lvl == 5:
        blue_shield_lvl += 1
        blue_ship_scrap -= shield_lvl_cost[blue_shield_lvl]
        blueshieldbutton.configure(text="Shield Level: " + str(blue_shield_lvl) + " MAX LEVEL")
        blue_scrap.configure(text=" BLUE SCRAP: " + str(blue_ship_scrap))
    elif blue_shield_lvl < 6 and (blue_ship_scrap - shield_lvl_cost[blue_shield_lvl]) > 0:
        blue_shield_lvl += 1
        blue_ship_scrap -= shield_lvl_cost[blue_shield_lvl]
        blueshieldbutton.configure(text="Shield Level: " + str(blue_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[blue_shield_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_shield_lvl == 6:
            blueshieldbutton.configure(state=DISABLED)
    else:
        print("NOPE")


blueshieldbutton = Button(root, width=32, text="Shield Level: " + str(blue_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[blue_shield_lvl + 1]), command=blueupgradeshield, bd=2, font=("Fixedsys", 18), bg="blue", fg="black")
blueshieldbutton.place(x=10, y=oldy)

"""
END SHIELD
"""

"""
ENGINE
"""

def redupgradeengine():  #MAY WANT TO PRINT COST OF NEXT UPGRADE
    global red_engine_lvl
    global red_ship_scrap
    if red_engine_lvl == 6:
        red_engine_lvl += 1
        red_ship_scrap -= engine_lvl_cost[red_engine_lvl]
        redenginebutton.configure(text="Engine Level: " + str(red_engine_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
    elif red_engine_lvl < 7 and (red_ship_scrap - engine_lvl_cost[red_engine_lvl]) > 0:
        red_engine_lvl += 1
        red_ship_scrap -= engine_lvl_cost[red_engine_lvl]
        redenginebutton.configure(text="Engine Level: " + str(red_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[red_engine_lvl + 1]))
        red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
        if red_engine_lvl == 7:
            redenginebutton.configure(state=DISABLED)
    else:
        print("NOPE")


redenginebutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="red", fg="black", text="Engine Level: " + str(red_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[blue_engine_lvl + 1]), command=redupgradeengine)
redenginebutton.place(x=0, y=oldy)

def blueupgradeengine():
    global blue_engine_lvl
    global blue_ship_scrap
    if blue_engine_lvl == 6:
        blue_engine_lvl += 1
        blue_ship_scrap -= engine_lvl_cost[blue_engine_lvl]
        blueenginebutton.configure(text="Engine Level: " + str(blue_engine_lvl) + " MAX LEVEL")
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
    elif blue_engine_lvl < 7 and (blue_ship_scrap - engine_lvl_cost[blue_engine_lvl]) > 0:
        blue_engine_lvl += 1
        blue_ship_scrap -= engine_lvl_cost[blue_engine_lvl]
        blueenginebutton.configure(text="Engine Level: " + str(blue_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[blue_engine_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_engine_lvl == 7:
            blueenginebutton.configure(state=DISABLED)
    else:
        print("NOPE")


blueenginebutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="blue", fg="black", text="Engine Level: " + str(blue_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[blue_engine_lvl + 1]), command=blueupgradeengine)
blueenginebutton.place(x=1400, y=oldy)

"""
END ENGINE
"""

"""
WEP
"""

def redupgradewep():  #MAY WANT TO PRINT COST OF NEXT UPGRADE
    global red_wep_lvl
    global red_ship_scrap
    if red_wep_lvl == 6:
        red_wep_lvl += 1
        red_ship_scrap -= wep_lvl_cost[red_wep_lvl]
        redwepbutton.configure(text="Wep Level: " + str(red_wep_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
    elif red_wep_lvl < 7 and (red_ship_scrap - wep_lvl_cost[red_wep_lvl]) > 0:
        red_wep_lvl += 1
        red_ship_scrap -= wep_lvl_cost[red_wep_lvl]
        redwepbutton.configure(text="Wep Level: " + str(red_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[red_wep_lvl + 1]))
        red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
        if red_wep_lvl == 7:
            redwepbutton.configure(state=DISABLED)
    else:
        print("NOPE")


redwepbutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="red", fg="black", text="Wep Level: " + str(red_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[blue_wep_lvl + 1]), command=redupgradewep)
redwepbutton.place(x=0, y=oldy)

def blueupgradewep():
    global blue_wep_lvl
    global blue_ship_scrap
    if blue_wep_lvl == 6:
        blue_wep_lvl += 1
        blue_ship_scrap -= wep_lvl_cost[blue_wep_lvl]
        bluewepbutton.configure(text="Wep Level: " + str(blue_wep_lvl) + " MAX LEVEL")
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
    elif blue_wep_lvl < 7 and (blue_ship_scrap - wep_lvl_cost[blue_wep_lvl]) > 0:
        blue_wep_lvl += 1
        blue_ship_scrap -= wep_lvl_cost[blue_wep_lvl]
        bluewepbutton.configure(text="Wep Level: " + str(blue_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[blue_wep_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_wep_lvl == 7:
            bluewepbutton.configure(state=DISABLED)
    else:
        print("NOPE")

bluewepbutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="blue", fg="black", text="wep Level: " + str(blue_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[blue_wep_lvl + 1]), command=blueupgradewep)
bluewepbutton.place(x=1400, y=oldy)

"""
END WEP
"""

"""

END SYSTEM UPGRADES

"""


def printallvalues(): #just a test thing
    print(str(red_shield_lvl))
    print(str(blue_shield_lvl))
    print(str(red_engine_lvl))
    print(str(blue_engine_lvl))
    print(str(red_wep_lvl))
    print(str(blue_wep_lvl))
    print(str(red_ship_scrap))
    print(str(blue_ship_scrap))

returnallvalues = Button(root, text="returnallupgradevalues", command=printallvalues)
returnallvalues.place(x=430, y=70)

root.mainloop()

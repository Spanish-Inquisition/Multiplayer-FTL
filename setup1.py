from tkinter import *
#Things to do: add buy more missile buttons.
import PIL
from PIL import Image, ImageTk

root = Tk()

red_ship_scrap = 800
blue_ship_scrap = 800
turn_max = 2

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

"""
red_power_lvl = 4
blue_power_lvl = 4
power_lvl_cost = [20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35]
"""

canvas = Canvas(root, height=900, width=1600, relief=RAISED, bg='black')
canvas.grid()

import os.path

directory = os.path.dirname(os.path.abspath(__file__))
start_filename = os.path.join(directory, './resources/screens/start.bmp')
redsetup_filename = os.path.join(directory, './resources/screens/redSetup.bmp')
bluesetup_filename = os.path.join(directory, './resources/screens/blueSetup.bmp')
redship_filename = os.path.join(directory, './resources/images/Federation.PNG')
blueship_filename = os.path.join(directory, './resources/images/Stealth.PNG')
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

redship_img = PIL.Image.open(redship_filename)
redship_img = redship_img.resize((500, 300))
redship_photo = PIL.ImageTk.PhotoImage(redship_img)

blueship_img = Image.open(blueship_filename)
blueship_img = blueship_img.resize((500, 300))
blueship_photo = ImageTk.PhotoImage(blueship_img)

oldy = -800 #moves buttons from offscreen to on screen. Negative values make them 'invisible'
scrap_newy = 16
shield_newy = 678
engine_newy = 748
wep_newy = 818
done_newy = 820
wep_row_1_newy = 670
wep_row_2_newy = 700
wep_row_3_newy = 730

redship_onscreen = Label(image=redship_photo)      #ASK ALEX HOW HE GOT HIS IMAGES TRANSPARENT BACKGROUNDS
redship_onscreen.place(x=100, y=oldy)
blueship_onscreen = Label(image=blueship_photo)
blueship_onscreen.place(x=900, y=oldy)

def changeimagefirst():
    redturn()
    button.place(x=540, y=670)
    red_scrap.place(y=scrap_newy)
    blue_scrap.place(y=scrap_newy)
    redship_onscreen.place(y=200)
    blueship_onscreen.place(y=200)
    red_done.place(y=done_newy)
    blue_done.place(y=done_newy)
    basic_laser_button.place(y=wep_row_1_newy)
    burst_laser_1_button.place(y=wep_row_1_newy)
    burst_laser_2_button.place(y=wep_row_1_newy)
    burst_laser_3_button.place(y=wep_row_1_newy)
    heavy_laser_1_button.place(y=wep_row_2_newy)
    heavy_laser_2_button.place(y=wep_row_2_newy)
    ion_button.place(y=wep_row_2_newy)
    ion_2_button.place(y=wep_row_2_newy)
    heavy_ion_button.place(y=wep_row_2_newy)
    leto_button.place(y=wep_row_3_newy)
    artemis_button.place(y=wep_row_3_newy)
    hermes_button.place(y=wep_row_3_newy)


def changeimageblue():
    blueturn()

def changeimagered():
    redturn()

button = Button(root, text="START", command=changeimagefirst, bd=8, font=("Fixedsys", 40), bg="black", fg="white")
button.place(x=680, y=700)

def redturn():
    global current_turn
    current_turn = "red"
    reset_buttons()
    check_missiles()
    check_weapons()
    background.configure(image=redsetup_photo)
    button.configure(command=changeimageblue, text="<Red End Turn>", state=DISABLED)
    button.place(x=540, y=670)
    #reverse all buttons
    #red
    redshieldbutton.place(x=10, y=shield_newy)
    redenginebutton.place(x=10, y=engine_newy)
    redwepbutton.place(x=10, y=wep_newy)
    red_done.configure(state=NORMAL)
    #blue
    blueshieldbutton.place(x=10, y=oldy)
    blueenginebutton.place(x=10, y=oldy)
    bluewepbutton.place(x=10, y=oldy)
    blue_done.configure(state=DISABLED)

def blueturn():
    global current_turn
    current_turn = "blue"
    reset_buttons()
    check_missiles()
    check_weapons()
    background.configure(image=bluesetup_photo)
    button.configure(command=changeimagered, text="<Blue End Turn>", state=DISABLED)
    button.place(x=535)
    #reverse all buttons
    #red
    redshieldbutton.place(x=10, y=oldy)
    redenginebutton.place(x=10, y=oldy)
    redwepbutton.place(x=10, y=oldy)
    red_done.configure(state=DISABLED)
    #blue
    blueshieldbutton.place(x=10, y=shield_newy)
    blueenginebutton.place(x=10, y=engine_newy)
    bluewepbutton.place(x=10, y=wep_newy)
    blue_done.configure(state=NORMAL)


turn_count = 0
def overturn():
    global turn_count
    global turn_max
    if turn_count < turn_max:
        turn_count += 1
    else:
        button.configure(state=NORMAL)
        redshieldbutton.configure(state=DISABLED)
        redenginebutton.configure(state=DISABLED)
        redwepbutton.configure(state=DISABLED)
        blueshieldbutton.configure(state=DISABLED)
        blueenginebutton.configure(state=DISABLED)
        bluewepbutton.configure(state=DISABLED)
        basic_laser_button.configure(state=DISABLED)
        burst_laser_1_button.configure(state=DISABLED)
        burst_laser_2_button.configure(state=DISABLED)
        burst_laser_3_button.configure(state=DISABLED)
        heavy_laser_1_button.configure(state=DISABLED)
        heavy_laser_2_button.configure(state=DISABLED)
        ion_button.configure(state=DISABLED)
        ion_2_button.configure(state=DISABLED)
        heavy_ion_button.configure(state=DISABLED)
        leto_button.configure(state=DISABLED)
        artemis_button.configure(state=DISABLED)
        hermes_button.configure(state=DISABLED)
        turn_count = 0

redissuredone = 0
def redisdone():
    global turn_max
    global redissuredone
    turn_max = 888
    changeimageblue()
    red_done.configure(state=DISABLED, text="✔")
    redissuredone = 1
    if blueissuredone == 1:
        button.configure(state=DISABLED)
        gobutton.place(y=done_newy)
        blue_done.configure(state=DISABLED)
        red_done.configure(state=DISABLED)
        blueshieldbutton.place(x=10, y=oldy)
        blueenginebutton.place(x=10, y=oldy)
        bluewepbutton.place(x=10, y=oldy)

red_done = Button(root, text="Done?", command=redisdone, bg="red", fg="black")
red_done.place(x=600, y=oldy)
blueissuredone = 0
def blueisdone():
    global turn_max
    global blueissuredone
    global redissuredone
    blueissuredone = 1
    turn_max = 888
    changeimagered()
    blue_done.configure(state=DISABLED, text="✔")
    if redissuredone == 1:
        button.configure(state=DISABLED)
        gobutton.place(y=done_newy)
        red_done.configure(state=DISABLED)
        redshieldbutton.place(x=10, y=oldy)
        redenginebutton.place(x=10, y=oldy)
        redwepbutton.place(x=10, y=oldy)

blue_done = Button(root, text="Done?", command=blueisdone, bg="blue", fg="black")
blue_done.place(x=800, y=oldy)

def reset_buttons():
    redshieldbutton.configure(state=NORMAL)
    redenginebutton.configure(state=NORMAL)
    redwepbutton.configure(state=NORMAL)
    blueshieldbutton.configure(state=NORMAL)
    blueenginebutton.configure(state=NORMAL)
    bluewepbutton.configure(state=NORMAL)
    basic_laser_button.configure(state=NORMAL)
    burst_laser_1_button.configure(state=NORMAL)
    burst_laser_2_button.configure(state=NORMAL)
    burst_laser_3_button.configure(state=NORMAL)
    heavy_laser_1_button.configure(state=NORMAL)
    heavy_laser_2_button.configure(state=NORMAL)
    ion_button.configure(state=NORMAL)
    ion_2_button.configure(state=NORMAL)
    heavy_ion_button.configure(state=NORMAL)
    leto_button.configure(state=NORMAL)
    artemis_button.configure(state=NORMAL)
    hermes_button.configure(state=NORMAL)
    check_missiles()
    check_weapons()

gobutton = Button(root, text="GO!") #THIS BUTTON WILL EXECUTE THE COMMAND THAT DOES YOUR THING ALEX
gobutton.place(x=750, y=oldy)

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
    if (red_shield_lvl == 5) and (red_ship_scrap - shield_lvl_cost[red_shield_lvl+1]) >= 0:
        red_shield_lvl += 1
        red_ship_scrap -= shield_lvl_cost[red_shield_lvl]
        redshieldbutton.configure(text="Shield Level: " + str(red_shield_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
        overturn()
    elif (red_shield_lvl < 6) and (red_ship_scrap - shield_lvl_cost[red_shield_lvl+1]) >= 0:
        red_shield_lvl += 1
        red_ship_scrap -= shield_lvl_cost[red_shield_lvl]
        redshieldbutton.configure(text="Shield Level: " + str(red_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[red_shield_lvl + 1]))
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
        if red_shield_lvl == 6:
            redshieldbutton.configure(state=DISABLED)
        overturn()
    else:
        print("NOPE")

redshieldbutton = Button(root, width=32, text="Shield Level: " + str(red_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[red_shield_lvl + 1]), command=redupgradeshield, bd=2, font=("Fixedsys", 18), bg="red", fg="black")
redshieldbutton.place(x=10, y=oldy)

def blueupgradeshield():
    global blue_shield_lvl
    global blue_ship_scrap
    if blue_shield_lvl == 5 and (blue_ship_scrap - shield_lvl_cost[blue_shield_lvl+1]) >= 0:
        blue_shield_lvl += 1
        blue_ship_scrap -= shield_lvl_cost[blue_shield_lvl]
        blueshieldbutton.configure(text="Shield Level: " + str(blue_shield_lvl) + " MAX LEVEL")
        blue_scrap.configure(text=" BLUE SCRAP: " + str(blue_ship_scrap))
        overturn()
    elif blue_shield_lvl < 6 and (blue_ship_scrap - shield_lvl_cost[blue_shield_lvl+1]) >= 0:
        blue_shield_lvl += 1
        blue_ship_scrap -= shield_lvl_cost[blue_shield_lvl]
        blueshieldbutton.configure(text="Shield Level: " + str(blue_shield_lvl) + "   Next Cost: " + str(shield_lvl_cost[blue_shield_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_shield_lvl == 6:
            blueshieldbutton.configure(state=DISABLED)
        overturn()
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
    if red_engine_lvl == 6 and (red_ship_scrap - engine_lvl_cost[red_engine_lvl+1]) >= 0:
        red_engine_lvl += 1
        red_ship_scrap -= engine_lvl_cost[red_engine_lvl]
        redenginebutton.configure(text="Engine Level: " + str(red_engine_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
        overturn()
    elif red_engine_lvl < 7 and (red_ship_scrap - engine_lvl_cost[red_engine_lvl+1]) >= 0:
        red_engine_lvl += 1
        red_ship_scrap -= engine_lvl_cost[red_engine_lvl]
        redenginebutton.configure(text="Engine Level: " + str(red_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[red_engine_lvl + 1]))
        red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
        if red_engine_lvl == 7:
            redenginebutton.configure(state=DISABLED)
        overturn()
    else:
        print("NOPE")

redenginebutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="red", fg="black", text="Engine Level: " + str(red_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[blue_engine_lvl + 1]), command=redupgradeengine)
redenginebutton.place(x=0, y=oldy)

def blueupgradeengine():
    global blue_engine_lvl
    global blue_ship_scrap
    if blue_engine_lvl == 6 and (blue_ship_scrap - engine_lvl_cost[blue_engine_lvl + 1]) >= 0:
        blue_engine_lvl += 1
        blue_ship_scrap -= engine_lvl_cost[blue_engine_lvl]
        blueenginebutton.configure(text="Engine Level: " + str(blue_engine_lvl) + " MAX LEVEL")
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        overturn()
    elif blue_engine_lvl < 7 and (blue_ship_scrap - engine_lvl_cost[blue_engine_lvl + 1]) >= 0:
        blue_engine_lvl += 1
        blue_ship_scrap -= engine_lvl_cost[blue_engine_lvl]
        blueenginebutton.configure(text="Engine Level: " + str(blue_engine_lvl) + "   Next Cost: " + str(engine_lvl_cost[blue_engine_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_engine_lvl == 7:
            blueenginebutton.configure(state=DISABLED)
        overturn()
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
    if red_wep_lvl == 6 and (red_ship_scrap - wep_lvl_cost[red_wep_lvl + 1]) >= 0:
        red_wep_lvl += 1
        red_ship_scrap -= wep_lvl_cost[red_wep_lvl]
        redwepbutton.configure(text="Wep Level: " + str(red_wep_lvl) + " MAX LEVEL")
        red_scrap.configure(text=" RED SCRAP: " + str(red_ship_scrap))
        overturn()
    elif red_wep_lvl < 7 and (red_ship_scrap - wep_lvl_cost[red_wep_lvl + 1]) >= 0:
        red_wep_lvl += 1
        red_ship_scrap -= wep_lvl_cost[red_wep_lvl]
        redwepbutton.configure(text="Wep Level: " + str(red_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[red_wep_lvl + 1]))
        red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
        if red_wep_lvl == 7:
            redwepbutton.configure(state=DISABLED)
        overturn()
    else:
        print("NOPE")

redwepbutton = Button(root, width=32, bd=2, font=("Fixedsys", 18), bg="red", fg="black", text="Wep Level: " + str(red_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[blue_wep_lvl + 1]), command=redupgradewep)
redwepbutton.place(x=0, y=oldy)

def blueupgradewep():
    global blue_wep_lvl
    global blue_ship_scrap
    if blue_wep_lvl == 6 and (blue_ship_scrap - wep_lvl_cost[blue_wep_lvl + 1]) >= 0:
        blue_wep_lvl += 1
        blue_ship_scrap -= wep_lvl_cost[blue_wep_lvl]
        bluewepbutton.configure(text="Wep Level: " + str(blue_wep_lvl) + " MAX LEVEL")
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        overturn()
    elif blue_wep_lvl < 7 and (blue_ship_scrap - wep_lvl_cost[blue_wep_lvl + 1]) >= 0:
        blue_wep_lvl += 1
        blue_ship_scrap -= wep_lvl_cost[blue_wep_lvl]
        bluewepbutton.configure(text="Wep Level: " + str(blue_wep_lvl) + "   Next Cost: " + str(wep_lvl_cost[blue_wep_lvl + 1]))
        blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
        if blue_wep_lvl == 7:
            bluewepbutton.configure(state=DISABLED)
        overturn()
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

"""

WEAPON STUFF

"""
basic_laser_cost = 20
burst_laser_1_cost = 50
burst_laser_2_cost = 80
burst_laser_3_cost = 95

heavy_laser_1_cost = 55
heavy_laser_2_cost = 65
# lasers

leto_cost = 20
artemis_cost = 38
hermes_cost = 45
#missiles

ion_cost = 30
heavy_ion_cost = 45
ion_2_cost = 70
#ion

red_weapon_count = 0
blue_weapon_count = 0
red_ship_weapons = []
blue_ship_weapons = []

red_ship_missile_weps = 0
blue_ship_missile_weps = 0

red_ship_missile_count = 0
blue_ship_missile_count = 0

max_missile_weps = 1
missile_increase = 5

def basic_laser_buy():
    global basic_laser_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - basic_laser_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= basic_laser_cost
            red_ship_weapons.append("basic_laser")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - basic_laser_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= basic_laser_cost
            blue_ship_weapons.append("basic_laser")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

basic_laser_button = Button(root, text="Basic Laser: Cost " + str(basic_laser_cost), command=basic_laser_buy)
basic_laser_button.place(x=1050, y=oldy)

def burst_laser_1_buy():
    global burst_laser_1_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - burst_laser_1_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= burst_laser_1_cost
            red_ship_weapons.append("burst_laser_1")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - burst_laser_1_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= burst_laser_1_cost
            blue_ship_weapons.append("burst_laser_1")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

burst_laser_1_button = Button(root, text="Burst Laser 1: Cost " + str(burst_laser_1_cost), command=burst_laser_1_buy)
burst_laser_1_button.place(x=1170, y=oldy)

def burst_laser_2_buy():
    global burst_laser_2_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - burst_laser_2_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= burst_laser_2_cost
            red_ship_weapons.append("burst_laser_2")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - burst_laser_2_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= burst_laser_2_cost
            blue_ship_weapons.append("burst_laser_2")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

burst_laser_2_button = Button(root, text="Burst Laser 2: Cost " + str(burst_laser_2_cost), command=burst_laser_2_buy)
burst_laser_2_button.place(x=1300, y=oldy)

def burst_laser_3_buy():
    global burst_laser_3_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - burst_laser_3_cost) > 0:
            red_weapon_count += 1
            red_ship_scrap -= burst_laser_3_cost
            red_ship_weapons.append("burst_laser_3")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - burst_laser_3_cost) > 0:
            blue_weapon_count += 1
            blue_ship_scrap -= burst_laser_3_cost
            blue_ship_weapons.append("burst_laser_3")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

burst_laser_3_button = Button(root, text="Burst Laser 3: Cost " + str(burst_laser_3_cost), command=burst_laser_3_buy)
burst_laser_3_button.place(x=1430, y=oldy)

def heavy_laser_1_buy():
    global heavy_laser_1_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - heavy_laser_1_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= heavy_laser_1_cost
            red_ship_weapons.append("heavy_laser_1")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - heavy_laser_1_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= heavy_laser_1_cost
            blue_ship_weapons.append("heavy_laser_1")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

heavy_laser_1_button = Button(root, text="Heavy Laser: Cost " + str(heavy_laser_1_cost), command=heavy_laser_1_buy)
heavy_laser_1_button.place(x=1050, y=oldy)

def heavy_laser_2_buy():
    global heavy_laser_2_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - heavy_laser_2_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= heavy_laser_2_cost
            red_ship_weapons.append("heavy_laser_2")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - heavy_laser_2_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= heavy_laser_2_cost
            blue_ship_weapons.append("heavy_laser_2")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

heavy_laser_2_button = Button(root, text="Heavy Laser 2: Cost " + str(heavy_laser_2_cost), command=heavy_laser_2_buy)
heavy_laser_2_button.place(x=1170, y=oldy)

def ion_buy():
    global ion_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - ion_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= ion_cost
            red_ship_weapons.append("ion")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - ion_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= ion_cost
            blue_ship_weapons.append("ion")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

ion_button = Button(root, text="Ion: Cost " + str(ion_cost), command=ion_buy)
ion_button.place(x=1300, y=oldy)

def heavy_ion_buy():
    global heavy_ion_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - heavy_ion_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= heavy_ion_cost
            red_ship_weapons.append("heavy_ion")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - heavy_ion_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= heavy_ion_cost
            blue_ship_weapons.append("heavy_ion")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

heavy_ion_button = Button(root, text="Heavy Ion: Cost " + str(heavy_ion_cost), command=heavy_ion_buy)
heavy_ion_button.place(x=1470, y=oldy)

def ion_2_buy():
    global ion_2_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - ion_2_cost) >= 0:
            red_weapon_count += 1
            red_ship_scrap -= ion_2_cost
            red_ship_weapons.append("ion_2")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - ion_2_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_scrap -= ion_2_cost
            blue_ship_weapons.append("ion_2")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

ion_2_button = Button(root, text="Ion 2: Cost " + str(ion_2_cost), command=ion_2_buy)
ion_2_button.place(x=1378, y=oldy)

def leto_buy():
    global leto_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    global red_ship_missile_weps
    global blue_ship_missile_weps
    global red_ship_missile_count
    global blue_ship_missile_count
    global missile_increase
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - leto_cost) >= 0:
            red_weapon_count += 1
            red_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            red_ship_scrap -= leto_cost
            red_ship_weapons.append("leto")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - leto_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            blue_ship_scrap -= leto_cost
            blue_ship_weapons.append("leto")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

leto_button = Button(root, text="Leto: Cost " + str(leto_cost), command=leto_buy)
leto_button.place(x=1050, y=oldy)

def artemis_buy():
    global artemis_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    global red_ship_missile_weps
    global blue_ship_missile_weps
    global red_ship_missile_count
    global blue_ship_missile_count
    global missile_increase
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - artemis_cost) >= 0:
            red_weapon_count += 1
            red_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            red_ship_scrap -= artemis_cost
            red_ship_weapons.append("artemis")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - artemis_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            blue_ship_scrap -= artemis_cost
            blue_ship_weapons.append("artemis")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

artemis_button = Button(root, text="Artemis: Cost " + str(artemis_cost), command=artemis_buy)
artemis_button.place(x=1170, y=oldy)

def hermes_buy():
    global hermes_cost
    global current_turn
    global red_weapon_count
    global blue_weapon_count
    global red_ship_weapons
    global blue_ship_weapons
    global red_ship_scrap
    global blue_ship_scrap
    global turn_count
    global turn_max
    global red_ship_missile_weps
    global blue_ship_missile_weps
    global red_ship_missile_count
    global blue_ship_missile_count
    global missile_increase
    if current_turn == "red":
        if red_weapon_count < 4 and (red_ship_scrap - hermes_cost) >= 0:
            red_weapon_count += 1
            red_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            red_ship_scrap -= hermes_cost
            red_ship_weapons.append("hermes")
            red_scrap.configure(text="RED SCRAP: " + str(red_ship_scrap))
            build_weps()
            overturn()
        else:
            print("Nope")
    elif current_turn == "blue":
        if blue_weapon_count < 4 and (blue_ship_scrap - hermes_cost) >= 0:
            blue_weapon_count += 1
            blue_ship_missile_weps += 1
            red_ship_missile_count += missile_increase
            blue_ship_scrap -= hermes_cost
            blue_ship_weapons.append("hermes")
            build_weps()
            blue_scrap.configure(text="BLUE SCRAP: " + str(blue_ship_scrap))
            overturn()
        else:
            print("Nope")

hermes_button = Button(root, text="Hermes: Cost " + str(hermes_cost), command=hermes_buy)
hermes_button.place(x=1300, y=oldy)

def check_missiles():
    if current_turn == "red":
        if red_ship_missile_weps >= max_missile_weps:
            leto_button.configure(state=DISABLED)
            artemis_button.configure(state=DISABLED)
            hermes_button.configure(state=DISABLED)
    if current_turn == "blue":
        if blue_ship_missile_weps >= max_missile_weps:
            leto_button.configure(state=DISABLED)
            artemis_button.configure(state=DISABLED)
            hermes_button.configure(state=DISABLED)

def check_weapons():
    if current_turn == "red":
        if red_weapon_count >= 4:
            basic_laser_button.configure(state=DISABLED)
            burst_laser_1_button.configure(state=DISABLED)
            burst_laser_2_button.configure(state=DISABLED)
            burst_laser_3_button.configure(state=DISABLED)
            heavy_laser_1_button.configure(state=DISABLED)
            heavy_laser_2_button.configure(state=DISABLED)
            ion_button.configure(state=DISABLED)
            ion_2_button.configure(state=DISABLED)
            heavy_ion_button.configure(state=DISABLED)
            leto_button.configure(state=DISABLED)
            artemis_button.configure(state=DISABLED)
            hermes_button.configure(state=DISABLED)
            #disable all weps
    if current_turn == "blue":
        if blue_weapon_count >= 4:
            basic_laser_button.configure(state=DISABLED)
            burst_laser_1_button.configure(state=DISABLED)
            burst_laser_2_button.configure(state=DISABLED)
            burst_laser_3_button.configure(state=DISABLED)
            heavy_laser_1_button.configure(state=DISABLED)
            heavy_laser_2_button.configure(state=DISABLED)
            ion_button.configure(state=DISABLED)
            ion_2_button.configure(state=DISABLED)
            heavy_ion_button.configure(state=DISABLED)
            leto_button.configure(state=DISABLED)
            artemis_button.configure(state=DISABLED)
            hermes_button.configure(state=DISABLED)
            #disable all weps

weapony = 600
def build_weps():
    global red_ship_weapons
    global blue_ship_weapons
    if red_weapon_count == 1:
        RedWeapon1 = Label(root, text=red_ship_weapons[0], bd=6)
        RedWeapon1.place(x=100, y=weapony)
    if red_weapon_count == 2:
        RedWeapon2 = Label(root, text=red_ship_weapons[1], bd=6)
        RedWeapon2.place(x=200, y=weapony)
    if red_weapon_count == 3:
        RedWeapon3 = Label(root, text=red_ship_weapons[2], bd=6)
        RedWeapon3.place(x=300, y=weapony)
    if red_weapon_count == 4:
        RedWeapon4 = Label(root, text=red_ship_weapons[3], bd=6)
        RedWeapon4.place(x=400, y=weapony)
    if blue_weapon_count == 1:
        BlueWeapon1 = Label(root, text=blue_ship_weapons[0], bd=6)
        BlueWeapon1.place(x=900, y=weapony)
    if blue_weapon_count == 2:
        BlueWeapon2 = Label(root, text=blue_ship_weapons[1], bd=6)
        BlueWeapon2.place(x=1000, y=weapony)
    if blue_weapon_count == 3:
        BlueWeapon3 = Label(root, text=blue_ship_weapons[2], bd=6)
        BlueWeapon3.place(x=1100, y=weapony)
    if blue_weapon_count == 4:
        BlueWeapon4 = Label(root, text=blue_ship_weapons[3], bd=6)
        BlueWeapon4.place(x=1200, y=weapony)
    check_weapons()
    check_missiles()
"""

END WEAPON STUFF

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
    print(red_ship_weapons)
    print(blue_ship_weapons)

returnallvalues = Button(root, text="returnallupgradevalues", command=printallvalues)
returnallvalues.place(x=430, y=70)

root.mainloop()

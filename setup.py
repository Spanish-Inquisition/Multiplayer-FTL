from tkinter import *
root = Tk()

canvas = Canvas(root, height=1000, width=2000, relief=RAISED, bg='black')
currentImage = 0
import os.path

directory = os.path.dirname(os.path.abspath(__file__))
startimage = os.path.join(directory, './resources/screens/fight.bmp')
testimage = os.path.join(directory, './resources/screens/test.jpg')

import PIL.Image, PIL.ImageTk
if currentImage == 0:

backgroundimage = PIL.Image.open(startimage)  # create a PIL.Image from the jpg file
testimg = testimg.resize((2000, 1000))
tkimg2 = PIL.ImageTk.PhotoImage(testimg)
icon2 = canvas.create_image(1000, 500, image=tkimg2)



def changeImagetoStart():


b = Button(root, text="OK", command=changeImage)
b.place(x = 0, y = 0)

root.mainloop()
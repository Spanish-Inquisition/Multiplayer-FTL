from tkinter import *

root = Tk()
buttonToggle = True


def pressbutton_bindkeys(event):
    global buttonToggle
    event.widget.config(bg='blue')
    event.widget.focus_set()  # give keyboard focus to the label
    if buttonToggle:
        event.widget.bind('<Key>', edit)
    elif not buttonToggle == True:
        event.widget.unbind('<Key')
    buttonToggle = not buttonToggle


def edit(event):
    print(event.char)


example = Label(root, text='press button to bind keys')
example.pack()
example.bind('<Button-1>', pressbutton_bindkeys)
mainloop()

from data import globals, gui
from PIL import Image, ImageTk
import tkinter as tk

def changeMisc(filename: str) -> None:
    globals["misc"] = 'picts/miscs/' + filename + '.png'
    misc: Image = tk.PhotoImage(file=globals["misc"])
    gui["frame"]["canvas"].misc = misc
    gui["frame"]["canvas"].itemconfig(globals["misc_container"], image=misc)
    for element in gui["el"]["misc"]:
        if element == "scale":
            gui["el"]["misc"][element].set(100)
        elif element != "select":
            gui["el"]["misc"][element].set(0)
    globals["val"]["miscScale"] = 100
    globals["val"]["miscPosX"] = 0
    globals["val"]["miscPosY"] = 0

def moveMisc(axis, value) -> None:
    if globals["misc_container"] is None:
        return
    globals["val"][axis] = value
    gui["frame"]["canvas"].coords(globals["misc_container"], gui["frame"]["canvas"].winfo_width() * int(globals["val"]["miscPosX"]) / 100, gui["frame"]["canvas"].winfo_height() * int(globals["val"]["miscPosY"]) / 100)

def scaleMisc(axis, value) -> None:
    if globals["misc_container"] is None:
        return
    globals["val"]["miscScale"] = value
    image = Image.open(globals["misc"])
    image = image.resize((int(image.size[0] * int(globals["val"]["miscScale"]) / 100), int(image.size[1] * int(globals["val"]["miscScale"]) / 100)), Image.ANTIALIAS)
    image = image.rotate(int(globals["val"]["miscRotate"]), expand=True)
    globals["gcMisc"] = ImageTk.PhotoImage(image)
    gui["frame"]["canvas"].itemconfig(globals["misc_container"], image=globals["gcMisc"])

def rotateMisc(axis, value) -> None:
    if globals["misc_container"] is None:
        return
    globals["val"]["miscRotate"] = value
    image = Image.open(globals["misc"])
    image = image.resize((int(image.size[0] * int(globals["val"]["miscScale"]) / 100), int(image.size[1] * int(globals["val"]["miscScale"]) / 100)), Image.ANTIALIAS)
    image = image.rotate(int(globals["val"]["miscRotate"]), expand=True)
    globals["gcMisc"] = ImageTk.PhotoImage(image)
    gui["frame"]["canvas"].itemconfig(globals["misc_container"], image=globals["gcMisc"])
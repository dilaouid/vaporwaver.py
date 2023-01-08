from data import globals, gui
from PIL import Image, ImageTk

def moveCharacter(axis, value):
    if globals["character"] is None:
        return
    globals["val"][axis] = value
    # change the position of the character according to % of the canvas
    gui["frame"]["canvas"].coords(globals["character"], gui["frame"]["canvas"].winfo_width() * int(globals["val"]["characterXpos"]) / 100, gui["frame"]["canvas"].winfo_height() * int(globals["val"]["characterYpos"]) / 100)

def scaleCharacter(axis, value):
    if globals["character"] is None:
        return
    globals["val"]["characterScale"] = value
    image = Image.open(globals["characterPath"])
    image = image.resize((int(image.size[0] * int(globals["val"]["characterScale"]) / 100), int(image.size[1] * int(globals["val"]["characterScale"]) / 100)), Image.ANTIALIAS)
    globals["previewChar"] = ImageTk.PhotoImage(image)
    gui["frame"]["canvas"].itemconfig(globals["character"], image=globals["previewChar"])

def scaleMisc(axis, value):
    if globals["misc"] is None:
        return
    globals["val"]["miscScale"] = value
    image = Image.open(globals["miscPath"])
    image = image.resize((int(image.size[0] * int(globals["val"]["miscScale"]) / 100), int(image.size[1] * int(globals["val"]["miscScale"]) / 100)), Image.ANTIALIAS)
    gui["frame"]["canvas"].itemconfig(globals["misc"], image=ImageTk.PhotoImage(image))
from tkinter import *
import math
import random
import time

import menu
import jimmies

def init(data):
    # data.menuData is defined in menu.py
    # data.countingData is defined in jimmies.py
    data.scenes = ["menu", "n choose k", "counting in two ways"]
    data.state = "menu"

    # optionRoot = Tk()
    # var = StringVar(optionRoot)
    # var.set(data.scenes[0])
    #
    # w = OptionMenu(optionRoot, var, *data.scenes)
    # w.pack()

def changeState(data, scene):
    data.state = scene

def checkCollision(event, box):
    (x0, y0, x1, y1) = box
    return event.x > x0 and event.x < x1 and event.y < y1 and event.y > y0

def mousePressed(event, data):
    if checkCollision(event, data.menuData.buttonBox):
        changeState(data, data.menuData.sceneChoice)
    elif checkCollision(event, data.menuData.upBox):
        menu.changeListOption(data.menuData, "up")
    elif checkCollision(event, data.menuData.downBox):
        menu.changeListOption(data.menuData, "down")

def keyPressed(event, data):
    if data.state == "counting in two ways":
        print("cock")
        jimmies.keyPressed(event, data.countingData)

def timerFired(data):
    if data.state == "counting in two ways":
        jimmies.timerFired(data.countingData)

def parseInput(data):
    pass

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)

    if data.state == "menu":
        menu.drawMenu(canvas, data.menuData)
    elif data.state == "n choose k":
        return
    elif data.state == "counting in two ways":
        jimmies.redrawAllPostFix(canvas, data.countingData)


def drawFrameRate(canvas, data):
    frameRate = len(data.t)
    canvas.create_text(data.width-10, 0, anchor=NE, text="fps:"+str(frameRate))

# run function adapted from 15-112 course website
def run(width=900, height=900):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        # update times
        t0 = time.time()
        data.timerDelay = (t0 - data.lastTime) * 1000
        data.t.append(data.timerDelay)
        while (sum(data.t) > 1000):
            data.t.pop(0)
        data.lastTime = t0
        
        timerFired(data)
        redrawAllWrapper(canvas, data)
        
        # call timerFired again
        canvas.after(0, timerFiredWrapper, canvas, data)
    # create the root and the canvas
    root = Tk()
    # root.overrideredirect(True)
    # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
    #                                   root.winfo_screenheight()))
    # canvas = Canvas(root, width=root.winfo_screenwidth(),
    #                height=root.winfo_screenheight())
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    # data.width = root.winfo_screenwidth()
    # data.height = root.winfo_screenheight()
    data.width = width
    data.height = height
    data.lastTime = time.time()
    data.timerDelay = 0
    data.t = []
    init(data)

    # set up menu
    data.menuData = data
    menu.initMenu(data.menuData)
    # set up counting two ways stuff
    data.countingData = data
    jimmies.init(data.countingData)

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()
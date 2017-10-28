from tkinter import *
import math
import random
import time

import menu
import jimmies
import nchoosekScene
import subcommittee

def init(data):
    # data.menuData is defined in menu.py
    # data.countingData is defined in jimmies.py
    # data.nchoosekdata defined in nchoosekScene.py
    data.scenes = ["menu", "n choose k", "counting in two ways", "subcommittee"]
    data.state = "menu"
    data.backBox = (data.width - data.width // 9,
                    data.height // 20,
                    (data.width - data.width // 9) + data.width // 10,
                    data.height // 20 + data.width // 10)

def changeState(data, scene):
    if scene == "menu":
        print("changed to menu")
        data.menuData.buttonPressed = False
        print(data.menuData.buttonPressed)

    else: data.menuData.buttonPressed = True
    data.state = scene
    if scene == "n choose k":
        data.nchoosekData = data
        nchoosekScene.init(data.nchoosekData)
    elif scene == "counting in two ways":
        data.countingData = data
        jimmies.init(data.countingData)
    elif scene == "subcommittee":
        data.subcommitteeData = data
        subcommittee.init(data.subcommitteeData)

def checkCollision(event, box):
    (x0, y0, x1, y1) = box
    return event.x > x0 and event.x < x1 and event.y < y1 and event.y > y0

def mousePressed(event, data):
    if data.state == "menu":
        if not data.menuData.buttonPressed:
            if checkCollision(event, data.menuData.buttonBox):
                changeState(data, data.menuData.sceneChoice)
            elif checkCollision(event, data.menuData.upBox):
                menu.changeListOption(data.menuData, "up")
            elif checkCollision(event, data.menuData.downBox):
                menu.changeListOption(data.menuData, "down")
    else:
        if checkCollision(event, data.backBox):
            changeState(data, "menu")

def mouseMoved(event, data):
    if data.state == "subcommittee":
        subcommittee.mouseMoved(event, data.subcommitteeData)

def keyPressed(event, data):
    if data.state == "counting in two ways":
        jimmies.keyPressed(event, data.countingData)
    if data.state == "n choose k":
        nchoosekScene.keyDown(event, data.nchoosekData)
    if data.state == "subcommittee":
        subcommittee.keyDown(event, data.subcommitteeData)

def timerFired(data):
    if data.state == "counting in two ways":
        jimmies.timerFired(data.countingData)
    elif data.state == "n choose k":
        data.nchoosekData.timerDelay = data.timerDelay
        nchoosekScene.timerFired(data.nchoosekData)
    elif data.state == "subcommittee":
        data.subcommitteeData.timerDelay = data.timerDelay
        subcommittee.timerFired(data.subcommitteeData)

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)
    if not data.state == "menu": drawBackButton(canvas, data)

    if data.state == "menu":
        menu.drawMenu(canvas, data.menuData)
    elif data.state == "n choose k":
        nchoosekScene.redrawAll(canvas, data.nchoosekData)
    elif data.state == "counting in two ways":
        jimmies.redrawAllPostFix(canvas, data.countingData)
    elif data.state == "subcommittee":
        subcommittee.redrawAll(canvas, data.subcommitteeData)

def drawBackButton(canvas, data):
    (x0, y0, x1, y1) = data.backBox
    canvas.create_rectangle(x0, y0, x1, y1)

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

    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event, data)

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
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))
    canvas = Canvas(root, width=root.winfo_screenwidth(),
                    height=root.winfo_screenheight())
    #canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = root.winfo_screenwidth()
    data.height = root.winfo_screenheight()
    #data.width = width
    #data.height = height
    data.lastTime = time.time()
    data.timerDelay = 0
    data.t = []
    init(data)

    # set up menu
    data.menuData = data
    menu.initMenu(data.menuData)

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()

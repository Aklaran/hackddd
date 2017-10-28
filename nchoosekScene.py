from tkinter import *

from nchoosekvisualization import nChooseKVisualization as vis

def init(data):
    data.cursor = 0
    data.inputNames = ["n", "k"]
    data.inputs = [8,3]
    updateNM(data)

def inputRestrictions(data):
    if (data.inputs[0] < 0):
        data.inputs[0] = 0
    data.inputs[1] = data.inputs[1] % (data.inputs[0] + 1)

def updateNM(data):
    data.visuals = [None] # * ((data.inputs[0] - data.inputs[1] + 2) * 2 - 1)
    bounds = (50, 200, 200, 200)
    data.visuals[-1] = vis(data.inputs[0], data.inputs[1], bounds)

def timerFired(data):
    for v in data.visuals:
        #b = v.bounds
        #if inBounds(data.mouse, b):
        v.update(data.timerDelay / 500)

def keyDown(event, data):
    print("key down")
    if event.keysym == "Left":
        data.cursor = (data.cursor - 1) % len(data.inputs)
    elif event.keysym == "Right":
        data.cursor = (data.cursor + 1) % len(data.inputs)
    elif event.keysym == "Up":
        data.inputs[data.cursor] += 1
        inputRestrictions(data)
        updateNM(data)
    elif event.keysym == "Down":
        data.inputs[data.cursor] -= 1
        inputRestrictions(data)
        updateNM(data)

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)
    for v in data.visuals:
        b = v.bounds
        canvas.create_rectangle(b[0], b[1], b[0] + b[2], b[1] + b[3])
        #if inBounds(data.mouse, b):
        if True:
            v.draw(canvas)
        else:
            text = ("Chooseing " + str(v.k) + " people from a group of " +
                    str(v.n) + " people")
            canvas.create_text(b[0], b[1], text=text, anchor="nw", width=b[2],
                               font="120")
    drawInputUI(canvas, data)

def drawInputUI(canvas, data):
    for i in range(len(data.inputs)):
        cX = 100 + i * 150
        cY = 50
        canvas.create_text(cX, cY, text=data.inputNames[i], font="40")
        cY = 100
        if (data.cursor == i):
            r = 20
            canvas.create_rectangle(cX-r, cY-r, cX+r, cY+r, fill="yellow")
        canvas.create_text(cX, cY, text=str(data.inputs[i]), font="40")

def drawFrameRate(canvas, data):
    frameRate = len(data.t)
    canvas.create_text(data.width-10, 0, anchor=NE, text="fps:"+str(frameRate))
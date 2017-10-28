# Jianming Wang aka Yonner Ming

from tkinter import *
import math
import random
import time

from nchoosekvisualization import nChooseKVisualization as vis

# first level functions
def init(data):
    data.cursor = 0
    data.inputNames = ["Number of People", "Size of Subcommittee"]
    data.inputs = [8, 3]
    data.mouse = [0, 0]
    updateNM(data)

def mousePressed(event, data):
    pass

def keyDown(event, data):
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

def inputRestrictions(data):
    if (data.inputs[0] < 0):
        data.inputs[0] = 0
    data.inputs[1] = data.inputs[1] % (data.inputs[0] + 1)

def updateNM(data):
    data.visuals = [None] * ((data.inputs[0] - data.inputs[1] + 2) * 2 - 1)
    r = (data.width - 260) // 440
    for i in range(0, data.inputs[0] - data.inputs[1] + 1):
        x = i % r
        y = i // r
        bounds = (300 + x * 440, 200 + y * 220, 200, 200)
        data.visuals[2 * i] = vis(data.inputs[0], data.inputs[1] + i, bounds)
        bounds = (300 + x * 440 + 200, 200 + y * 220, 200, 200)
        data.visuals[2 * i + 1] = vis(data.inputs[1] + i, data.inputs[1], bounds)
    bounds = (50, 200, 200, 200)
    data.visuals[-1] = vis(data.inputs[0], data.inputs[1], bounds)

def keyUp(event, data):
    pass

def mouseMoved(event, data):
    data.mouse = [event.x, event.y]

def inBounds(mouse, bounds):
    if (mouse[0] < bounds[0] or mouse[1] < bounds[1]):
        return False
    if (mouse[0] > bounds[0] + bounds[2] or
        mouse[1] > bounds[1] + bounds[3]):
        return False
    return True

def timerFired(data):
    for v in data.visuals:
        b = v.bounds
        if inBounds(data.mouse, b):
            v.update(data.timerDelay / 500)

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)
    for v in data.visuals:
        b = v.bounds
        canvas.create_rectangle(b[0], b[1], b[0] + b[2], b[1] + b[3])
        if inBounds(data.mouse, b):
            v.draw(canvas)
        else:
            text = ("Chooseing " + str(v.k) + " people from a group of " +
                    str(v.n) + " people")
            canvas.create_text(b[0], b[1], text=text, anchor="nw", width=b[2],
                               font = "120")
    drawPlusSigns(canvas, data)
    drawInputUI(canvas, data)

def drawPlusSigns(canvas, data):
    # first draw the equal sign
    cY = 300
    cX = (300 + 250) / 2
    canvas.create_text(cX, cY, text="=", font="40")
    # now draw a plus sign after every other box
    r = (data.width - 260) // 440
    for i in range(0, data.inputs[0] - data.inputs[1]):
        x = i % r
        y = i // r
        bounds = (300 + x * 440 + 200, 200 + y * 220, 200, 200)
        cX = 300 + x * 440 + 200 + 200 + 40 / 2
        cY = 200 + y * 220 + 200 / 2
        canvas.create_text(cX, cY, text="+", font="40")

def drawInputUI(canvas, data):
    for i in range(len(data.inputs)):
        cX = 300 + i * 200
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

    def keyDownWrapper(event, canvas, data):
        keyDown(event, data)

    def keyUpWrapper(event, canvas, data):
        keyUp(event, data)

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
    canvas.pack()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = root.winfo_screenwidth()
    data.height = root.winfo_screenheight()
    data.lastTime = time.time()
    data.timerDelay = 0
    data.t = []
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyDownWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyUpWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

if __name__ == "__main__":
    run()

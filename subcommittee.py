# Jianming Wang aka Yonner Ming

from tkinter import *
import math
import random
import time

from nchoosekvisualization import nChooseKVisualization as vis

# first level functions
def init(data):
    data.cursor = 0
    data.n = 8
    data.m = 3
    data.mouse = [0, 0]
    updateNM(data)

def mousePressed(event, data):
    pass

def keyDown(event, data):
    if event.keysym == "Left":
        data.cursor = (data.cursor - 1) % 2
    elif event.keysym == "Right":
        data.cursor = (data.cursor + 1) % 2
    elif event.keysym == "Up":
        if (data.cursor == 0):
            data.n += 1
        elif (data.cursor == 1):
            data.m = (data.m + 1) % data.n
        updateNM(data)
    elif event.keysym == "Down":
        if (data.cursor == 0):
            if data.n > 0:
                data.n -= 1
                if data.m > data.n:
                    data.m = data.n
        elif (data.cursor == 1):
            data.m = (data.m - 1) % data.n
        updateNM(data)

def updateNM(data):
    data.visuals = [None] * ((data.n - data.m + 2) * 2 - 1)
    r = (data.width - 260) // 440
    for i in range(0, data.n - data.m + 1):
        x = i % r
        y = i // r
        bounds = (300 + x * 440, 200 + y * 220, 200, 200)
        data.visuals[2 * i] = vis(data.n, data.m + i, bounds)
        bounds = (300 + x * 440 + 200, 200 + y * 220, 200, 200)
        data.visuals[2 * i + 1] = vis(data.m + i, data.m, bounds)
    bounds = (50, 200, 200, 200)
    data.visuals[-1] = vis(data.n, data.m, bounds)

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
    canvas.create_text(100, 50, text="Total people", font="40")
    canvas.create_text(250, 50, text="Subcommittee Size", font="40")

    if (data.cursor == 0):
        cX = 100
        cY = 100
    elif (data.cursor == 1):
        cX = 250
        cY = 100
    r = 20
    canvas.create_rectangle(cX-r, cY-r, cX+r, cY+r, fill="yellow")

    canvas.create_text(100, 100, text=str(data.n), font="40")
    canvas.create_text(250, 100, text=str(data.m), font="40")

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

run()

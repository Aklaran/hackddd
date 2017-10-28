# Jianming Wang aka Yonner Ming

from tkinter import *
import math
import random
import time

from nchoosekvisualization import nChooseKVisualization

# first level functions
def init(data):
    data.n = 6
    data.mouse = [0, 0]
    data.visuals = [None] * (data.n + 1)
    data.bounds = [None] * (data.n + 1)
    for i in range(0, data.n+1):
        bounds = (data.width * 0.05 + data.width*0.9/(data.n + 1)*i,
                  data.height * 0.05,
                  data.width * 0.8 / (data.n + 1),
                  data.width * 0.8 / (data.n + 1))
        data.bounds[i] = bounds
        data.visuals[i] = nChooseKVisualization(data.n, i, bounds)

def mousePressed(event, data):
    pass

def keyDown(event, data):
    pass

def keyUp(event, data):
    pass

def mouseMoved(event, data):
    data.mouse = [event.x, event.y]

def timerFired(data):
    for i in range(0, data.n+1):
        if (inBounds(data.mouse, data.bounds[i])):
            data.visuals[i].update(data.timerDelay / 500)

def inBounds(mouse, bounds):
    if (mouse[0] < bounds[0] or mouse[1] < bounds[1]):
        return False
    if (mouse[0] > bounds[0] + bounds[2] or
        mouse[1] > bounds[1] + bounds[3]):
        return False
    return True

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)
    for b in data.bounds:
        canvas.create_rectangle(b[0], b[1], b[0] + b[2], b[1] + b[3])
    for i in range(0, data.n+1):
        if (inBounds(data.mouse, data.bounds[i])):
            data.visuals[i].draw(canvas)

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

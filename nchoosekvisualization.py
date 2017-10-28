from tkinter import *
import random
import math
import time

class nChooseKVisualization():
    def __init__(self, n, k, bounds):
        self.n = n
        self.k = k
        self.bounds = bounds;
        self.chosen = -1
        self.moving = None
        self.formula = ""
        self.time = 0
        self.startingPositions()
        self.sorted = False
        self.L = []

    def startingPositions(self):
        self.dots = [ [1, i+1] for i in range(self.n) ]
        self.endingPositions = [ [2, i+1] for i in range(self.k) ]

    def update(self, deltaT):
        if (deltaT <= 0):
            return
        newTime = self.time + deltaT
        if (self.chosen < self.k):
            self.roundOneMoves(newTime)
        elif (not self.sorted):
            if (len(self.L) == 0):
                # go through and create the actual list of chosen dots
                self.L = [0] * self.k;
                for i in range(self.n):
                    if (self.dots[i][0] == 2):
                        self.L[self.dots[i][1] - 1] = i
                self.moving = None
                for i in range(self.k):
                    self.formula = self.formula + "/" + str(self.k - i)
            self.sorting(newTime)
        self.time = newTime

    def roundOneMoves(self, newTime):
        if (self.chosen < self.k):
            if (self.time == 0 or
                (math.floor(newTime) - math.floor(self.time) == 1)):
                if (self.moving != None):
                    #finish the move
                    #print(self.chosen)
                    self.dots[self.moving] = self.endingPositions[self.chosen][:]
                    if (self.formula == ""):
                        self.formula = self.formula + str(self.n - self.chosen)
                    else:
                        self.formula = self.formula + "(" + str(self.n - self.chosen) + ")"
                #choose the next one to move
                canBeMoved = 0
                for i in range(self.n):
                    if (self.dots[i][0] == 1 and self.dots[i][1] == i+1):
                        canBeMoved += 1
                if canBeMoved > 0:
                    #choose which dot to move next
                    r = random.randint(0, canBeMoved - 1)
                    self.moving = -1
                    while (r >= 0):
                        self.moving += 1;
                        if (self.dots[self.moving][0] == 1 and
                            self.dots[self.moving][1] == self.moving + 1):
                            r -= 1
                    self.chosen += 1
            else:
                pass
        if (self.chosen < self.k):
            #now move the dot to the correct place
            initialPosition = [1, self.moving + 1]
            finalPosition = self.endingPositions[self.chosen]
            t = newTime - math.floor(newTime)
            self.dots[self.moving][0] = (t * finalPosition[0] +
                                         (1 - t) * initialPosition[0])
            self.dots[self.moving][1] = (t * finalPosition[1] +
                                         (1 - t) * initialPosition[1])

    def sorting(self, newTime):
        self.checkOrder()
        m = 1.0;
        if (not self.sorted):
            if (math.floor(newTime * m) - math.floor(self.time * m) >= 1):
                if (self.moving != None):
                    pos1 = self.L.index(self.moving[0])
                    pos2 = self.L.index(self.moving[1])
                    self.dots[self.moving[0]] = [2, pos2 + 1]
                    self.dots[self.moving[1]] = [2, pos1 + 1]
                    self.L[pos1] = self.moving[1]
                    self.L[pos2] = self.moving[0]
            self.checkOrder()
            if (not self.sorted):
                # find the first place where things are out of order
                i = 0
                while self.L[i] < self.L[i+1]:
                    i += 1
                self.moving = [self.L[i], self.L[i+1]]
            else:
                return
            # update positions
            pos1 = self.L.index(self.moving[0])
            pos2 = self.L.index(self.moving[1])
            cX = (pos1 + pos2) / 2 + 1
            cY = 2
            radius = (pos1 - pos2) / 2
            yScale = 1.0 / (self.n + 1.0) * self.bounds[2] / self.bounds[3] * 3
            t = newTime * m - math.floor(newTime * m)
            self.dots[self.moving[0]] = [cY + radius*yScale*math.sin(math.pi * (1 - t)),
                                         cX + radius*math.cos(math.pi * (1 - t))]
            self.dots[self.moving[1]] = [cY + radius*yScale*math.sin( - t * math.pi),
                                         cX + radius*math.cos( - t * math.pi)]
            

    def checkOrder(self):
        # check for order
        self.sorted = True
        for i in range(self.k - 1):
            if (self.L[i] > self.L[i+1]):
                self.sorted = False

    def draw(self, canvas):
        (x, y, w, h) = self.bounds
        radius = min( w / (self.n + 1) / 2, h / 9)
        radius = radius * 0.8;
        for d in self.dots:
            cX = x + d[1] / (self.n + 1.0) * w
            cY = y + d[0] / 4 * h
            canvas.create_oval(cX - radius, cY - radius, cX + radius,
                               cY + radius, fill = "orange")
            canvas.create_text(cX, cY, text=str(self.dots.index(d) + 1))
        cX = w * 0.05
        cY = 3 / 4 * h
        canvas.create_text(cX, cY, text=self.formula, anchor="nw",
                           font="30")

## TESTING

# first level functions
def init(data):
    bounds = (0, 0, 300, 300)
    data.visualization = nChooseKVisualization(8, 5, bounds)

def mousePressed(event, data):
    pass

def keyDown(event, data):
    pass

def keyUp(event, data):
    pass

def timerFired(data):
    data.visualization.update(data.timerDelay / 500)

def parseInput(data):
    pass

def redrawAll(canvas, data):
    drawFrameRate(canvas, data)
    data.visualization.draw(canvas)

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
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()
    

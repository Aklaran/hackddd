from tkinter import *
import random

class nChooseKVisualization():
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.left = n;
        self.chosen = 0;
        self.moving = None;
        self.formula = "";
        self.time = 0;
        startingPositions(self)

    def startingPositions(self):
        self.dots = [ [1, i+1] for i in range(self.n) ]
        self.endingPositions = [ [2, i+1] for i in range(self.k) ]

    def update(self, deltaT):
        newTime = self.time + deltaT
        if (self.time < self.k):
            if (self.time == 0 or (int) newTime - (int) self.Time == 1):
                if (self.moving != None):
                    #finish the move
                    self.dots[self.moving] = self.endingPosition[self.chosen][:]
                #choose the next one to move
                canBeMoved = 0
                for i in range(n):
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
                    self.chozen += 1
            else:
                pass
            #now move the dot to the correct place
            initialPostion = [1, self.moving + 1]
            finalPosition = self.endingPositions[self.chosen]
            t = newTime - (int) newTime
            
        pass

    def draw(self, x, y, w, h, canvas):
        pass
    

from tkinter import *

def initMenu(data):
    data.buttonX = data.width // 3
    data.buttonY = data.height // 3
    data.buttonW = data.width // 3
    data.buttonH = data.buttonW // 3

def drawMenu(canvas, data):
    (x0, y0, x1, y1) = data.buttonX, data.buttonY, data.buttonX+data.buttonW, data.buttonY+data.buttonH
    canvas.create_rectangle(x0, y0, x1, y1)
from tkinter import *

def initMenu(data):
    data.buttonX = data.width // 3
    data.buttonY = 2 * (data.height // 3)
    data.buttonW = data.width // 3
    data.buttonH = data.buttonW // 3

    data.buttonBox = (data.buttonX, data.buttonY,
    				  data.buttonX+data.buttonW, data.buttonY+data.buttonH)

def drawMenu(canvas, data):
    (x0, y0, x1, y1) = data.buttonBox
    canvas.create_rectangle(x0, y0, x1, y1)
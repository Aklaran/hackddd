from tkinter import *

def initMenu(data):
    data.buttonX = data.width // 3
    data.buttonY = 2 * (data.height // 3)
    data.buttonW = data.width // 3
    data.buttonH = data.buttonW // 3
    data.buttonBox = (data.buttonX, data.buttonY,
    				  data.buttonX+data.buttonW, data.buttonY+data.buttonH)

    data.listX = data.width // 3
    data.listY = data.buttonY - ((data.height - data.buttonY) // 2)
    data.listW = data.buttonW
    data.listH = data.listW // 4
    data.listBox = (data.listX, data.listY, data.listX+data.listW, data.listY+data.listH)

    data.upW = data.listW // 8
    data.upX = data.listX + data.listW - data.upW
    data.upY = data.listY
    data.upH = data.listH // 2
    data.upBox = (data.upX, data.upY, data.upX+data.upW, data.upY+data.upH)

    data.downW = data.upW
    data.downX = data.upX
    data.downY = data.listY + data.listH // 2
    data.downH = data.listH // 2
    data.downBox = (data.downX, data.downY, data.downX+data.downW, data.downY+data.downH)

    data.boxes = [data.buttonBox, data.listBox, data.upBox, data.downBox]

    data.scenes = ["n choose k", "counting in two ways", "subcommittee"]
    data.sceneIndex = 0
    data.sceneChoice = data.scenes[data.sceneIndex]

    data.buttonPressed = False

def changeListOption(data, dir):
    if dir == "up":
        if not data.sceneIndex == 0:
            data.sceneIndex -= 1
            data.sceneChoice = data.scenes[data.sceneIndex]
    elif dir == "down":
        if not data.sceneIndex == len(data.scenes) - 1:
            data.sceneIndex += 1
            data.sceneChoice = data.scenes[data.sceneIndex]

def drawMenu(canvas, data):

    for box in data.boxes:
        (x0, y0, x1, y1) = box
        canvas.create_rectangle(x0, y0, x1, y1)
        if box == data.listBox:
            canvas.create_text((x1+x0)/2, (y1+y0)/2, text=data.sceneChoice, font="Helvetica 24")

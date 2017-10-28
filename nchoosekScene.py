from nchoosekvisualization import nChooseKVisualization
from textInput import TextInput

def init(data):
    data.textInput = TextInput({"n":None, "k":None}, (0,0))
    data.varDict = data.textInput.setVars()
    data.visual = nChooseKVisualization(data.varDict["n"], data.varDict["k"],
                                        (0, 0, data.width, data.height))

def timerFired(data):
    data.visual.update(data.timerDelay / 500)

def redrawAll(canvas, data):
    data.visual.draw(canvas)
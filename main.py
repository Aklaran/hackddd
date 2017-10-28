def init(data):
    # load data.xyz as appropriate
    data.board = make2dList(data.rows, data.cols)
    data.player1, data.player2 = "blue", "orange"
    #sum = turnSum (out of 42),  score = total score (out of 5)
    data.player1Sum = data.player2Sum = 0
    data.player1Score = data.player2Score = 0
    data.position = [0, 0]
    data.currPlayer = data.player1
    data.gameOver = False
    data.winner = ''
    
    #calc data
    data.checkDirs = [ (-1, -1), (-1, 0), (-1, +1),
                       ( 0, -1),          ( 0, +1),
                       (+1, -1), (+1, 0), (+1, +1) ]
    
    # view data
    data.placeBuffer = 3
    data.gridWidth = data.width
    data.gridHeight = data.height - data.height//10
    data.yRadius = (data.gridHeight//data.rows)//2
    data.xRadius = (data.gridWidth//data.cols)//2

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    #only allow input if game is not over duh
    if not data.gameOver:
        # use event.char and event.keysym
        if event.keysym in ["Up", "Right", "Down", "Left"]:
            moveMarker(event,data)
        elif event.char in string.digits:
            placePiece(event, data)
        else: print("please choose a valid move")

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if not data.gameOver:
        # draw in canvas
        drawBoard(canvas, data)
        drawMarker(canvas, data)
        drawP1Score(canvas, data)
        drawP2Score(canvas, data)
        for row in range(data.rows):
            for col in range(data.cols):
                r, c = row, col
                d = data.board[row][col]
                if d: drawDigit(canvas, data, d, r, c)
    elif data.gameOver:
        canvas.create_text(data.width//2, data.height//2,
                           text=("GAME OVER - WINNER: %s" %data.winner), 
                           font="Arial 16 bold")
        drawP1Score(canvas, data)
        drawP2Score(canvas, data)

def run(rows, cols, width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.rows = rows
    data.cols = cols
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    run()
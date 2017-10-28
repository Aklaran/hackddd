from tkinter import*

def init(data):
    data.index = 0
    # load data.xyz as appropriate
    data.activated = False
    #data.listDex = 0
    data.args = [12,5]
    #l = listMaker(data.args[0],data.args[1],data.args[2])
    #data.len = len(l)
    
    
   

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "a":
        data.activated = True
    print(event.keysym)
    if event.keysym == "Right" and data.index <  data.args[0]  - data.args[1] - 3 :
        data.index += 1
        
    if event.keysym == "Left" and data.index > 0:
        data.index -= 1
    print(data.index)


def timerFired(data):
    pass

def redrawAllPostFix(canvas, data):
    #if data.activated:
     #   listmaker(4,5,4,canvas)
    initialForm(data.args[0],data.args[1],canvas, data)
    boxesAndText(data.args[0],data.args[1],canvas, data)
    theBracketsBelow(data.args[0],data.args[1],canvas, data)
    

        
def inABox(x,y):
    for i in range(0,4):
        if x in range(data.width / 20 * (r + 3.5 * i)  + data.width // 9,data.width / 20 * (r + 3.5 * i + 3) + data.width // 9):
            if y in range(data.height / 20 * (r + 6),data.height/20 * (r + 11)):
                return i
        return -1
                
        canvas.create_rectangle(data.width / 20 * (r + 3.5 * i)  + data.width // 9, data.height / 20 * (r + 6), data.width / 20 * (r + 3.5 * i + 3) + data.width // 9, data.height/20 * (r + 11), width = 4)
        

    

#def listMaker(m,n,k):
    #l = []
    #i = 0
    #a = m
    #b = n
    #c = k
    #while i <= k:
        #l.append([a,b,i,k-i])
        #i+= 1
        
    return l
        
    
def initialForm(n,k,canvas, data):
    r = 2
    s = data.width // 70
    canvas.create_line(data.width/20  * .97, data.height/20 * r, data.width/10, data.height/20 * r, width = s//2)
    canvas.create_line(data.width/20 , data.height/20 * r, data.width / 20 * 1.5 + 2, data.height/20 * (r + 1) + 2, width = s//2)
    canvas.create_line(data.width / 20 * 1.5, data.height / 20 * (r + 1), data.width/20, data.height/20 * (r + 2), width = s//2)
    canvas.create_line(data.width/20 * .97, data.height/20 * (r + 2), data.width/10, data.height/20 * (r + 2), width = s//2)
    canvas.create_text(data.width/16  , data.height/20 * (3 * r / 4) * .95, text = "n - k", font = "helvetica "+ str(s), anchor = W)
    canvas.create_text(data.width/16 , data.height/20 * ((21 * (r+1)) / 16 * 1.05 ), text = "i = 0", anchor = NW, font = "helvetica " + str(s))
    canvas.create_text(data.width / 10 * (7 / 4),data.height/20 * (r + 1), text = "(   )", font = "helvetica " + str(4*s))
    #canvas.create_text(data.width / 10 * (11 / 4),data.height/20 * (r + 1), text = "(   )", font = "helvetica " + str(4*s))
    canvas.create_text(data.width / 10 * 7/4, data.height/20 * (r + 1) * .9, text = "n - i", font = "helvetica " + str(int(1.5 * s )))
    canvas.create_text(data.width / 10 * 7/4, data.height/20 * (r + 1) * 1.25, text = " k", font = "helvetica " + str(int(1.5 * s)))
    #canvas.create_text(data.width / 10 * 2.8, data.height/20 * (r + 1) * .9, text = str(69), font = "helvetica " + str(int(1.3 * s )))
    #canvas.create_text(data.width / 10 * 2.8, data.height/20 * (r + 1) * 1.25, text = "boobs", font = "helvetica " + str(int(1.3 * s)))
    canvas.create_line(data.width / 10 , data.height / 20 * (r + 3), data.width / 10 , data.height / 20 * (r + 5), width = int(s / 1.3))
    canvas.create_polygon(data.width / 10 * 9/4, data.height / 20 * (r + 5), data.width / 10 * 2, data.height / 20 * (r + 5), data.width / 10 * 17/8, data.height / 20 * (r + 5), width = 5, fill = "red")
    canvas.create_rectangle(data.width / 20, data.height / 20 * (r + 6), data.width/5.5, data.height/20 * (r + 11), width = 4)
    canvas.create_line(data.width / 10 * 1.9, data.height / 20 * (r + 8) * .98, data.width / 10 * 2.05,  data.height / 20 * (r + 8) * .98, width = 2)
    canvas.create_line(data.width / 10 * 1.9, data.height / 20 * (r + 8) * 1.03, data.width / 10 * 2.05,  data.height / 20 * (r + 8) * 1.03, width = 2)
    canvas.create_text(data.width / 20 + 3, data.height / 20 * (r + 6) + 3, anchor = NW, text = "Pick m + n total buttholes from a group of k objects" , width = data.width / 8, font = "helvetica " + str(s), justify = CENTER)
    canvas.create_text(data.width / 20 + 3, data.height / 20 * (r + 13.5) + 3, text = "(    )" , font = "helvetica " + str(int(3.5 * s)), anchor = W)
    canvas.create_text(data.width / 8.5, data.height / 20 * (r + 13.5) + 3, text = "n + 1     k + 1" , font = "helvetica " + str(s), width = 100 , justify =  CENTER)
    
    
def boxesAndText(n,k,canvas, data):
    r = 2
    x = 0
    #l = listMaker(m,n,k)
    s = data.width//70
    for i in range(0,4):
        canvas.create_rectangle(data.width / 20 * (r + 3.5 * i)  + data.width // 7, data.height / 20 * (r + 6), data.width / 20 * (r + 3.5 * i + 3) + data.width // 8, data.height/20 * (r + 11), width = 4)
        if i > 0:
            canvas.create_text(data.width / 20 * (r + 3.5 * i)  + data.width // 8, data.height / 20 * (r + 8), text = "+", font = "helvetica " + str(s))
    for i in range(data.index,data.index + 4):
        canvas.create_text(data.width / 20 * (r + 3.5 * x)  + data.width // 6.6, data.height / 20 * (r + 6), anchor = NW, text = "Choose " + str(k) + " people from a group of " + str(n - i) + " people " ,font = "helvetica " + str(s), justify = CENTER, width = int(8*s))
        x += 1
    if 69 != 69 - 4:
        canvas.create_text(data.width / 20 * (r + 3.6 * 4)  + data.width // 10, data.height / 20 * (r + 8), text = "+ ...", font = "helvetica " +str(s))
        
    
    x += 1
    
    if 69 != 0:
        canvas.create_text(data.width / 20 * (r + 3.6 * .13)  + data.width // 10, data.height / 20 * (r + 8), text = "... +", font = "helvetica " +str(s))
        
def theBracketsBelow(n,k,canvas, data):
    r = 2
    x = 0
    s = data.width//70
    l = 69
    for i in range(0,4): 
        canvas.create_text(data.width / 20 * (r + 3.6 * i + 1.5)  + data.width // 8,data.height/20 * (r + 14), text = "(      )", font = "helvetica " + str(3 * s) )
       # canvas.create_rectangle(data.width / 20 * (r + 3.5 * i)  + data.width // 9, data.height / 20 * (r + 6), data.width / 20 * (r + 3.5 * i + 3) + data.width // 9, data.height/20 * (r + 11), width = 4)
        if i > 0:
            canvas.create_text(data.width / 20 * (r + 3.5 * i)  + data.width // 8, data.height / 20 * (r + 14), text = "+", font = "helvetica " + str(s))
    for i in range(data.index, data.index + 4):
     #   canvas.create_text(data.width / 20 * (r + 3.5 * x)  + data.width // 6.6, data.height / 20 * (r + 6), anchor = NW, text = "Choose " + str(l[i][2]) + " people from a group of " + str(l[i][1]) + ", and " + str(l[i][3]) + " from a group of " + str(l[i][0]), width = data.width / 8 , font = "helvetica " + str(s), justify = CENTER)
        canvas.create_text(data.width / 20 * (r + 3.6 * x)  + data.width // 5, data.height / 20 * (r + 14.7), text = str(k), font = "helvetica " + str(s))
        canvas.create_text(data.width / 20 * (r + 3.6 * x)  + data.width // 5, data.height / 20 * (r + 13.7), text = str(n - i), font = "helvetica " + str(s))
        #canvas.create_text(data.width / 20 * (r + 3.6 * x + 1.4 )  + data.width // 6, data.height / 20 * (r + 13.7), text = str(69), font = "helvetica " + str(s))
        #canvas.create_text(data.width / 20 * (r + 3.6 * x + 1.4)  + data.width // 6, data.height / 20 * (r + 14.7), text = str(69), font = "helvetica " + str(s))
        x += 1
    
    
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllPostFix(canvas, data)
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

run(1400, 700)
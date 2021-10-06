"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["Number of rows"] = 10
    data["Number of cols"] = 10
    data["Board Size"] = 500
    data["Cell Size"] = data["Board Size"] / data["Number of rows"] 
    data["num Of Ships"] = 5
    data["computer Board"] = emptyGrid(data["Number of rows"],data["Number of cols"])
    data["user Board"] = emptyGrid(data["Number of rows"],data["Number of cols"]) 
    #data["user Board"] = test.testGrid()
    data["computer Board"] = addShips(data["computer Board"],data["num Of Ships"]) 
    data["temporary_ship"]= []
    data["num of user ships"]= 0

    return 


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user Board"],True)
    drawShip(data,userCanvas,data["temporary_ship"])
    drawGrid(data,compCanvas,data["computer Board"],True)
    return

'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        x=[]
        for j in range(cols):
            x.append(EMPTY_UNCLICKED )
        grid.append(x)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    center_rows=random.randint(1,8)
    center_cols=random.randint(1,8)
    edge=random.randint(0,1)
    if edge==0:
        ship= [[center_rows-1,center_cols], [center_rows,center_cols] , [center_rows+1,center_cols]]
    else:
        ship = [[center_rows,center_cols-1] , [center_rows,center_cols] , [center_rows,center_cols+1]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):  
    for i in ship:
        if (grid[i[0]][i[1]]!= EMPTY_UNCLICKED):
            return False    
    return True



'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    ship_count=0
    while ship_count!=numShips:
        ship=createShip()
        if checkShip(grid,ship)==True:
            for i in ship:
                grid[i[0]][i[1]]=SHIP_UNCLICKED
            ship_count+=1
    return (grid)



'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["Number of rows"]):
        for col  in range(data["Number of cols"]):
            if grid[row][col] == SHIP_UNCLICKED: 
                
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="yellow")
            else:
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="blue")
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ((ship[0][1])==(ship[1][1])==(ship[2][1])):
        if ship[0][0]== (ship[1][0]-1)== (ship[2][0]-2):
            return True
        return False
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ((ship[0][0])==(ship[1][0])==(ship[2][0])):
        if ship[0][1]== (ship[1][1]-1)== (ship[2][1]-2):
            return True
        return False
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    row_coordinate = int(event.y/data["Cell Size"])
    col_coordinate = int(event.x/data["Cell Size"])
    return  [row_coordinate,col_coordinate]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        canvas.create_rectangle(data["Cell Size"]*ship[i][1] , data["Cell Size"]*ship[i][0] , data["Cell Size"]*(ship[i][1]+1) , data["Cell Size"]*(ship[i][0]+1), fill ="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if (checkShip(grid, ship)) ==True :
        if (isVertical(ship)) == True :
            return True
        elif (isHorizontal(ship))== True:
            return True
        else:
            return False
    else:
        return False

'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
   if shipIsValid(data["user Board"],data["temporary_ship"])==True:
        for ship_list in data["temporary_ship"] :
            data["user Board"][ship_list[0]][ship_list [1]] = SHIP_UNCLICKED
        data["num of user ships"]=data["num of user ships"]+1
   else:
        print("ship is not vaild")
   data["temporary_ship"]=[]
   return

'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["num of user ships"]==5:
       return 
    if [row,col] not in data["temporary_ship"]:
        data["temporary_ship"].append([row,col])
        if len(data["temporary_ship"])==3:
          placeShip(data)
        if data["num of user ships"]==5:  
            print("start playing the game")
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    #runSimulation(500, 500)
    test.testGetClickedCell()

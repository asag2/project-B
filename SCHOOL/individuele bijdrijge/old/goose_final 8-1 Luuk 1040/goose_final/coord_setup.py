# creates a dictionary to be used as a grid (coordinates). Stored with plain string keys. Values are empty.

lX = 0
cDict = {}
while lX <= 35:
    lY = 0
    while lY <= 11:
        lC = str(lX) + ', ' + str(lY)
        # lC = '(' + str(lX) + ', ' + str(lY) + ')'
        # lC = (lX, lY)
        cDict[lC] = []
        lY += 1
    lX += 1

eX = 0
cDictEvents = {}
while eX <= 35:
    eY = 0
    while eY <= 11:
        eC = str(eX) + ', ' + str(eY)
        # lC = '(' + str(lX) + ', ' + str(lY) + ')'
        # lC = (lX, lY)
        cDictEvents[eC] = []
        eY += 1
    eX += 1

rX = 0
cDictBackwards = {}
while rX <= 35:
    rY = 0
    while rY <= 11:
        rC = str(rX) + ', ' + str(rY)
        # lC = '(' + str(lX) + ', ' + str(lY) + ')'
        # lC = (lX, lY)
        cDictBackwards[rC] = []
        rY += 1
    rX += 1

    
# lists of coordinates. These lists will be used to add directions to the grid dictionary as values.
upList = ['13, 2','24, 11','26, 11','35, 11','26, 9','28, 9','28, 6','19, 9','19, 7','24, 2','19, 4','22, 7', '35, 5', '35, 8']
rightList = ['0, 0', '3, 0', '11, 2', '11, 11', '13, 0', '0, 5','7, 6','0, 8','7, 9','0, 11','9, 11','24, 11','26, 11','26, 9','28, 8','26, 6','28, 5','19, 0','22, 2','19, 7','13, 7','24, 0']
downList = ['11, 0','0, 2','0, 5','0, 8','7, 5','7, 8','9, 6','9, 9','16, 0','22, 0','16, 4','13, 4','16, 7','11, 9']
leftList = ['11, 2', '16, 4', '16, 9', '24, 9', '22, 4', '35, 2']

mcqList = ['10, 0', '8, 2', '13, 2', '5, 5', '0, 6', '4, 8', '5, 8', '6, 8', '9, 10', '13, 2', '13, 5', '13, 6', '13, 9', '21, 4', '22, 5', '22, 11', '26, 2', '31, 2', '34, 2', '30, 5', '31, 5', '32, 11']

# redEventList = ['7, 0', '11, 1', '15, 0', '4, 2', '16, 2', '1, 5', '8, 6', '1, 5', '16, 5', '16, 6', '8, 6', '2, 8', '3, 8', '7, 8', '7, 9', '3, 11', '14, 9', '15, 9', '17, 11', '18, 11', '21, 0', '33, 0', '34, 0', '19, 1', '22, 2', '19, 5', '33, 5', '19, 6', '26, 6', '27, 6', '26, 7', '21, 9', '22, 9', '35, 9', '27, 11']

redEventList = []

backwardsUpList = ["11, 2"]
backwardsRightList = ["0, 2"]
backwardsDownList = []
backwardsLeftList = ["11, 0", "13, 2"]

finishlineList = ["35, 0"]


# this functions adds a direction (string) to each element (coordinates) of the given list. If a direction already exists, adds it to a lists with all directions for that coordinate.
def addDirections(dirList, dirV):
    global cDict
    for d in dirList:
        if len(cDict[d]) >= 1:
            temp = [cDict[d], [dirV]]
            cDict[d] = temp
        else:
            cDict[d] = [dirV]

def addEvents(eventList, dirV):
    global cDictEvents
    for d in eventList:
        if len(cDictEvents[d]) >= 1:
            temp = [cDictEvents[d], [dirV]]
            cDictEvents[d] = temp
        else:
            cDictEvents[d] = [dirV]

def addBackwards(backwardsDirList, dirV):
    global cDictBackwards
    for d in backwardsDirList:
        if len(cDictBackwards[d]) >= 1:
            temp = [cDictBackwards[d], [dirV]]
            cDictBackwards[d] = temp
        else:
            cDictBackwards[d] = [dirV]

# calls the addDirections function, parameters are a list (coordinates) and a string (direction/other type of event)
addDirections(upList, "up")
addDirections(rightList, "right")
addDirections(downList, "down")
addDirections(leftList, "left")

# calls the addEvents function, adds the string to the coordinates (coordinates are in the List parameters)
addEvents(mcqList, "mcq")
addEvents(redEventList, "red")
addEvents(finishlineList, "finish")

addBackwards(backwardsUpList, "up")
addBackwards(backwardsRightList, "right")
addBackwards(backwardsDownList, "down")
addBackwards(backwardsLeftList, "left")
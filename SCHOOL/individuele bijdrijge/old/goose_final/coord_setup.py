# creates a dictionary to be used as a grid (coordinates). Stored with plain string keys. Values are empty.
lX = 0
cDict = {}
while lX <= 35:
    lY = 0
    while lY <= 11:
        lC = str(lX) + ", " + str(lY)
        cDict[lC] = []
        lY += 1
    lX += 1

eX = 0
cDictEvents = {}
while eX <= 35:
    eY = 0
    while eY <= 11:
        eC = str(eX) + ", " + str(eY)
        cDictEvents[eC] = []
        eY += 1
    eX += 1

rX = 0
cDictBackwards = {}
while rX <= 35:
    rY = 0
    while rY <= 11:
        rC = str(rX) + ", " + str(rY)
        cDictBackwards[rC] = []
        rY += 1
    rX += 1

    
# lists of coordinates. These lists will be used to add directions to the grid dictionary as values.
# upList = ["13, 2", "24, 11", "26, 11", "35, 11", "26, 9", "28, 9", "28, 6", "19, 9", "19, 7", "24, 2", "19, 4", "22, 7", "35, 5", "35, 8"]
# rightList = ["0, 0", "3, 0", "11, 2", "11, 11", "13, 0", "0, 5", "7, 6", "0, 8", "7, 9", "0, 11", "9, 11", "24, 11", "26, 11", "26, 9", "28, 8", "26, 6", "28, 5", "19, 0", "22, 2", "19, 7", "13, 7", "24, 0"]
# downList = ["11, 0", "0, 2", "0, 5", "0, 8", "7, 5", "7, 8", "9, 6", "9, 9", "16, 0", "22, 0", "16, 4", "13, 4", "16, 7", "11, 9"]
# leftList = ["11, 2", "16, 4", "16, 9", "24, 9", "22, 4", "35, 2"]

mcqList = ["10, 0", "8, 2", "5, 5", "0, 6", "4, 8", "5, 8", "6, 8", "9, 10", "13, 2", "13, 5", "13, 6", "13, 9", "21, 4", "22, 5", "22, 11", "26, 2", "31, 2", "34, 2", "30, 5", "31, 5", "32, 11"]

redEventList = ["7, 0", "11, 1", "15, 0", "4, 2", "16, 2", "1, 5", "8, 6", "1, 5", "16, 5", "16, 6", "8, 6", "2, 8", "3, 8", "7, 8", "7, 9", "3, 11", "14, 9", "15, 9", "17, 11", "18, 11", "21, 0", "33, 0", "34, 0", "19, 1", "22, 2", "19, 5", "33, 5", "19, 6", "26, 6", "27, 6", "26, 7", "21, 9", "22, 9", "35, 9", "27, 11"]

# redEventList = []

backwardsUpList = ["11, 2", "16, 4", "16, 7", "11, 11", "9, 11", "0, 11", "0, 8", "0, 5", "7, 6", "7, 9", "16, 4", "16, 7", "16, 9", "22, 2", "13, 7"]
backwardsRightList = ["0, 2", "13, 4", "11, 9", "24, 2", "19, 9", "19, 4"]
backwardsDownList = ["13, 3", "19, 0", "28, 5", "28, 8", "26, 6", "26, 9", "24, 9", "19, 7", "22, 4", "24, 0", "13, 0", "16, 2"]
backwardsLeftList = ["11, 0", "13, 2", "7, 5", "9, 6", "9, 9", "7, 8", "35, 5", "35, 8", "35, 11", "28, 9", "28, 6", "26, 11", "24, 11", "22, 7", "22, 0"]


upList = ["13, 2", "13, 1",
"19, 9", "19, 8", "19, 7", "19, 6", "19, 5", "19, 4", "19, 3", "19, 2", "19, 1",
"22, 7", "22, 6", "22, 5",
"24, 11", "24, 10", "24, 2", "24, 1",
"26, 11", "26, 10", "26, 9", "26, 8", "26, 7",
"28, 9", "28, 6",
"35, 11", "35, 10", "35, 9", "35, 8", "35, 7", "35, 6", "35, 5", "35, 4", "35, 3", 
]
rightList = ["0, 0", "1, 0", "2, 0", "3, 0", "4, 0", "5, 0", "6, 0", "7, 0", "8, 0", "9, 0", "10, 0", "13, 0", "14, 0", "15, 0", "19, 0", "20, 0", "21, 0", "24, 0", "25, 0", "26, 0", "27, 0", "28, 0", "29, 0", "30, 0", "31, 0", "32, 0", "33, 0", "34, 0",
"11, 2", "22, 2", "23, 2",
"0, 5", "1, 5", "2, 5", "3, 5", "4, 5", "5, 5", "6, 5", "28, 5", "29, 5", "30, 5", "31, 5", "32, 5", "33, 5", "34, 5",
"7, 6", "8, 6", "26, 6", "27, 6",
"13, 7", "14, 7", "15, 7", "19, 7", "20, 7", "21, 7",
"0, 8", "1, 8", "2, 8", "3, 8", "4, 8", "5, 8", "6, 8", "28, 8", "29, 8", "30, 8", "31, 8", "32, 8", "33, 8", "34, 8",
"7, 9", "8, 9", "26, 9", "27, 9",
"0, 11", "1, 11", "2, 11", "3, 11", "4, 11", "5, 11", "6, 11", "7, 11", "8, 11", "9, 11", "10, 11", "11, 11", "12, 11", "13, 11", "14, 11", "15, 11", "16, 11", "17, 11", "18, 11", "19, 11", "20, 11", "21, 11", "22, 11", "23, 11", "24, 11", "25, 11", "26, 11", "27, 11", "28, 11", "29, 11", "30, 11", "31, 11", "32, 11", "33, 11", "34, 11",
]
downList = ["0, 2", "0, 3", "0, 4", "0, 5", "0, 6", "0, 7", "0, 8", "0, 9", "0, 10",
"7, 5", "7, 8",
"9, 6", "9, 7", "9, 8", "9, 9", "9, 10",
"11, 0", "11, 1", "11, 9", "11, 10",
"13, 4", "13, 5", "13, 6",
"16, 0", "16, 1", "16, 2", "16, 3", "16, 4", "16, 5", "16, 6", "16, 7", "16, 8",
"22, 0", "22, 1", 
]
leftList = ["1, 2", "2, 2", "3, 2", "4, 2", "5, 2", "6, 2", "7, 2", "8, 2", "9, 2", "10, 2", "11, 2",
"14, 4", "15, 4", "16, 4", "20, 4", "21, 4", "22, 4",
"12, 9", "13, 9", "14, 9", "15, 9", "16, 9", "20, 9", "21, 9", "22, 9", "23, 9", "24, 9",
"35, 2", "34, 2", "33, 2", "32, 2", "31, 2", "30, 2", "29, 2", "28, 2", "27, 2", "26, 2", "25, 2", 
]

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
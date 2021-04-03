
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
    
# lists of coordinates. These lists will be used to add directions to the grid dictionary as values.
upList = ['13, 2','24, 11','26, 11','35, 11','26, 9','28, 9','28, 6','19, 9','19, 7','24, 2','19, 4','22, 7', '35, 5', '35, 8']
rightList = ['0, 0', '11, 2', '11, 11', '13, 0', '0, 5','7, 6','0, 8','7, 9','0, 11','9, 11','24, 11','26, 11','26, 9','28, 8','26, 6','28, 5','19, 0','22, 2','19, 7','13, 7','24, 0']
downList = ['11, 0','0, 2','0, 5','0, 8','7, 5','7, 8','9, 6','9, 9','16, 0','22, 0','16, 4','13, 4','16, 7','11, 9']
leftList = ['11, 2', '16, 4', '16, 9', '24, 9', '22, 4', '35, 2']

# this functions adds a direction (string) to each element (coordinates) of the given list. If a direction already exists, adds it to a lists with all directions for that coordinate.
def addDirections(dirList, dirV):
    global cDict
    for d in dirList:
        if len(cDict[d]) >= 1:
            temp = [cDict[d], [dirV]]
            cDict[d] = temp
        else:
            cDict[d] = [dirV]

# calls the addDirections functions, parameters are a list (coordinates) and a string (direction)
addDirections(upList, 'up')
addDirections(rightList, 'right')
addDirections(downList, 'down')
addDirections(leftList, 'left')
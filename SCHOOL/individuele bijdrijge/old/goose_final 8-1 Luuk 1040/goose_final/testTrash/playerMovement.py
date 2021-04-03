# function which moves the player on a grid according to the direction it is given. Parameters are the rolled dice and the currently rolling player.
def movePlayer(rolledDice, player, cDict):
    global player1, player2, player3, player4, player5, player6, chooseRoute
    i = 0
    playerDirection = player[2]

    while rolledDice > 0:

        # takes the player location on the grid, [-1] for the coordinates in string
        tileDirection = cDict[player[-1]]
        print(tileDirection)
        # checks if there are multiple directions at the player location. If so, lets the user pick a direction.
        
        if len(tileDirection) > 1:
            chooseRoute = 2
            print(chooseRoute)
            #pickedDirection = input(f'Pick a direction: \n > type the letter A for {tileDirection[0]} \n > type the letter B for {tileDirection[1]} \n >>> ')
            #print(pickedDirection)
            #if pickedDirection == 'A':
            #    tileDirection = tileDirection[0]
            #else:
            #    tileDirection = tileDirection[1]
            
            # weetJijVeel = int(random(0, 2))
            # tileDirection = tileDirection[weetJijVeel]
        
        # checks if the player location has a direction. If so, take that as the direction. If not, take the stored player direction as the direction.
        if tileDirection == []:
            playerDirection = player[2]
        else:
            playerDirection = tileDirection
            player[2] = tileDirection

        # checks what the direction is. Then changes the players locations coordinates in int and in string to the new location.
        if playerDirection == ['up']:
            player[1] -= 1
            #moveBitch(player, playerDirection)
        elif playerDirection == ['right']:
            player[0] += 1
            #moveBitch(player, playerDirection)
        elif playerDirection == ['down']:
            player[1] += 1
            #moveBitch(player, playerDirection)
        elif playerDirection == ['left']:
            player[0] -= 1
            #moveBitch(player, playerDirection)
        player[-1] = str(player[0]) + ', ' + str(player[1])
        print(player, '<- Print player [X, Y, [dir], XY in string]')




        # if player reaches the last tile with the given coordinates, the player wins
        if player[-1] == '35, 0':
            print('You win!')
            exit()

        # lower dice because infinite loop is no bueno
        rolledDice -= 1

def moveBitch(player):
    global posxp1, posyp1, posxp2, posyp2, posxp3, posyp3, posxp4, posyp4, posxp5, posyp5, posxp6, posyp6
    playerDirection = player[2]
    stapje = 33
    # print('GET OUT THE WAY', player[3])
    if player[3] == 'player1':
        if playerDirection == ['up']:
            posyp1 -= stapje
        if playerDirection == ['right']:
            posxp1 += stapje
        if playerDirection == ['down']:
            posyp1 += stapje
        if playerDirection == ['left']:
            posxp1 -= stapje
    if player[3] == 'player2':
        if playerDirection == ['up']:
            posyp2 -= stapje
        if playerDirection == ['right']:
            posxp2 += stapje
        if playerDirection == ['down']:
            posyp2 += stapje
        if playerDirection == ['left']:
            posxp2 -= stapje
    if player[3] == 'player3':
        if playerDirection == ['up']:
            posyp3 -= stapje
        if playerDirection == ['right']:
            posxp3 += stapje
        if playerDirection == ['down']:
            posyp3 += stapje
        if playerDirection == ['left']:
            posxp3 -= stapje
    if player[3] == 'player4':
        if playerDirection == ['up']:
            posyp4 -= stapje
        if playerDirection == ['right']:
            posxp4 += stapje
        if playerDirection == ['down']:
            posyp4 += stapje
        if playerDirection == ['left']:
            posxp4 -= stapje
    if player[3] == 'player5':
        if playerDirection == ['up']:
            posyp5 -= stapje
        if playerDirection == ['right']:
            posxp5 += stapje
        if playerDirection == ['down']:
            posyp5 += stapje
        if playerDirection == ['left']:
            posxp5 -= stapje
    if player[3] == 'player6':
        if playerDirection == ['up']:
            posyp6 -= stapje
        if playerDirection == ['right']:
            posxp6 += stapje
        if playerDirection == ['down']:
            posyp6 += stapje
        if playerDirection == ['left']:
            posxp6 -= stapje

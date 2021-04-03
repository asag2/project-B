import coord_setup
from coord_setup import cDict 
from coord_setup import cDictEvents
from coord_setup import cDictBackwards
import dice
from questions import q1, q2, q3, q4, q5, q6, q7
from random import randrange
from redTiles import redTiles

'''###################################################################################################################
######################################################################################################################
######################################################################################################################
Dit wordt speelbord final. hierin komen alle componenten die we gemaakt hebben om het hele spel te laten functioneren.
######################################################################################################################
######################################################################################################################
###################################################################################################################'''

grid = False



''' Dit zijn de spelerscoordinaten van iedere speler '''

posxp1, posxp2, posxp3, posxp4, posxp5, posxp6 = 68, 68, 68, 68, 68, 68
posyp1, posyp2, posyp3, posyp4, posyp5, posyp6 = 28, 28, 28, 28, 28, 28

player1 = [0, 0, 'right', 'player1', '0, 0']
player2 = [0, 0, 'right', 'player2', '0, 0']
player3 = [0, 0, 'right', 'player3', '0, 0']
player4 = [0, 0, 'right', 'player4', '0, 0']
player5 = [0, 0, 'right', 'player5', '0, 0']
player6 = [0, 0, 'right', 'player6', '0, 0']
playerNone = [0, 0, 'right', 'None Selected', "0, 0"]

currentPlayer = player1

''' Dit zijn globale beginvariabelen van de players en van de inventory code '''
players = 0
player = 0
position1, position2, position3, position4, position5, position6,  = 0, 0, 0, 0, 0, 0
score, score2, score3, score4, score5, score6 = 1000, 1000, 1000, 1000, 1000, 1000
screen = 1
player1Finished = False
player2Finished = False
player3Finished = False
player4Finished = False
player5Finished = False
player6Finished = False

playerWinList = []

''' Intersection Variables'''
chooseRoute = False
intersectionUp = False
intersectionRight = False
intersectionDown = False
intersectionLeft = False
playerIntersectionChoice = ''

''' MCQ Variables '''
mcqEvent = False
mcqIterator = 1
timesAnswered = 0
possibleAnswerList = ["a", "b", "c", "d"]
vraag = ''
answer = ''
check = False
checkAnswer = False
removeMCQ = False

''' Red Tile Variables '''
redTileEvent = False
redTileIterator = True
z = 1
redTileMove = 0

''' Dice variables '''
dice.diceIsOne = False
dice.diceIsTwo= False
dice.diceIsThree = False
dice.diceIsFour = False
dice.diceIsFive = False
dice.diceIsSix = False


''' Inventory of players ----- Jingkit '''

def allItems():
    return {'item1' : 0 , 'item2' : 0 ,'item3' : 0 , 'item4' : 0 , 'item5' : 0 , 'item6' : 0 , 'item7' : 0 , 'item8' : 0} 
inventoryDict = allItems()
inventoryDict2 = allItems()
inventoryDict3 = allItems()
inventoryDict3 = allItems()
inventoryDict4 = allItems()
inventoryDict5 = allItems()
inventoryDict6 = allItems()
inventoryDict7 = allItems()
inventoryDict8 = allItems()

'''
Dit is de hoeveelheid pixels die één stap naar een andere tegel nodig heeft, om precies in het midden te komen.
met meer of minder pixels loopt ie uiteindelijk scheef
'''

stapje = 33

'''
Initial setup met de resolutie van 1366 x 768
Het laadt een achtergrond en een gans spelertje in
'''

def setup():
    size(1366,768)
    # frameRate(2)
    global speelbord
    global gans1, gans2, gans3, gans4, gans5, gans6
    
    

    '''
    jingkits code
    '''
    global img, store, twoplayers, threeplayers, fourplayers, fiveplayers, sixplayers, player, achtergrond, achtergrondwinscreen, players
    
    img = loadImage('Scoreachtergrond.png')
    store = loadImage('store.png')
    twoplayers = loadImage('twoplayers.PNG')
    threeplayers = loadImage('threeplayers.png')
    fourplayers = loadImage('fourplayers.png')
    fiveplayers = loadImage('fiveplayers.png')
    sixplayers = loadImage('sixplayers.png')
    store = loadImage('store.png')
    
    achtergrond = loadImage("bordspel.png")

    '''
    achtergrond = loadImage("speelbord_events_blue.png")
    achtergrond = loadImage("speelbord_events_yellow.png")
    '''

    gans1 = loadImage("gans player 1.1.png")
    gans2 = loadImage("gans player 2.1.png")
    gans3 = loadImage("gans player 3.png")
    gans4 = loadImage("gans player 4.png")
    gans5 = loadImage("gans player 5.png")
    gans6 = loadImage("gans player 6.png")
    
    if players == 2:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen2p.png")
    elif players == 3:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen3p.png")
    elif players == 4:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen4p.png")
    elif players == 5:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen5p.png")
    elif players == 6:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen6p.png")
    
    



    

def draw(): 
    global posX, posY, grid, playerWinList, achtergrondwinscreen, listToStr 
    
    global redTileIterator, z, redTileMove
    global screen, store, twoplayers, threeplayers, fourplayers, players, fiveplayers, sixplayers, inventoryDict, player, mcqIterator, mcqEvent, currentPlayer
    
    ''' First screen to choose the player amount ---- Jingkit '''
    
    rect(286, 150, 200, 200)
    rect(586, 150, 200, 200)
    rect(886, 150, 200, 200)
    rect(433, 400, 200, 200)
    rect(736, 400, 200, 200)
    image(twoplayers, 296, 160, 180, 180)
    image(threeplayers, 596, 160, 180, 180)
    image(fourplayers, 896, 160, 180, 180)
    image(fiveplayers, 443, 410, 180, 180)
    image(sixplayers, 746, 410, 180, 180)
    
    if players == 2:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen2p.png")
    elif players == 3:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen3p.png")
    elif players == 4:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen4p.png")
    elif players == 5:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen5p.png")
    elif players == 6:
        achtergrondwinscreen = loadImage("Achtergrondwinscreen6p.png")
    

    

        
        
    
    ''' Game board '''
    if screen == 2:
        background(achtergrond)

        dice.dice()
        dice.rollButtons()

        ''' Shows the currently selected player '''
        textSize(30)
        text("Currently selected player: " + str(currentPlayer[-2]),(width/2)-250, 25)
        textSize(12)
        


        if grid:
            col = 0
            breedte = 36
            hoogte = 12
            while col < breedte: 
                fill(0,0,0)
                row = 0
                while row < hoogte: 
                    textSize(10)
                    text(str(col)+","+str(row), 80+(stapje * col), 60+(stapje * row))
                    textSize(12)
                    row += 1
                
                col += 1









        ''' Player score/inventoy ---- Ayub '''

        if players == 2 :
            image(gans1,posxp1,posyp1)
            image(gans2,posxp2,posyp2)
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            

            
            fill(255)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position1), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position2), 150, 650)
        elif players == 3 :
            image(gans1,posxp1,posyp1)
            image(gans2,posxp2,posyp2)
            image(gans3,posxp3,posyp3)
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
        
            fill(255)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position1), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position2), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position3), 270, 650)
        elif players == 4 :
            image(gans1,posxp1,posyp1)
            image(gans2,posxp2,posyp2)
            image(gans3,posxp3,posyp3)
            image(gans4,posxp4,posyp4)
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            
            fill(255)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position1), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position2), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position3), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position4), 400, 650)
        elif players == 5 :
            image(gans1,posxp1,posyp1)
            image(gans2,posxp2,posyp2)
            image(gans3,posxp3,posyp3)
            image(gans4,posxp4,posyp4)
            image(gans5,posxp5,posyp5)
            
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            image(img, 510, 600, 100, 100)

            fill(255)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position1), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position2), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position3), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position4), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score5), 520, 640)
            text('Position: ' + str(position5), 520, 650)
        elif players == 6 :
            image(gans1,posxp1,posyp1)
            image(gans2,posxp2,posyp2)
            image(gans3,posxp3,posyp3)
            image(gans4,posxp4,posyp4)
            image(gans5,posxp5,posyp5)
            image(gans6,posxp6,posyp6)
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            image(img, 510, 600, 100, 100)
            image(img, 630, 600, 100, 100) 
            fill(255)
            
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position1), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position2), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position3), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position4), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score5), 520, 640)
            text('Position: ' + str(position5), 520, 650)
            text('Player 6 ', 640, 620)
            text('Score: ' + str(score6), 640, 640)
            text('Position: ' + str(position6), 640, 650)

            '''
            ##############inventory scetch---- Jingkit
            '''
    if screen == 3:
        background(achtergrond)
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 100, 970, 658) 
        fill(255,255,255)
        textSize(55)
        text('Inventory', 40, 80)
        fill(255,255,255)
        rect(40, 190, 600, 550)
        textSize(32)
        fill(255,255,255)
        text('Player ' + str(player) , 40, 140)
        image(store, 890, 5, 100, 100)
        text('Return', 870, 150)

        '''
        ############items in inventory
        '''
        if player == 1:
            itemsInInventory1()
        elif player == 2:
            itemsInInventory2()
        elif player == 3:
            itemsInInventory3()
        elif player == 4:
            itemsInInventory4()            
        elif player == 5:
            itemsInInventory5()            
        elif player == 6:
            itemsInInventory6() 

        '''
        ##############buy menu scetch----Ayub
        '''

    if screen == 4:
        background(achtergrond)
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 100, 970, 658) 
        fill(255,255,255)
        textSize(32)
        text('Player ' +str(player), 40, 140 )
        
        if player == 1:
            text('Score ' + str(score), 40, 170)
        elif player == 2:
            text('Score ' + str(score2), 40, 170)
        elif player == 3:
            text('Score ' + str(score3), 40, 170)
        elif player == 4:
            text('Score ' + str(score4), 40, 170)
        elif player == 5:
            text('Score ' + str(score5), 40, 170)
        elif player == 6:
            text('Score ' + str(score6), 40, 170)
        
        text('Information', 400, 150)
        text('Return', 870, 150)
        fill(255,255,255)
        rect(40, 190, 600, 550)
        textSize(42)
        text('Buy menu', 40, 80)
        textSize(12)
        
        '''
        #################coordinates of items in buy menu---- Ayub
        '''
        image(img, 650, 200, 100, 100)
        text('Item 1', 655, 215)
        text('Price = 200', 655, 235)

        '''
        ############item 2
        '''

        image(img, 850, 200, 100, 100)
        text('Item 2', 855, 215)
        text('Price = 200', 855, 235)
        '''
        ###############item 3
        '''
        image(img, 650, 340, 100, 100)
        text('Item 3', 655, 355)
        text('Price = 250', 655, 365)
        '''
        ############item 4
        '''
        image(img, 850, 340, 100, 100)
        text('Item 4', 855, 355)
        text('Price = 500', 855, 365)
        '''
        ############item 5
        '''
        image(img, 650, 480, 100, 100)
        text('Item 5', 655, 495)
        text('Price = 400', 655, 505)
        '''
        ##############item 6
        '''
        image(img, 850, 480, 100, 100)
        text('Item 6', 855, 495)
        text('Price = 400', 855, 505)
        '''
        ##############item 7
        '''
        image(img, 650, 620, 100, 100)
        text('Item 7', 655, 635)
        text('Price = 400', 655, 645)
        '''
        ##############item 8
        '''
        image(img, 850, 620, 100, 100)
        text('Item 8', 855, 635)
        text('Price = 600', 855, 645)
        
        '''
        ################items in inventory---- Jingkit
        '''
        if player == 1:
            itemsInInventory1()
        elif player == 2:
            itemsInInventory2()
        elif player == 3:
            itemsInInventory3()
        elif player == 3:
            itemsInInventory3()            
        elif player == 4:
            itemsInInventory4()
        elif player == 5:
            itemsInInventory5()            
        elif player == 6:
            itemsInInventory6()     
            
        '''
        ############# information on items ---- ayub    
        '''

    elif screen == 5:
        background(achtergrond)
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 15, 970, 658) 
        fill(255,255,255)
        text('Return', 870, 150)
        textSize(50)
        text('INFORMATION ABOUT THE CARDS', 40, 80)  
        image(img, 100, 100, 100, 100)
        textSize(20)
        text('Item1', 110, 120)
        text('Take 1 step', 200, 190)
        image(img, 500, 100, 100, 100)
        text('Item2', 510, 120)
        text('Take 2 steps', 600, 190)
        image(img, 100, 210, 100, 100)
        text('Item3', 110, 230)
        text('Take 1 step', 200, 300)
        image(img, 500, 210, 100, 100)
        text('Item4', 510, 230)
        text('Take 6 steps', 600, 300)
        image(img, 100, 320, 100, 100)
        text('Item5', 110, 340)
        text('Take 3 steps', 200, 400)
        image(img, 500, 320, 100, 100)
        text('Item6', 510, 340)
        text('Take 4 steps', 600, 400)
        image(img, 100, 430, 100, 100)
        text('Item7', 110, 450)
        text('Take 5 steps', 200, 510)
        image(img, 500, 430, 100, 100)
        text('Item8', 510, 450)
        text('Take 6 steps', 600, 510)    
    
     

        
        

            
        
        

    if dice.diceIsOne == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img1 = loadImage("data/dice-1.png")
        image(img1, (width/4)*3.2, 500, 200, 200)

    if dice.diceIsTwo == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img2 = loadImage("data/dice-2.png")
        image(img2, (width/4)*3.2, 500, 200, 200)

    if dice.diceIsThree == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img3 = loadImage("data/dice-3.png")
        image(img3, (width/4)*3.2, 500, 200, 200)

    if dice.diceIsFour == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img4 = loadImage("data/dice-4.png")
        image(img4, (width/4)*3.2, 500, 200, 200)

    if dice.diceIsFive == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img5 = loadImage("data/dice-5.png")
        image(img5, (width/4)*3.2, 500, 200, 200)

    if dice.diceIsSix == True:
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        img6 = loadImage("data/dice-6.png")
        image(img6, (width/4)*3.2, 500, 200, 200)
    
        



    intersectionChoice = []
    if chooseRoute == True:
        if intersectionUp == True:
            intersectionChoice.append("up")
        if intersectionRight == True:
            intersectionChoice.append("right")
        if intersectionDown == True:
            intersectionChoice.append("down")
        if intersectionLeft == True:
            intersectionChoice.append("left")
        fill(255)
        rect((width/2)+200, (height*0.75)-100, 400, 200)
        fill(0)
        textSize(25)
        text('You can go ' + str(intersectionChoice[0]) + ' or ' + str(intersectionChoice[1]), (width/2)+250, (height*0.75)-50)
        text('Press ' + str(intersectionChoice[0][0]) + ' for ' + str(intersectionChoice[0]), (width/2)+250, (height*0.75)-10)
        text('Press ' + str(intersectionChoice[1][0]) + ' for ' + str(intersectionChoice[1]), (width/2)+250, (height*0.75)+30)
        textSize(11)
        

    if mcqEvent == True:
        global qst, y, vraag, answer

        qst = {q1:"a",q2:"b",q3:"b",q4:"c",q5:"d",q6:"d",q7:"a"}

        stroke(0)
        fill(255,255,0)
        rect((width/2)+200, (height*0.75)-100,400,200)

        while mcqIterator > 0:
            y = randrange(len(qst))
            vraag = list(qst.keys())[y]
            answer = list(qst.values())[y]
            mcqIterator -= 1

        f = createFont("Arial", 20, True)
        textFont(f,10)
        fill(0)          
        text(vraag,(width/2)+225, (height*0.75)-75)

        if checkAnswer ==  True:
            removeMCQ = True
            if check == True:
                fill(0,255,0)
                rect((width/2)+200, (height*0.75)-100,400,200)
                fill(255)
                textSize(45)
                text("Correct",(width/2)+325, (height*0.75)+15)
                textSize(20)
                fill(0)
                text("Press 'k' to continue",(width/2)+325, (height*0.75)+45)
                textSize(12)
            elif check == False:
                fill(255,0,0)
                rect((width/2)+200, (height*0.75)-100,400,200)
                fill(255)
                textSize(45)
                text("Wrong",(width/2)+325, (height*0.75)+15)
                textSize(20)
                fill(0)
                text("Press 'k' to continue",(width/2)+325, (height*0.75)+45)
                textSize(12)

    
    
    if redTileEvent == True:
        fill(255,0,0)
        rect((width/2)+200, (height*0.75)-100,400,200)
        fill(255)
        textSize(45)
        while redTileIterator == True:
            z = randrange(4)
            redTileIterator = False
            redTileMove = redTiles[z][1]
        text(str(redTiles[z][0]),(width/2)+250, (height*0.75)+15)
        textSize(20)
        fill(0)
        text("Press 'k' to continue",(width/2)+285, (height*0.75)+45)
        textSize(12)

        '''
        # dit zijn alle keybindings

        # pijltje omhoog = 38
        # pijltje omlaag = 40
        # pijltje naar links = 37
        # pijltje naar rechts = 39
        '''
    
    elif screen == 7:
        background(achtergrondwinscreen)
        textSize(36)
        if players == 2:
            text(playerWinList[0], 450, 90)
            text(playerWinList[1], 450, 180)
        elif players == 3:
            text(playerWinList[0], 450, 90)
            text(playerWinList[1], 450, 180)
            text(playerWinList[2], 450, 270)
        elif players == 4:
            text(playerWinList[0], 450, 90)
            text(playerWinList[1], 450, 180)
            text(playerWinList[2], 450, 270)
            text(playerWinList[3], 450, 360)
        elif players == 5:
            text(playerWinList[0], 450, 90)
            text(playerWinList[1], 450, 180)
            text(playerWinList[2], 450, 270)
            text(playerWinList[3], 450, 360)
            text(playerWinList[4], 450, 450)
        elif players == 6:
            text(playerWinList[0], 450, 90)
            text(playerWinList[1], 450, 180)
            text(playerWinList[2], 450, 270)
            text(playerWinList[3], 450, 360)
            text(playerWinList[4], 450, 450)
            text(playerWinList[5], 450, 540)


playermovement = 0
def keyPressed():
    print(key,keyCode)
    
    global playermovement, posxp1, posyp1, posxp2, posyp2, posxp3, posyp3, posxp4, posyp4, posxp5, posyp5, posxp6, posyp6
    global player1, player2, player3, player4, player5, player6, currentPlayer, playerIntersectionChoice, mcqEvent, mcqIterator
    global answer, vraag, check, checkAnswer, score, score2, score3, score4, score5, score6, timesAnswered
    global redTileEvent, redTileMove, grid, playerWinList, screen
    if key == "=":
        print(playerWinList, players)
    if key == '/':
        grid = not grid

    ''' Controls which characters are selectable '''
    if mcqEvent == False and chooseRoute == False and redTileEvent == False:
        if keyCode == 49:
            # playermovement = 1
            currentPlayer = player1
        if keyCode == 50:
            # playermovement = 2
            currentPlayer = player2
        if players > 2:
            if keyCode == 51:
                # playermovement = 3
                currentPlayer = player3
            if players > 3:
                if keyCode == 52:
                    # playermovement = 4
                    currentPlayer = player4
                if players > 4:
                    if keyCode == 53:
                        # playermovement = 5
                        currentPlayer = player5
                    if players > 5:
                        if keyCode == 54:
                            # playermovement = 6
                            currentPlayer = player6
    '''Dit is de handmatige manier van bewegen. met de toetsen 1,2,3,4,5, en 6 kun je een speler selecteren. vervolgens gebruik je de pijltjestoetsen om hem te bewegen. '''
    '''
    if playermovement == 1: 
        if keyCode == 38:
            posyp1 -= stapje
        if keyCode == 40:
            posyp1 += stapje
        if keyCode == 37:
            posxp1 -= stapje
        if keyCode == 39:
            posxp1 += stapje     

    if playermovement == 2: 
        if keyCode == 38:
            posyp2 -= stapje
        if keyCode == 40:
            posyp2 += stapje
        if keyCode == 37:
            posxp2 -= stapje
        if keyCode == 39:
            posxp2 += stapje
        
    if playermovement == 3: 
        if keyCode == 38:
            posyp3 -= stapje
        if keyCode == 40:
            posyp3 += stapje
        if keyCode == 37:
            posxp3 -= stapje
        if keyCode == 39:
            posxp3 += stapje
        
    if playermovement == 4: 
        if keyCode == 38:
            posyp4 -= stapje
        if keyCode == 40:
            posyp4 += stapje
        if keyCode == 37:
            posxp4 -= stapje
        if keyCode == 39:
            posxp4 += stapje
        
    if playermovement == 5: 
        if keyCode == 38:
            posyp5 -= stapje
        if keyCode == 40:
            posyp5 += stapje
        if keyCode == 37:
            posxp5 -= stapje
        if keyCode == 39:
            posxp5 += stapje
        
    if playermovement == 6: 
        if keyCode == 38:
            posyp6 -= stapje
        if keyCode == 40:
            posyp6 += stapje
        if keyCode == 37:
            posxp6 -= stapje
        if keyCode == 39:
            posxp6 += stapje
    
    '''
    if mcqEvent == True:
        if timesAnswered == 0:
            if key in possibleAnswerList:
                if key == answer:
                    checkAnswer = True
                    check = True
                    if currentPlayer[-2] == "player1":
                        score += 200
                    elif currentPlayer[-2] == "player2":
                        score2 += 200
                    elif currentPlayer[-2] == "player3":
                        score3 += 200
                    elif currentPlayer[-2] == "player4":
                        score4 += 200
                    elif currentPlayer[-2] == "player5":
                        score5 += 200
                    elif currentPlayer[-2] == "player6":
                        score6 += 200
                elif key != answer:
                    checkAnswer = True
                    check = False
                timesAnswered += 1
        if timesAnswered > 0:
            if key == 'k':
                resetMCQBooleans()
        
    
    if redTileEvent == True:
        if key == 'k':
            resetRedTileBooleans()
            movePlayerBackwards(redTileMove, currentPlayer, cDictBackwards)

    if key == ' ' and mcqEvent == False and chooseRoute == False and redTileEvent == False and currentPlayer != playerNone:
        dice.diceIsOne, dice.diceIsTwo, dice.diceIsThree, dice.diceIsFour, dice.diceIsFive, dice.diceIsSix = False, False, False, False, False, False
        movementIterator = dice.rollDice()
        movementIterator = 20
        while movementIterator > 0 and chooseRoute == False: 
            movePlayer(1, currentPlayer, cDict)
            print(movementIterator, chooseRoute)
            movementIterator -= 1
            currentPlayerEventTileCheck = currentPlayer[-1]
            if cDictEvents[currentPlayerEventTileCheck] == ["finish"]:
                movementIterator = 0
                if currentPlayer[-2] == "player1":
                    player1Finished = True
                    playerWinList.append("Player 1")
                    print('wtf1')
                elif currentPlayer[-2] == "player2":
                    player2Finished = True
                    playerWinList.append("Player 2")
                    print('wtf2')
                elif currentPlayer[-2] == "player3":
                    player3Finished = True
                    playerWinList.append("Player 3")
                elif currentPlayer[-2] == "player4":
                    player4Finished = True
                    playerWinList.append("Player 4")
                elif currentPlayer[-2] == "player5":
                    player5Finished = True
                    playerWinList.append("Player 5")
                elif currentPlayer[-2] == "player6":
                    player6Finished = True
                    playerWinList.append("Player 6")
                currentPlayer = playerNone
                if len(playerWinList) == players:
                    print("klaar")
                    screen = 7
            elif movementIterator == 0:
                if cDictEvents[currentPlayerEventTileCheck] == ["mcq"]:
                    print("MCQ Tile")
                    mcqEvent = True
                elif cDictEvents[currentPlayerEventTileCheck] == ["red"]:
                    print("Red Tile")
                    redTileEvent = True

        # yall 

    if chooseRoute == True:
        ''' print(intersectionDown, intersectionUp, intersectionLeft, intersectionRight) '''
        if intersectionUp == True:
            if key == "u":
                print(" You pressed u for up" )
                playerIntersectionChoice = ["up"]
                movePlayerInDirection(currentPlayer, playerIntersectionChoice)
                clearPlayerIntersectionChoice()

                currentPlayerEventTileCheck = currentPlayer[-1]
                if cDictEvents[currentPlayerEventTileCheck] == ["mcq"]:
                    print("MCQ Tile")
                    mcqEvent = True
                elif cDictEvents[currentPlayerEventTileCheck] == ["red"]:
                    print("Red Tile")
                    redTileEvent = True

        if intersectionRight == True:
            if key == "r":
                print("You pressed R for right")
                playerIntersectionChoice = ["right"]
                movePlayerInDirection(currentPlayer, playerIntersectionChoice)
                clearPlayerIntersectionChoice()

                currentPlayerEventTileCheck = currentPlayer[-1]
                if cDictEvents[currentPlayerEventTileCheck] == ["mcq"]:
                    print("MCQ Tile")
                    mcqEvent = True
                elif cDictEvents[currentPlayerEventTileCheck] == ["red"]:
                    print("Red Tile")
                    redTileEvent = True

        if intersectionDown == True:
            if key == "d":
                print(" You pressed D for down" )
                playerIntersectionChoice = ["down"]
                movePlayerInDirection(currentPlayer, playerIntersectionChoice) 
                clearPlayerIntersectionChoice()

                currentPlayerEventTileCheck = currentPlayer[-1]
                if cDictEvents[currentPlayerEventTileCheck] == ["mcq"]:
                    print("MCQ Tile")
                    mcqEvent = True
                elif cDictEvents[currentPlayerEventTileCheck] == ["red"]:
                    print("Red Tile")
                    redTileEvent = True

        if intersectionLeft == True:
            if key == "l":
                print(" You pressed L for left" )
                playerIntersectionChoice = ["left"]
                movePlayerInDirection(currentPlayer, playerIntersectionChoice)
                clearPlayerIntersectionChoice()

                currentPlayerEventTileCheck = currentPlayer[-1]
                if cDictEvents[currentPlayerEventTileCheck] == ["mcq"]:
                    print("MCQ Tile")
                    mcqEvent = True
                elif cDictEvents[currentPlayerEventTileCheck] == ["red"]:
                    print("Red Tile")
                    redTileEvent = True



''' Returns all intersection related boolean values to False '''
def clearPlayerIntersectionChoice():
    global intersectionUp, intersectionRight, intersectionDown, intersectionLeft, chooseRoute, playerIntersectionChoice
    intersectionUp, intersectionRight, intersectionDown, intersectionLeft, chooseRoute = False, False, False, False, False
    playerIntersectionChoice = ''

''' Returns all MCQ related boolean values to False '''
def resetMCQBooleans():
    global answer, checkAnswer, mcqEvent, removeMCQ, mcqIterator, timesAnswered
    answer, checkAnswer, mcqEvent, removeMCQ = False, False, False, False
    mcqIterator, timesAnswered = 1, 0

''' Returns all RedTile related boolean values to False '''
def resetRedTileBooleans():
    global redTileEvent, redTileIterator
    redTileEvent = False
    redTileIterator = 1

''' Function which moves the player on a grid according to the direction it is given. Parameters are the rolled dice and the currently rolling player.'''
def movePlayer(rolledDice, player, cDict):
    global player1, player2, player3, player4, player5, player6, chooseRoute, intersectionUp, intersectionRight, intersectionDown, intersectionLeft
    i = 0
    playerDirection = player[2]

    while rolledDice > 0 and chooseRoute == False:
        '''takes the player location on the grid, [-1] for the coordinates in string'''
        tileDirection = cDict[player[-1]]

        '''Checks if there is a tile direction. If not, uses the players own stored direction to call the movePlayer function.'''
        if len(tileDirection) == 0:
            playerDirection = player[2]
            movePlayerInDirection(player, playerDirection)
        
        '''Checks if there is one tile direction. If so, uses the tile direction to call the movePlayer function.'''
        if len(tileDirection) == 1:
            playerDirection = tileDirection
            #player[2] = tileDirection
            movePlayerInDirection(player, playerDirection)
        
        '''Checks if there are two tile directions. If so, calls the intersection choice function'''
        if len(tileDirection) == 2:
            chooseRoute = True
            if ["up"] in tileDirection:
                intersectionUp = True
            if ["right"] in tileDirection:
                intersectionRight = True
            if ["down"] in tileDirection:
                intersectionDown = True
            if ["left"] in tileDirection:
                intersectionLeft = True

        '''if player reaches the last tile with the given coordinates, the player wins'''

        rolledDice -= 1





def movePlayerBackwards(redTileMove, player, cDictBackwards):
    global player1, player2, player3, player4, player5, player6

    redTileMoveCache = redTileMove

    while redTileMove > 0:

        tileDirectionBackwards = cDictBackwards[player[-1]]


        if redTileMoveCache == redTileMove:
            if tileDirectionBackwards:
                playerDirection = tileDirectionBackwards
                movePlayerInDirection(player, playerDirection)
            else:
                playerDirection = player[2]
                if playerDirection == ["up"]:
                    playerDirection = ["down"]
                elif playerDirection == ["right"]:
                    playerDirection = ["left"]
                elif playerDirection == ["down"]:
                    playerDirection = ["up"]
                elif playerDirection == ["left"]:
                    playerDirection = ["right"]
                
                movePlayerInDirection(player, playerDirection)
        else:
            if tileDirectionBackwards:
                playerDirection = tileDirectionBackwards
                movePlayerInDirection(player, playerDirection)
            else:
                print(player, playerDirection, 'lol')
                movePlayerInDirection(player, playerDirection)
            if redTileMove == 1:
                if playerDirection == ["up"]:
                    playerDirection = ["down"]
                elif playerDirection == ["right"]:
                    playerDirection = ["left"]
                elif playerDirection == ["down"]:
                    playerDirection = ["up"]
                elif playerDirection == ["left"]:
                    playerDirection = ["right"]
                player[2] = playerDirection
        redTileMove -= 1





''' Moves the players coordinates to the given direction '''
def movePlayerInDirection(player, playerDirection):
    ''' print(playerDirection, player)'''
    if playerDirection == ["up"]:
        player[1] -= 1
    elif playerDirection == ["right"]:
        player[0] += 1
    elif playerDirection == ["down"]:
        player[1] += 1
    elif playerDirection == ["left"]:
        player[0] -= 1
    else:
        print("Er is geen player direction")
    player[-1] = str(player[0]) + ", " + str(player[1])
    player[2] = playerDirection
    ''' print(player, "<- Print player [X, Y, [dir], XY in string]") '''
    movePlayerChar(player, playerDirection)

''' Moves the players goose figure to the given direction '''
def movePlayerChar(player, playerDirection):
    global posxp1, posyp1, posxp2, posyp2, posxp3, posyp3, posxp4, posyp4, posxp5, posyp5, posxp6, posyp6
    # playerDirection = player[2]
    stapje = 33
    if player[3] == "player1":
        if playerDirection == ['up']:
            posyp1 -= stapje
        if playerDirection == ['right']:
            posxp1 += stapje
        if playerDirection == ['down']:
            posyp1 += stapje
        if playerDirection == ['left']:
            posxp1 -= stapje
    if player[3] == "player2":
        if playerDirection == ['up']:
            posyp2 -= stapje
        if playerDirection == ['right']:
            posxp2 += stapje
        if playerDirection == ['down']:
            posyp2 += stapje
        if playerDirection == ['left']:
            posxp2 -= stapje
    if player[3] == "player3":
        if playerDirection == ['up']:
            posyp3 -= stapje
        if playerDirection == ['right']:
            posxp3 += stapje
        if playerDirection == ['down']:
            posyp3 += stapje
        if playerDirection == ['left']:
            posxp3 -= stapje
    if player[3] == "player4":
        if playerDirection == ['up']:
            posyp4 -= stapje
        if playerDirection == ['right']:
            posxp4 += stapje
        if playerDirection == ['down']:
            posyp4 += stapje
        if playerDirection == ['left']:
            posxp4 -= stapje
    if player[3] == "player5":
        if playerDirection == ['up']:
            posyp5 -= stapje
        if playerDirection == ['right']:
            posxp5 += stapje
        if playerDirection == ['down']:
            posyp5 += stapje
        if playerDirection == ['left']:
            posxp5 -= stapje
    if player[3] == "player6":
        if playerDirection == ["up"]:
            posyp6 -= stapje
        if playerDirection == ["right"]:
            posxp6 += stapje
        if playerDirection == ["down"]:
            posyp6 += stapje
        if playerDirection == ["left"]:
            posxp6 -= stapje


''' hier is de functionaliteit van de muis '''
def mousePressed():
    global screen, players, playerInventory, score, inventoryDict, player, score2, score3, score4, score5, score6
    '''
    ###############Choose Players---- Jingkit
    '''
    if screen == 1 and 286 < mouseX < 486 and 160 < mouseY < 360:
        screen = 2
        players = 2
    if screen == 1 and 586 < mouseX < 786 and 160 < mouseY < 360:
        screen = 2
        players = 3
    if screen == 1 and 886 < mouseX < 1086 and 160 < mouseY < 360:
        screen = 2
        players = 4
    if screen == 1 and 433 < mouseX < 633 and 400 < mouseY < 600:
        screen = 2
        players = 5
    if screen == 1 and 736 < mouseX < 936 and 400 < mouseY < 600:
        screen = 2
        players = 6

    '''
    ######################Choosing whitch inventory to open---- Jingkit
    '''

    if screen == 2 and 20 < mouseX < 120 and 600 < mouseY < 700:
        screen = 3
        player = 1
        
    if screen == 2 and 140 < mouseX < 240 and 600 < mouseY < 700:
        screen = 3
        player = 2
        
    if players > 2:
        if screen == 2 and 260 < mouseX < 360 and 600 < mouseY < 700:
            screen = 3
            player = 3

    if players > 3:
        if screen == 2 and 390 < mouseX < 490 and 600 < mouseY < 700:
            screen = 3
            player = 4

    if players > 4:
        if screen == 2 and 510 < mouseX < 610 and 600 < mouseY < 700:
            screen = 3 
            player = 5
        
    if players > 5:
        if screen == 2 and 630 < mouseX < 730 and 600 < mouseY < 700:
            screen = 3
            player= 6
    '''
    ##################Return button---- Ayub
    '''
    if screen == 3 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 2
        textSize(12)
    if screen == 5 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 4
    '''
    #####################Open buy menu
    '''
    if screen == 3 and 900 < mouseX < 970 and 10 < mouseY < 100:
        screen = 4
    '''
    #####################Return button
    '''
    if screen == 4 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 3
    '''
    ####################to screen 5 400, 150
    '''
    if screen == 4 and 400 < mouseX < 580 and 100 < mouseY < 170:
        screen = 5

    '''
    ###################Score deduction and buying items in inventory---- Jingkit
    '''

    if screen == 4 and mouseOnItem1Shop() == True:
        if player == 1:
            if score >= 200 and inventoryDict['item1'] < 1:
                inventoryDict['item1'] += 1
                score -= 200
        elif player == 2:
            if score2 >= 200 and inventoryDict2['item1'] < 1:
                inventoryDict2['item1'] += 1
                score2 -= 200
        elif player == 3:
            if score3 >= 200 and inventoryDict3['item1'] < 1:
                inventoryDict3['item1'] += 1
                score3 -= 200
        elif player == 4:
            if score4 >= 200 and inventoryDict4['item1'] < 1:
                inventoryDict4['item1'] += 1
                score4 -= 200
        elif player == 5:
            if score5 >= 200 and inventoryDict5['item1'] < 1:
                inventoryDict5['item1'] += 1
                score5 -= 200
        elif player == 6:
            if score6 >= 200 and inventoryDict6['item1'] < 1:
                inventoryDict6['item1'] += 1
                score6 -= 200
            
    if screen == 4 and mouseOnItem2Shop() == True:
        if player == 1:
            if score >= 200 and inventoryDict['item2'] < 1:
                inventoryDict['item2'] += 1
                score -= 200
        elif player == 2:
            if score2 >= 200 and inventoryDict2['item2'] < 1:
                inventoryDict2['item2'] += 1
                score2 -= 200
        elif player == 3:
            if score3 >= 200 and inventoryDict3['item2'] < 1:
                inventoryDict3['item2'] += 1
                score3 -= 200
        elif player == 4:
            if score4 >= 200 and inventoryDict4['item2'] < 1:
                inventoryDict4['item2'] += 1
                score4 -= 200
        elif player == 5:
            if score5 >= 200 and inventoryDict5['item2'] < 1:
                inventoryDict5['item2'] += 1
                score5 -= 200
        elif player == 6:
            if score6 >= 200 and inventoryDict6['item2'] < 1:
                inventoryDict6['item2'] += 1
                score6 -= 200
            
    if screen == 4 and mouseOnItem3Shop() == True:
        if player == 1:
            if score >= 250 and inventoryDict['item3'] < 1:
                inventoryDict['item3'] += 1
                score -= 250
        elif player == 2:
            if score2 >= 250 and inventoryDict2['item3'] < 1:
                inventoryDict2['item3'] += 1
                score2 -= 250
        elif player == 3:
            if score3 >= 250 and inventoryDict3['item3'] < 1:
                inventoryDict3['item3'] += 1
                score3 -= 250
        elif player == 4:
            if score4 >= 250 and inventoryDict4['item3'] < 1:
                inventoryDict4['item3'] += 1
                score4 -= 250
        elif player == 5:
            if score5 >= 250 and inventoryDict5['item3'] < 1:
                inventoryDict5['item3'] += 1
                score5 -= 250
        elif player == 6:
            if score6 >= 250 and inventoryDict6['item3'] < 1:
                inventoryDict6['item3'] += 1
                score6 -= 250
            
    if screen == 4 and mouseOnItem4Shop() == True:
        if player == 1:
            if score >= 500 and inventoryDict['item4'] < 1:
                inventoryDict['item4'] += 1
                score -= 500
        elif player == 2:
            if score2 >= 500 and inventoryDict2['item4'] < 1:
                inventoryDict2['item4'] += 1
                score2 -= 500
        elif player == 3:
            if score3 >= 500 and inventoryDict3['item4'] < 1:
                inventoryDict3['item4'] += 1
                score3 -= 500
        elif player == 4:
            if score4 >= 500 and inventoryDict4['item4'] < 1:
                inventoryDict4['item4'] += 1
                score4 -= 500
        elif player == 5:
            if score5 >= 500 and inventoryDict5['item4'] < 1:
                inventoryDict5['item4'] += 1
                score5 -= 500
        elif player == 6:
            if score6 >= 500 and inventoryDict6['item4'] < 1:
                inventoryDict6['item4'] += 1
                score6 -= 500
        
    if screen == 4 and mouseOnItem5Shop() == True:
        if player == 1:
            if score >= 400 and inventoryDict['item5'] < 1:
                inventoryDict['item5'] += 1
                score -= 400
        elif player == 2:
            if score2 >= 400 and inventoryDict2['item5'] < 1:
                inventoryDict2['item5'] += 1
                score2 -= 400
        elif player == 3:
            if score3 >= 400 and inventoryDict3['item5'] < 1:
                inventoryDict3['item5'] += 1
                score3 -= 400
        elif player == 4:
            if score4 >= 400 and inventoryDict4['item5'] < 1:
                inventoryDict4['item5'] += 1
                score4 -= 400
        elif player == 5:
            if score5 >= 400 and inventoryDict5['item5'] < 1:
                inventoryDict5['item5'] += 1
                score5 -= 400
        elif player == 6:
            if score6 >= 400 and inventoryDict6['item5'] < 1:
                inventoryDict6['item5'] += 1
                score6 -= 400
            
    if screen == 4 and mouseOnItem6Shop() == True:
        if player == 1:
            if score >= 400 and inventoryDict['item6'] < 1:
                inventoryDict['item6'] += 1
                score -= 400
        elif player == 2:
            if score2 >= 400 and inventoryDict2['item6'] < 1:
                inventoryDict2['item6'] += 1
                score2 -= 400
        elif player == 3:
            if score3 >= 400 and inventoryDict3['item6'] < 1:
                inventoryDict3['item6'] += 1
                score3 -= 400
        elif player == 4:
            if score4 >= 400 and inventoryDict4['item6'] < 1:
                inventoryDict4['item6'] += 1
                score4 -= 400
        elif player == 5:
            if score5 >= 400 and inventoryDict5['item6'] < 1:
                inventoryDict5['item6'] += 1
                score5 -= 400
        elif player == 6:
            if score6 >= 400 and inventoryDict6['item6'] < 1:
                inventoryDict6['item6'] += 1
                score6 -= 400

    if screen == 4 and mouseOnItem7Shop() == True:
        if player == 1:
            if score >= 400 and inventoryDict['item7'] < 1:
                inventoryDict['item7'] += 1
                score -= 400
        elif player == 2:
            if score2 >= 400 and inventoryDict2['item7'] < 1:
                inventoryDict2['item7'] += 1
                score2 -= 400
        elif player == 3:
            if score3 >= 400 and inventoryDict3['item7'] < 1:
                inventoryDict3['item7'] += 1
                score3 -= 400
        elif player == 4:
            if score4 >= 400 and inventoryDict4['item7'] < 1:
                inventoryDict4['item7'] += 1
                score4 -= 400
        elif player == 5:
            if score5 >= 400 and inventoryDict5['item7'] < 1:
                inventoryDict5['item7'] += 1
                score5 -= 400
        elif player == 6:
            if score6 >= 400 and inventoryDict6['item7'] < 1:
                inventoryDict6['item7'] += 1
                score6 -= 400
        
    if screen == 4 and mouseOnItem8Shop() == True:
        if player == 1:
            if score >= 600 and inventoryDict['item8'] < 1:
                inventoryDict['item8'] += 1
                score -= 600
        elif player == 2:
            if score2 >= 600 and inventoryDict2['item8'] < 1:
                inventoryDict2['item8'] += 1
                score2 -= 600
        elif player == 3:
            if score3 >= 600 and inventoryDict3['item8'] < 1:
                inventoryDict3['item8'] += 1
                score3 -= 600
        elif player == 4:
            if score4 >= 600 and inventoryDict4['item8'] < 1:
                inventoryDict4['item8'] += 1
                score4 -= 600
        elif player == 5:
            if score5 >= 600 and inventoryDict5['item8'] < 1:
                inventoryDict5['item8'] += 1
                score5 -= 600
        elif player == 6:
            if score6 >= 600 and inventoryDict6['item8'] < 1:
                inventoryDict6['item8'] += 1
                score6 -= 600
                
                '''
                ################## Using items in inventory ----- ayub
                '''
    global cDict
    # from playerMovement import movePlayer
    if screen == 3 and mouseOnItem1() == True:
        if player == 1:
            if inventoryDict['item1'] > 0: 
                inventoryDict['item1'] -= 1
                
                movePlayer(1, player1, cDict)
                '''
                movePlayerChar(player1)
                '''
                
                
        elif player == 2:
            if inventoryDict2['item1'] > 0: 
                inventoryDict2['item1'] -= 1
                
                movePlayer(1,player2, cDict)
                '''
                movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item1'] > 0: 
                inventoryDict3['item1'] -= 1
                
                movePlayer(1,player3, cDict)
                '''
                movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item1'] > 0: 
                inventoryDict4['item1'] -= 1
                
                movePlayer(1,player4, cDict)
                '''
                movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item1'] > 0: 
                inventoryDict5['item1'] -= 1
                
                movePlayer(1,player5, cDict)
                '''
                movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item1'] > 0: 
                inventoryDict6['item1'] -= 1
                
                movePlayer(1,player6, cDict)
                '''
                movePlayerChar(player6)
                '''
                
                    
    elif screen == 3 and mouseOnItem2() == True:
        if player == 1:
            if inventoryDict['item2'] > 0: 
                inventoryDict['item2'] -= 1
                
                movePlayer(2,player1, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player1)
                '''
                
                
        elif player == 2:
            if inventoryDict2['item2'] > 0: 
                inventoryDict2['item2'] -= 1
                
                movePlayer(2,player2, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item2'] > 0: 
                inventoryDict3['item2'] -= 1
                
                movePlayer(2,player3, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item2'] > 0: 
                inventoryDict4['item2'] -= 1
                
                movePlayer(2,player4, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item2'] > 0: 
                inventoryDict5['item2'] -= 1
                
                movePlayer(2,player5, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item2'] > 0: 
                inventoryDict6['item2'] -= 1
                
                movePlayer(2,player6, cDict)
                '''
                for i in range(2):
                    movePlayerChar(player6)
                '''
                
    elif screen == 3 and mouseOnItem3() == True:
        if player == 1:
            if inventoryDict['item3'] > 0: 
                inventoryDict['item3'] -= 1
                
                movePlayer(1,player1, cDict)
                '''
                movePlayerChar(player1)
                '''
                                
        elif player == 2:
            if inventoryDict2['item3'] > 0: 
                inventoryDict2['item3'] -= 1
                
                movePlayer(1,player2, cDict)
                '''
                movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item3'] > 0: 
                inventoryDict3['item3'] -= 1
                
                movePlayer(1,player3, cDict)
                '''
                movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item3'] > 0: 
                inventoryDict4['item3'] -= 1
                
                movePlayer(1,player4, cDict)
                '''
                movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item3'] > 0: 
                inventoryDict5['item3'] -= 1
                
                movePlayer(1,player5, cDict)
                '''
                movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item3'] > 0: 
                inventoryDict6['item3'] -= 1
                
                movePlayer(1,player6, cDict)
                '''
                movePlayerChar(player6)
                '''
            
                
    elif screen == 3 and mouseOnItem4() == True:
        if player == 1:
            if inventoryDict['item4'] > 0: 
                inventoryDict['item4'] -= 1
                
                movePlayer(6,player1, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player1)
                '''
                
        elif player == 2:
            if inventoryDict2['item4'] > 0: 
                inventoryDict2['item4'] -= 1
                
                movePlayer(6,player2, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item4'] > 0: 
                inventoryDict3['item4'] -= 1
                
                movePlayer(6,player3, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item4'] > 0: 
                inventoryDict4['item4'] -= 1
                
                movePlayer(6,player4, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item4'] > 0: 
                inventoryDict5['item4'] -= 1
                
                movePlayer(6,player5, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item4'] > 0: 
                inventoryDict6['item4'] -= 1
                
                movePlayer(6,player6, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player6)
                '''
                
                
    elif screen == 3 and mouseOnItem5() == True:
        if player == 1:
            if inventoryDict['item5'] > 0: 
                inventoryDict['item5'] -= 1
                
                movePlayer(3,player1, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player1)
                '''
                
        elif player == 2:
            if inventoryDict2['item5'] > 0: 
                inventoryDict2['item5'] -= 1
                
                movePlayer(3,player2, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item5'] > 0: 
                inventoryDict3['item5'] -= 1
                
                movePlayer(3,player3, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item5'] > 0: 
                inventoryDict4['item5'] -= 1
                
                movePlayer(3,player4, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item5'] > 0: 
                inventoryDict5['item5'] -= 1
                
                movePlayer(3,player5, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item5'] > 0: 
                inventoryDict6['item5'] -= 1
                
                movePlayer(3,player6, cDict)
                '''
                for i in range(3):
                    movePlayerChar(player6)
                '''
    
    elif screen == 3 and mouseOnItem6() == True:
        if player == 1:
            if inventoryDict['item6'] > 0: 
                inventoryDict['item6'] -= 1
                
                movePlayer(4,player1, cDict)
                '''
                for i in range(4):
                    movePlayerChar(player1)
                '''
                
        elif player == 2:
            if inventoryDict2['item6'] > 0: 
                inventoryDict2['item6'] -= 1
                
                movePlayer(4,player2, cDict)
                '''
                for i in range(4):
                    movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item6'] > 0: 
                inventoryDict3['item6'] -= 1
                
                movePlayer(4,player3, cDict)
                '''
                for i in range(4):
                    movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item6'] > 0: 
                inventoryDict4['item6'] -= 1
                
                movePlayer(4,player4, cDict)
                '''
                for i in range(4):
                    movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item6'] > 0: 
                inventoryDict5['item6'] -= 1
                
                movePlayer(4,player5, cDict)
                '''
                for i in range(4):
                    movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item6'] > 0: 
                inventoryDict6['item6'] -= 1
                
                movePlayer(4,player6, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player6)
                '''
    
    elif screen == 3 and mouseOnItem7() == True:
        if player == 1:
            if inventoryDict['item7'] > 0: 
                inventoryDict['item7'] -= 1
                
                movePlayer(5,player1, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player1)
                '''
                
        elif player == 2:
            if inventoryDict2['item7'] > 0: 
                inventoryDict2['item7'] -= 1
                
                movePlayer(5,player2, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player2)
                '''
                
        elif player == 3:
            if inventoryDict3['item7'] > 0: 
                inventoryDict3['item7'] -= 1
                
                movePlayer(5,player3, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player3)
                '''
                
        elif player == 4:
            if inventoryDict4['item7'] > 0: 
                inventoryDict4['item7'] -= 1
                
                movePlayer(5,player4, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player4)
                '''
                
        elif player == 5:
            if inventoryDict5['item7'] > 0: 
                inventoryDict5['item7'] -= 1
                
                movePlayer(5,player5, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player5)
                '''
                
        elif player == 6:
            if inventoryDict6['item7'] > 0: 
                inventoryDict6['item7'] -= 1 
                
                movePlayer(5,player6, cDict)
                '''
                for i in range(5):
                    movePlayerChar(player6)
                '''
                
                
    elif screen == 3 and mouseOnItem8() == True:
        if player == 1:
            if inventoryDict['item8'] > 0: 
                inventoryDict['item8'] -= 1
                    
                movePlayer(6,player1, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player1)
                '''
                    
        elif player == 2:
            if inventoryDict2['item8'] > 0: 
                inventoryDict2['item8'] -= 1
    
                movePlayer(6,player2, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player2)
                '''
                    
        elif player == 3:
            if inventoryDict3['item8'] > 0: 
                inventoryDict3['item8'] -= 1
                
                movePlayer(6,player3, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player3)
                '''
                    
        elif player == 4:
            if inventoryDict4['item8'] > 0: 
                inventoryDict4['item8'] -= 1
                
                movePlayer(6,player4, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player4)
                '''
                    
        elif player == 5:
            if inventoryDict5['item8'] > 0: 
                inventoryDict5['item8'] -= 1
    
                movePlayer(6,player5, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player5)
                '''
                    
        elif player == 6:
            if inventoryDict6['item8'] > 0: 
                inventoryDict6['item8'] -= 1
    
                movePlayer(6,player6, cDict)
                '''
                for i in range(6):
                    movePlayerChar(player6)
                '''

''' Mouse on item in shop ----- Jingkit '''                                                                                                                          
def mouseOnItem1Shop():
    if 650 < mouseX < 750 and 200 < mouseY < 300:
        return True
    else: 
        return False
    
def mouseOnItem2Shop():
    if 850 < mouseX < 950 and 200 < mouseY < 300:
        return True
    else: 
        return False
    
def mouseOnItem3Shop():
    if 650 < mouseX < 750 and 340 < mouseY < 440:
        return True
    else: 
        return False
    
def mouseOnItem4Shop():
    if 850 < mouseX < 950 and 340 < mouseY < 440:
        return True
    else: 
        return False

def mouseOnItem5Shop():
    if 650 < mouseX < 750 and 480 < mouseY < 580:
        return True
    else: 
        return False
    
def mouseOnItem6Shop():
    if 850 < mouseX < 950 and 480 < mouseY < 580:
        return True
    else: 
        return False    
    
def mouseOnItem7Shop():
    if 650 < mouseX < 750 and 620 < mouseY < 720:
        return True
    else: 
        return False    
    
def mouseOnItem8Shop():
    if 850 < mouseX < 950 and 620 < mouseY < 720:
        return True
    else: 
        return False
    
''' The visual aspect of the items ------ Jingkit '''

def itemsInInventory1():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict['item1']), 205, 290)
    text('x' + str(inventoryDict['item2']), 505, 290)           
    text('x' + str(inventoryDict['item3']), 205, 430)         
    text('x' + str(inventoryDict['item4']), 505, 430)      
    text('x' + str(inventoryDict['item5']), 205, 570)         
    text('x' + str(inventoryDict['item6']), 505, 570)          
    text('x' + str(inventoryDict['item7']), 205, 710)
    text('x' + str(inventoryDict['item8']), 505, 710)
    
def itemsInInventory2():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict2['item1']), 205, 290)
    text('x' + str(inventoryDict2['item2']), 505, 290)           
    text('x' + str(inventoryDict2['item3']), 205, 430)         
    text('x' + str(inventoryDict2['item4']), 505, 430)      
    text('x' + str(inventoryDict2['item5']), 205, 570)         
    text('x' + str(inventoryDict2['item6']), 505, 570)          
    text('x' + str(inventoryDict2['item7']), 205, 710)
    text('x' + str(inventoryDict2['item8']), 505, 710)

def itemsInInventory3():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict3['item1']), 205, 290)
    text('x' + str(inventoryDict3['item2']), 505, 290)           
    text('x' + str(inventoryDict3['item3']), 205, 430)         
    text('x' + str(inventoryDict3['item4']), 505, 430)      
    text('x' + str(inventoryDict3['item5']), 205, 570)         
    text('x' + str(inventoryDict3['item6']), 505, 570)          
    text('x' + str(inventoryDict3['item7']), 205, 710)
    text('x' + str(inventoryDict3['item8']), 505, 710)

def itemsInInventory4():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict4['item1']), 205, 290)
    text('x' + str(inventoryDict4['item2']), 505, 290)           
    text('x' + str(inventoryDict4['item3']), 205, 430)         
    text('x' + str(inventoryDict4['item4']), 505, 430)      
    text('x' + str(inventoryDict4['item5']), 205, 570)         
    text('x' + str(inventoryDict4['item6']), 505, 570)          
    text('x' + str(inventoryDict4['item7']), 205, 710)
    text('x' + str(inventoryDict4['item8']), 505, 710)
    
def itemsInInventory5():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict5['item1']), 205, 290)
    text('x' + str(inventoryDict5['item2']), 505, 290)           
    text('x' + str(inventoryDict5['item3']), 205, 430)         
    text('x' + str(inventoryDict5['item4']), 505, 430)      
    text('x' + str(inventoryDict5['item5']), 205, 570)         
    text('x' + str(inventoryDict5['item6']), 505, 570)          
    text('x' + str(inventoryDict5['item7']), 205, 710)
    text('x' + str(inventoryDict5['item8']), 505, 710)
    
def itemsInInventory6():
    textSize(12)
    image(img, 100, 200, 100, 100)
    text('Item 1', 105, 215)
    
    image(img, 400, 200, 100, 100)
    text('Item 2', 405, 215)
    
    image(img, 100, 340, 100, 100)
    text('Item 3', 105, 355)
    
    image(img, 400, 340, 100, 100)
    text('Item 4', 405, 355)
    
    image(img, 100, 480, 100, 100)
    text('Item 5', 105, 495)
    
    image(img, 400, 480, 100, 100)
    text('Item 6', 405, 495)
    
    image(img, 100, 620, 100, 100)
    text('Item 7', 105, 635)
    
    image(img, 400, 620, 100, 100)
    text('Item 8', 405, 635)
    
    fill(0)
    textSize(30)
    text('x' + str(inventoryDict6['item1']), 205, 290)
    text('x' + str(inventoryDict6['item2']), 505, 290)           
    text('x' + str(inventoryDict6['item3']), 205, 430)         
    text('x' + str(inventoryDict6['item4']), 505, 430)      
    text('x' + str(inventoryDict6['item5']), 205, 570)         
    text('x' + str(inventoryDict6['item6']), 505, 570)          
    text('x' + str(inventoryDict6['item7']), 205, 710)
    text('x' + str(inventoryDict6['item8']), 505, 710)
    
''' Mouse on item in inventory ----- ayub '''

def mouseOnItem1():
    global screen, players, playerInventory, score, inventoryDict, player, allItems
    if 100 < mouseX < 200 and 200 < mouseY < 300:
        return True
    else: 
        return False 
def mouseOnItem2():
    if 400 < mouseX < 500 and 200 < mouseY < 300:
        return True
    else: 
        return False 
def mouseOnItem3():
    if 100 < mouseX < 200 and 340 < mouseY < 440:
        return True
    else: 
        return False 
def mouseOnItem4():
    if 400 < mouseX < 500 and 340 < mouseY < 440:
        return True
    else: 
        return False 
def mouseOnItem5():
    if 100 < mouseX < 200 and 480 < mouseY < 580:
        return True
    else: 
        return False 
def mouseOnItem6():
    if 400 < mouseX < 500 and 480 < mouseY < 580:
        return True
    else: 
        return False 
def mouseOnItem7():
    if 100 < mouseX < 200 and 620 < mouseY < 720:
        return True
    else: 
        return False 
def mouseOnItem8():
    if 400 < mouseX < 500 and 620 < mouseY < 720:
        return True
    else: 
        return False 
    
    


    

def rollButtons(): # dice text box
    fill(255, 255, 255)
    rect((width/4)*3.2, 700, 200, 50)
    fill(0, 0, 0)
    textSize(12)
    text('Select a player with the', (width/4)*3.31, 715)
    text('keyboard numerical keys', (width/4)*3.29, 730)
    text('and press Space to roll', (width/4)*3.31, 745)
    # pass

def dice(): #the right dice
    fill(255, 255, 255)
    rect((width/4)*3.2, 500, 200, 200)


def rollDice():
    global player, diceIsOne, diceIsTwo, diceIsThree, diceIsFour, diceIsFive, diceIsSix
    rolledDice = int(random(1, 7))
    print(rolledDice)
    if rolledDice == 1:
        diceIsOne = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img1
        img1 = loadImage("data/dice-1.png")
        image(img1, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 2:
        diceIsTwo = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img2
        img2 = loadImage("data/dice-2.png")
        image(img2, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 3:
        diceIsThree = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img3
        img3 = loadImage("data/dice-3.png")
        image(img3, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 4:
        diceIsFour = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img4
        img4 = loadImage("data/dice-4.png")
        image(img4, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 5:
        diceIsFive = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img5
        img5 = loadImage("data/dice-5.png")
        image(img5, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 6:
        diceIsSix = True
        fill(255, 255, 255)
        rect((width/4)*3.2, 500, 200, 200)
        global img6
        img6 = loadImage("data/dice-6.png")
        image(img6, (width/4)*3.2, 500, 200, 200)
    return rolledDice
'''
def setup():
    dice()

def draw():
    rollButtons()

def keyPressed():
    if key == ' ': #right button coordinates
        rollDice()
'''

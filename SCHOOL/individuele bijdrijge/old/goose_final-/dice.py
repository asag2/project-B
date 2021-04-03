def rollButtons(): # dice text box
    fill(255, 255, 255)
    #rectMode(CENTER)
    rect((width/4)*3.2, 700, 200, 50)
    fill(0, 0, 0)
    # textSize(20)
    #textAlign(CENTER)
    text('Select a player with the', (width/4)*3.33, 715)
    text('keyboard numerical keys', (width/4)*3.31, 730)
    text('and press Space to roll', (width/4)*3.33, 745)
    # pass

def dice(): #the right dice
    fill(255, 255, 255)
    #rectMode(CENTER)
    rect((width/4)*3.2, 500, 200, 200)
    global img6
    img6 = loadImage("data/dice-6.png")
    #imageMode(CENTER)
    image(img6, (width/4)*3.2, 500, 200, 200)
    # pass

def rollDice():
    global player
    rolledDice = int(random(1, 7))
    if rolledDice == 1:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img1
        img1 = loadImage("data/dice-1.png")
        #imageMode(CENTER)
        image(img1, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 2:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img2
        img2 = loadImage("data/dice-2.png")
        #imageMode(CENTER)
        image(img2, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 3:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img3
        img3 = loadImage("data/dice-3.png")
        #imageMode(CENTER)
        image(img3, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 4:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img4
        img4 = loadImage("data/dice-4.png")
        #imageMode(CENTER)
        image(img4, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 5:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img5
        img5 = loadImage("data/dice-5.png")
        #imageMode(CENTER)
        image(img5, (width/4)*3.2, 500, 200, 200)
    if rolledDice == 6:
        fill(255, 255, 255)
        #rectMode(CENTER)
        rect((width/4)*3.2, 500, 200, 200)
        global img6
        img6 = loadImage("data/dice-6.png")
        #imageMode(CENTER)
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

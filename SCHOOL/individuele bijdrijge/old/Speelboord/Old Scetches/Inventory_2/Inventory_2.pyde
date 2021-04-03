screen = 1
playeramount = 0
playerOneInventory = ''
playerTwoInventory = ''
playerThreeInventory = ''
playerFourInventory = ''

def setup():
    global twoplayers
    global threeplayers
    global fourplayers
    size(1000, 800)
    twoplayers = loadImage('twoplayers.PNG')
    threeplayers = loadImage('threeplayers.png')
    fourplayers = loadImage('fourplayers.png')
    
def draw():
    global twoplayers
    global threeplayers
    global fourplayers
    global playeramount
    global screen
    
    background(0)
    rect(100, 150, 200, 200)
    rect(400, 150, 200, 200)
    rect(700, 150, 200, 200)
    image(twoplayers, 110, 160, 180, 180)
    image(threeplayers, 410, 160, 180, 180)
    image(fourplayers, 710, 160, 180, 180)
    
    if screen == 2:
        background(0)
        fill(169,169,169)
        rect(15, 100, 970, 680)
        fill(255,255,255)
        textSize(55)
        text('Inventory', 40, 80)
        inventory = 1
        inventoryX = 40
        inventoryY = 200
        plus = '+'
        
        while inventory <= playeramount and inventory < 7:
            fill(255,255,255)
            rect(inventoryX, inventoryY, 200, 500)
            ellipse(inventoryX + 100, inventoryY + 540, 40, 40)
            fill(0,0,0)
            textSize(32)
            text(plus, inventoryX + 87.5, inventoryY + 549)
            fill(255,255,255)
            text('Player ' + str(inventory), inventoryX + 40, inventoryY - 20)
            inventoryX = inventoryX + 240
            inventory = inventory + 1
            
    if screen == 3:
        background(0)
        fill(169,169,169)
        rect(15, 300, 970, 480)
        lands = 0
        landsX = 150
        landsY = 400
        textSize(32)
        plus = '+'
        fill(255,255,255)
        text('Back', 30, 340)
        
        while lands < 10:
            if lands == 5:
                landsX = 150
                landsY = 600
            fill(255,255,255)
            rect(landsX, landsY, 100, 100)
            ellipse(landsX + 50, landsY + 130, 40, 40)
            fill(0,0,0)
            text(plus, landsX + 37.5, landsY + 140)
            landsX = landsX + 150
            lands = lands + 1
            
def mousePressed():
    global screen
    global playeramount
    if screen == 1 and 100 < mouseX < 300 and 160 < mouseY < 360:
        screen = 2
        playeramount = 2
    if screen == 1 and 400 < mouseX < 600 and 160 < mouseY < 360:
        screen = 2
        playeramount = 3
    if screen == 1 and 700 < mouseX < 900 and 160 < mouseY < 360:
        screen = 2
        playeramount = 4
        
    if screen == 2 and 120 < mouseX < 160 and 720 < mouseY < 760:
        screen = 3
        playeradd = 1
    if screen == 2 and 360 < mouseX < 400 and 720 < mouseY < 760:
        screen = 3
        playeradd = 2
    if screen == 2 and 600 < mouseX < 640 and 720 < mouseY < 760:
        screen = 3
        playeradd = 3
    if screen == 2 and 840 < mouseX < 880 and 720 < mouseY < 760:
        screen = 3
        playeradd = 4
        
    if screen == 3 and 30 < mouseX < 100 and 320 < mouseY < 380:
        screen = 2

players = 0
player = 1
position = 0
score = 1000
screen = 1
def setup():
    global img
    global store
    global twoplayers
    global threeplayers
    global fourplayers
    global fiveplayers
    global sixplayers
    global player
    global achtergrond
    

    img = loadImage('Scoreachtergrond.png')
    store = loadImage('store.png')
    twoplayers = loadImage('twoplayers.PNG')
    threeplayers = loadImage('threeplayers.png')
    fourplayers = loadImage('fourplayers.png')
    fiveplayers = loadImage('fiveplayers.png')
    sixplayers = loadImage('sixplayers.png')
    store = loadImage('store.png')
    achtergrond = loadImage('speelbord alfa 0.002.png')
    size(1366, 768)

def draw():
    global screen
    global store
    global twoplayers
    global threeplayers
    global fourplayers
    global players
    global screen
    global fiveplayers
    global sixplayers
    global store
    

    rect(100, 150, 200, 200)
    rect(400, 150, 200, 200)
    rect(700, 150, 200, 200)
    rect(250, 400, 200, 200)
    rect(550, 400, 200, 200)
    image(twoplayers, 110, 160, 180, 180)
    image(threeplayers, 410, 160, 180, 180)
    image(fourplayers, 710, 160, 180, 180)
    image(fiveplayers, 260, 410, 180, 180)
    image(sixplayers, 560, 410, 180, 180)


    if screen == 2:
        background(achtergrond)
        if players == 2 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score), 150, 640)
            text('Position: ' + str(position), 150, 650)
        elif players == 3 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
        
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score), 270, 640)
            text('Position: ' + str(position), 270, 650)
        elif players == 4 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score), 400, 640)
            text('Position: ' + str(position), 400, 650)
        elif players == 5 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            image(img, 510, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score), 400, 640)
            text('Position: ' + str(position), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score), 520, 640)
            text('Position: ' + str(position), 520, 650)
        elif players == 6 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            image(img, 510, 600, 100, 100)
            image(img, 630, 600, 100, 100) 
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score), 400, 640)
            text('Position: ' + str(position), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score), 520, 640)
            text('Position: ' + str(position), 520, 650)
            text('Player 6 ', 640, 620)
            text('Score: ' + str(score), 640, 640)
            text('Position: ' + str(position), 640, 650)

            
    if screen == 3:
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 100, 970, 658) 
        fill(255,255,255)
        textSize(55)
        text('Inventory', 40, 80)
        fill(255,255,255)
        rect(40, 180, 600, 550)
        textSize(32)
        fill(255,255,255)
        text('Player ' + str(player) , 40, 150)
        image(store, 890, 5, 100, 100)
        text('Return', 870, 150)
    
    if screen == 4:
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 100, 970, 658) 
        fill(255,255,255)
        textSize(32)
        text('Player ' +str(player), 20, 40 )
        text('Score ' + str(score), 20, 70)
        text('Return', 870, 150)
        image(img, 650, 180, 100, 100)
        textSize(12)
        text('Item 1', 655, 195)
        text('Price = 200', 655, 205)
        fill(255,255,255)
        rect(40, 180, 600, 550)


def mousePressed():
    global screen
    global players
    global player
    global score
    global Bought
    if screen == 1 and 100 < mouseX < 300 and 160 < mouseY < 360:
        screen = 2
        players = 2
    if screen == 1 and 400 < mouseX < 600 and 160 < mouseY < 360:
        screen = 2
        players = 3
    if screen == 1 and 700 < mouseX < 900 and 160 < mouseY < 360:
        screen = 2
        players = 4
    if screen == 1 and 250 < mouseX < 450 and 400 < mouseY < 600:
        screen = 2
        players = 5
    if screen == 1 and 550 < mouseX < 750 and 400 < mouseY < 600:
        screen = 2
        players = 6

        
    if screen == 2 and 20 < mouseX < 120 and 600 < mouseY < 700:
        screen = 3
        player = 1
        
    if screen == 2 and 140 < mouseX < 240 and 600 < mouseY < 700:
        screen = 3
        player = 2

    if screen == 2 and 260 < mouseX < 360 and 600 < mouseY < 700:
        screen = 3
        player = 3
 
    if screen == 2 and 390 < mouseX < 490 and 600 < mouseY < 700:
        screen = 3
        player = 4

    if screen == 2 and 510 < mouseX < 610 and 600 < mouseY < 700:
        screen = 3 
        player = 5

        
    if screen == 2 and 630 < mouseX < 730 and 600 < mouseY < 700:
        screen = 3
        player = 6

    if screen == 3 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 2
        textSize(12)
    if screen == 3 and 900 < mouseX < 970 and 10 < mouseY < 100:
        screen = 4
        
    if screen == 4 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 3
    if score > 0:  
        if screen == 4 and 650 < mouseX < 750 and 180 < mouseY < 280:
            score -= 200

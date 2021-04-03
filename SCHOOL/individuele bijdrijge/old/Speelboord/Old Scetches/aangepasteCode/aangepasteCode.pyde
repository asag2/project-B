img= ''
players = 0
position = 0
score1 = 0
score2 = 1
score3 = 2
score4 = 3
score5 = 4
score6 = 5
screen = 1
def setup():
    global img
    global store
    global twoplayers
    global threeplayers
    global fourplayers
    global fiveplayers
    global sixplayers
    
    img = loadImage('Scoreachtergrond.png')
    store = loadImage('store.png')
    twoplayers = loadImage('twoplayers.PNG')
    threeplayers = loadImage('threeplayers.png')
    fourplayers = loadImage('fourplayers.png')
    fiveplayers = loadImage('fiveplayers.png')
    sixplayers = loadImage('sixplayers.png')
    store = loadImage('store.png')
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
    
    background(0)
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
        background(255,255,255)
        if players == 1:
            fill(0, 0, 0)
            text('This game is best played in a group, please invite your friends and have fun playing :)', 10, 150 )
        elif players == 2 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score1), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position), 150, 650)
        elif players == 3 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
        
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score1), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position), 270, 650)
        elif players == 4 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score1), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position), 400, 650)
        elif players == 5 :
            image(img, 20 , 600, 100, 100)
            image(img, 140, 600, 100, 100)
            image(img, 260, 600, 100, 100)
            image(img, 390, 600, 100, 100)
            image(img, 510, 600, 100, 100)
            
            fill(0, 0, 0)
            text('Player 1 ', 30, 620)
            text('Score: ' + str(score1), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score5), 520, 640)
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
            text('Score: ' + str(score1), 30, 640)
            text('Position: ' + str(position), 30, 650)
            text('Player 2 ', 150, 620)
            text('Score: ' + str(score2), 150, 640)
            text('Position: ' + str(position), 150, 650)
            text('Player 3 ', 270, 620)
            text('Score: ' + str(score3), 270, 640)
            text('Position: ' + str(position), 270, 650)
            text('Player 4 ', 400, 620)
            text('Score: ' + str(score4), 400, 640)
            text('Position: ' + str(position), 400, 650)
            text('Player 5 ', 520, 620)
            text('Score: ' + str(score5), 520, 640)
            text('Position: ' + str(position), 520, 650)
            text('Player 6 ', 640, 620)
            text('Score: ' + str(score6), 640, 640)
            text('Position: ' + str(position), 640, 650)
        
        elif players > 6:
            fill(0, 0, 0)
            text('This game was designed with a maximum of 6 players in mind.', 10, 150 )
            
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
        text('Player ' , 40, 150)
        image(store, 890, 5, 100, 100)

def mousePressed():
    global screen
    global players
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
        
    if screen == 2 and 140 < mouseX < 240 and 600 < mouseY < 700:
        screen = 3

    if screen == 2 and 260 < mouseX < 360 and 600 < mouseY < 700:
        screen = 3
 
    if screen == 2 and 390 < mouseX < 490 and 600 < mouseY < 700:
        screen = 3

    if screen == 2 and 510 < mouseX < 610 and 600 < mouseY < 700:
        screen = 3
        
    if screen == 2 and 630 < mouseX < 730 and 600 < mouseY < 700:
        screen = 3

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

#Game board
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

#inventory scetch
    if screen == 3:
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
#buy menu scetch
    if screen == 4:
        fill(0)
        rect(0,0, 1000, 800)
        fill(169,169,169)
        rect(15, 100, 970, 658) 
        fill(255,255,255)
        textSize(32)
        text('Player ' +str(player), 40, 140 )
        text('Score ' + str(score), 40, 170)
        text('Return', 870, 150)
        fill(255,255,255)
        rect(40, 190, 600, 550)
        textSize(42)
        text('Buy menu', 40, 80)
        textSize(12)
        
#coördinaten kaarten buy menu
        image(img, 650, 200, 100, 100)
        text('Item 1', 655, 215)
        text('Price = 200', 655, 235)
#item 2
        image(img, 850, 200, 100, 100)
        text('Item 2', 855, 215)
        text('Price = 200', 855, 235)
#item 3
        image(img, 650, 340, 100, 100)
        text('Item 3', 655, 355)
        text('Price = 250', 655, 365)
#item 4
        image(img, 850, 340, 100, 100)
        text('Item 4', 855, 355)
        text('Price = 500', 855, 365)
#item 5
        image(img, 650, 480, 100, 100)
        text('Item 5', 655, 495)
        text('Price = 400', 655, 505)
#item 6
        image(img, 850, 480, 100, 100)
        text('Item 6', 855, 495)
        text('Price = 400', 855, 505)
#item 7
        image(img, 650, 620, 100, 100)
        text('Item 7', 655, 635)
        text('Price = 400', 655, 645)
#item 8
        image(img, 850, 620, 100, 100)
        text('Item 8', 855, 635)
        text('Price = 600', 855, 645)

def mousePressed():
    global screen
    global players
    global player
    global score

#Choose Players
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

#Choosing whitch inventory to open
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

#Return button
    if screen == 3 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 2
        textSize(12)
#Open buy menu
    if screen == 3 and 900 < mouseX < 970 and 10 < mouseY < 100:
        screen = 4
#Return button
    if screen == 4 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 3

#Score deduction
    if score > 0:  
        if screen == 4 and 650 < mouseX < 750 and 180 < mouseY < 280:
            score -= 200
            

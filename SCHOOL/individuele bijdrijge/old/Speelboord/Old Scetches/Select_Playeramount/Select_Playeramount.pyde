screen = 1
playeramount = 0

def setup():
    global twoplayers
    global threeplayers
    global fourplayers
    global fiveplayers
    global sixplayers
    size(1000, 800)
    twoplayers = loadImage('twoplayers.PNG')
    threeplayers = loadImage('threeplayers.png')
    fourplayers = loadImage('fourplayers.png')
    fiveplayers = loadImage('fiveplayers.png')
    sixplayers = loadImage('sixplayers.png')
    
    
# dit is de beginscherm waar je kan kiezen met hoeveel spelers je speelt

def draw():
    global twoplayers
    global threeplayers
    global fourplayers
    global fiveplayers
    global sixplayers
    global playeramount
    global screen
    
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
    
# dit is de code voor wanneer je klikt op de vierkant dat je dan verder gaat naar het volgende scherm
# screen 2 zou dan het bordspel bijvoorbeeld kunnen zijn en met de playeramount kunnen we bepalen hoeveel spelers er zijn
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
    if screen == 1 and 250 < mouseX < 450 and 400 < mouseY < 600:
        screen = 2
        playeramount = 5
    if screen == 1 and 550 < mouseX < 750 and 400 < mouseY < 600:
        screen = 2
        playeramount = 6

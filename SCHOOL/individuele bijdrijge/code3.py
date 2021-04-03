############# information on items ---- ayub    
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
        text('information about item 1', 200, 190)
        image(img, 500, 100, 100, 100)
        text('Item2', 510, 120)
        text('information about item 2', 600, 190)
        image(img, 100, 210, 100, 100)
        text('Item3', 110, 230)
        text('information about item 3', 200, 300)
        image(img, 500, 210, 100, 100)
        text('Item4', 510, 230)
        text('information about item 4', 600, 300)
        image(img, 100, 320, 100, 100)
        text('Item5', 110, 340)
        text('information about item 5', 200, 400)
        image(img, 500, 320, 100, 100)
        text('Item6', 510, 340)
        text('information about item 6', 600, 400)
        image(img, 100, 430, 100, 100)
        text('Item7', 110, 450)
        text('information about item 7', 200, 510)
        image(img, 500, 430, 100, 100)
        text('Item8', 510, 450)
        text('information about item 8', 600, 510)      
    
        
def mousePressed():
    global screen, players, playerInventory, score, inventoryDict, player, score2, score3, score4, score5, score6


##################Return button---- Ayub
    if screen == 3 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 2
        textSize(12)
    if screen == 5 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 4
        
#####################Open buy menu
    if screen == 3 and 900 < mouseX < 970 and 10 < mouseY < 100:
        screen = 4
#####################Return button
    if screen == 4 and 870 < mouseX < 980 and 80 < mouseY < 150:
        screen = 3
####################to screen 5 400, 150
    if screen == 4 and 400 < mouseX < 580 and 100 < mouseY < 170:
        screen = 5

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
        
        
#################coordinates of items in buy menu---- Ayub
        image(img, 650, 200, 100, 100)
        text('Item 1', 655, 215)
        text('Price = 200', 655, 235)
############item 2
        image(img, 850, 200, 100, 100)
        text('Item 2', 855, 215)
        text('Price = 200', 855, 235)
###############item 3
        image(img, 650, 340, 100, 100)
        text('Item 3', 655, 355)
        text('Price = 250', 655, 365)
############item 4
        image(img, 850, 340, 100, 100)
        text('Item 4', 855, 355)
        text('Price = 500', 855, 365)
############item 5
        image(img, 650, 480, 100, 100)
        text('Item 5', 655, 495)
        text('Price = 400', 655, 505)
##############item 6
        image(img, 850, 480, 100, 100)
        text('Item 6', 855, 495)
        text('Price = 400', 855, 505)
##############item 7
        image(img, 650, 620, 100, 100)
        text('Item 7', 655, 635)
        text('Price = 400', 655, 645)
##############item 8
        image(img, 850, 620, 100, 100)
        text('Item 8', 855, 635)
        text('Price = 600', 855, 645)
            
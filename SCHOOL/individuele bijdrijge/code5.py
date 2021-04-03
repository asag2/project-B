if players == 2:
    Achtergrondwinscreen = loadImage("Achtergrondwinscreen2p.png")
elif players == 3:
    Achtergrondwinscreen = loadImage("Achtergrondwinscreen3p.png")
elif players == 4:
    Achtergrondwinscreen = loadImage("Achtergrondwinscreen4p.png")
elif players == 5:
    Achtergrondwinscreen = loadImage("Achtergrondwinscreen5p.png")
elif players == 6: 
     Achtergrondwinscreen = loadImage("Achtergrondwinscreen6p.png")

elif screen == 2:
    background(Achtergrondwinscreen)





elif screen == 6:
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
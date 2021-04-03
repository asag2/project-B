'''
dit is speelbord009, wat we nu hebben is :
een achtergrond
een track
coordinaten van de tegeltjes
een gans op het bord
je kan de gans besturen met WASD en 1-6
(er is ook nog een versie met een tweede gans die kan bewegen maar die hebben we nu nog niet nodig)

    
    
'''


#dit zijn de coordinaten van de eerste gans. deze worden met WASD bewogen om de gans te laten lopen
posX = 80
posY = 44
grid = True

#dit is de hoeveelheid pixels die één stap naar een andere tegel nodig heeft, om precies in het midden te komen.
# met meer of minder tegels loopt ie uiteindelijk schuin

stapje = 33


# initial setup met de resolutie van 1366 x 768
# het laadt een achtergrond en een gans spelertje in

def setup():
    size(1366,768)
    global speelbord
    global gans1
    speelbord = loadImage("speelbord alfa 0.002.png")
    gans1 = loadImage("gansje3.png")
    

# de draw waarmee je de afbeeldingen daadwerkelijk toont
def draw(): 
    global posX, posY, grid
    image(speelbord,0,0)
    


    image(gans1,posX, posY)
    
    
    # dit zijn parameters voor het grid met coordinaten
    fill(0,0,0)
    breedte = 36
    hoogte = 12
    
    col = 0
    row = 0
    
    
    # met "c" toon of verberg je het grid, kijk maar bij de key bindings
    if grid:
        
        while col < breedte: 
            fill(0,0,0)
            row = 0
            while row < hoogte: 
            
                text(str(col)+","+str(row), 80+(stapje * col), 60+(stapje * row))
                row += 1
            
            col += 1
        
        


    
    
        

            

# dit zijn alle keybindings
def keyPressed():
    global posX, posY, grid
    if key == 'w':
        posY -= stapje
    if key == 'd':
        posX += stapje
    elif key == 's':
        posY += stapje
    elif key == 'a':
        posX -= stapje
        
    
    # met "c" toon of verberg je het grid
    if key == "c":
        grid = not grid    
        
    # met deze keys laat je de gans x aantal stappen doen om de effectiviteit van movement te testen
    # verder nog niet heel nuttig
    if key == "1":
        posX += stapje * 1
    if key == "2":
        posX += stapje * 2
    if key == "3": 
        posX += stapje * 3
    if key == "4":
        posX += stapje * 4
    if key == "5":
        posX += stapje * 5
    if key == "6":
        posX += stapje * 6
        
        
    if key == "v":
        # hier komt de dobbelsteen dat ie ook de bocht om kan enzo maar ik heb nog geen idee hoe
        dobbel = int(random(1,7))
        print(dobbel)
        pass

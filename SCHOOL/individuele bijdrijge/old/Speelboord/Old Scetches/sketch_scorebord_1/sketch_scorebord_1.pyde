img= ''
players = 6
position = 0
score1 = 0
score2 = 1
score3 = 2
score4 = 3
score5 = 4
score6 = 5
def setup():
    global img
    img = loadImage('Scoreachtergrond.png')
    size(750, 300)
    background(255, 255, 255)

def draw():
    if players == 1:
        fill(0, 0, 0)
        text('This game is best played in a group, please invite your friends and have fun playing :)', 10, 150 )
    elif players == 2 :
      image(img, 150 , 100, 100, 100)
      image(img, 500, 100, 100, 100)
      
      fill(0, 0, 0)
      text('Player 1 ', 160, 120)
      text('Score: ' + str(score1), 160, 140)
      text('Position: ' + str(position), 160, 150)
      text('Player 2 ', 510, 120)
      text('Score: ' + str(score2), 510, 140)
      text('Position: ' + str(position), 510, 150)
    elif players == 3 :
      image(img, 20 , 100, 100, 100)
      image(img, 325, 100, 100, 100)
      image(img, 630, 100, 100, 100)
      
      fill(0, 0, 0)
      text('Player 1 ', 30, 120)
      text('Score: ' + str(score1), 30, 140)
      text('Position: ' + str(position), 30, 150)
      text('Player 2 ', 335, 120)
      text('Score: ' + str(score2), 335, 140)
      text('Position: ' + str(position), 335, 150)
      text('Player 3 ', 640, 120)
      text('Score: ' + str(score3), 640, 140)
      text('Position: ' + str(position), 640, 150)
    elif players == 4 :
      image(img, 20 , 100, 100, 100)
      image(img, 230, 100, 100, 100)
      image(img, 430, 100, 100, 100)
      image(img, 630, 100, 100, 100)
      fill(0, 0, 0)
      text('Player 1 ', 30, 120)
      text('Score: ' + str(score1), 30, 140)
      text('Position: ' + str(position), 30, 150)
      text('Player 2 ', 240, 120)
      text('Score: ' + str(score2), 240, 140)
      text('Position: ' + str(position), 240, 150)
      text('Player 3 ', 440, 120)
      text('Score: ' + str(score3), 440, 140)
      text('Position: ' + str(position), 440, 150)
      text('Player 4 ', 640, 120)
      text('Score: ' + str(score4), 640, 140)
      text('Position: ' + str(position), 640, 150)
    elif players == 5 :
      image(img, 20 , 100, 100, 100)
      image(img, 170, 100, 100, 100)
      image(img, 325, 100, 100, 100)
      image(img, 480, 100, 100, 100)
      image(img, 630, 100, 100, 100)
      
      fill(0, 0, 0)
      text('Player 1 ', 30, 120)
      text('Score: ' + str(score1), 30, 140)
      text('Position: ' + str(position), 30, 150)
      text('Player 2 ', 180, 120)
      text('Score: ' + str(score2), 180, 140)
      text('Position: ' + str(position), 180, 150)
      text('Player 3 ', 335, 120)
      text('Score: ' + str(score3), 335, 140)
      text('Position: ' + str(position), 335, 150)
      text('Player 4 ', 490, 120)
      text('Score: ' + str(score4), 490, 140)
      text('Position: ' + str(position), 490, 150)
      text('Player 5 ', 640, 120)
      text('Score: ' + str(score5), 640, 140)
      text('position: ' + str(position), 640, 150)
    elif players == 6 :
      image(img, 20 , 100, 100, 100)
      image(img, 140, 100, 100, 100)
      image(img, 260, 100, 100, 100)
      image(img, 390, 100, 100, 100)
      image(img, 510, 100, 100, 100)
      image(img, 630, 100, 100, 100) 
      
      fill(0, 0, 0)
      text('Player 1 ', 30, 120)
      text('Score: ' + str(score1), 30, 140)
      text('Position: ' + str(position), 30, 150)
      text('Player 2 ', 150, 120)
      text('Score: ' + str(score2), 150, 140)
      text('Position: ' + str(position), 150, 150)
      text('Player 3 ', 270, 120)
      text('Score: ' + str(score3), 270, 140)
      text('Position: ' + str(position), 270, 150)
      text('Player 4 ', 400, 120)
      text('Score: ' + str(score4), 400, 140)
      text('Position: ' + str(position), 400, 150)
      text('Player 5 ', 520, 120)
      text('Score: ' + str(score5), 520, 140)
      text('Position: ' + str(position), 520, 150)
      text('Player 6 ', 640, 120)
      text('Score: ' + str(score6), 640, 140)
      text('Position: ' + str(position), 640, 150)
    elif players > 6:
        fill(0, 0, 0)
        text('This game was designed with a maximum of 6 players in mind.', 10, 150 )

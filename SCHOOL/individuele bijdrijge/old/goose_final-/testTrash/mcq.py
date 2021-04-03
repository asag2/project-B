from random import randrange
from questions import q1, q2, q3, q4, q5, q6, q7

score = 0

def check(x):
    if x == True:
        fill(0,255,0)
        rect(900,500,400,200)
    elif x == False:
        fill(255,0,0)
        rect(900,500,400,200)
def MCQ():
    global qst
    global y
    stroke(0)
    fill(255,255,0)
    rect(900,500,400,200)
    f = createFont("Arial", 16, True)
    qst = {q1:"a",q2:"b",q3:"b",q4:"c",q5:"d",q6:"d",q7:"a"}
    y = randrange(7)
    vraag = list(qst.keys())[y]
    textFont(f,10)
    fill(0)
    text(vraag,890,450)
    
def keyPressed():
    global qst
    global y
    global score
    if key == ' ':
        MCQ()
    answer = list(qst.values())[y]
    if key == answer:
        check(True)
        score += 1
    elif key == ' ':
        print("next question")
        print(score)
    elif key != answer:
        check(False)
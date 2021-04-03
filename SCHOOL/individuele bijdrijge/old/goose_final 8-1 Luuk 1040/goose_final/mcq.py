from random import randrange
from questions import q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19

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
    qst = {q1:"a",q2:"b",q3:"b",q4:"c",q5:"d",q6:"d",q7:"a",q8:"b",q9:"d",q10:"a",q11:"d",q12:"d",q13:"a",q14:"a",q15:"b",q16:"d",q17:"a",q18:"b",q19:"a"}
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
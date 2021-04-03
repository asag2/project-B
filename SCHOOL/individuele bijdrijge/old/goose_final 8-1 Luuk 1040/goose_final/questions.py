q1 = """Is Python case sensitive when dealing with Identifiers?
a. Yes
b. No
c. Machine Dependent
d. None\n"""

q2 = """Given the following state:
x = 10
y = 5
What is the value bound to x?
a. y
b. 10
c. 5
d. x\n"""

q3 = """Which one of these is floor division?
a. /
b. //
c. %
d. None\n"""

q4 = """What is the output of this 3*1**3?
a. 27
b. 9
c. 3
d. 1\n"""

q5 = """"a"+"bc"=?
a. a
b. bc
c. bca
d. abc\n"""

q6 = """Given the following state:
x = 1
y = 2
What is the value bound to y?
a. 1
b. y
c. The whole state is bound to y
d. 2\n"""

q7 = """Given the following state:
x = 10
y = 5
Which of the following code snippets would change the state to the following state?
x = 1
y = 2
\n
a. x = 1  | y = 2
b. x = 2  | y = 1
c. x = 10 | y = 5
d. y = 1  | y = 2\n"""

q8 = """Consider the following code snippet:
x = 0
while x < 10:
  x = x + 1
How many times will the body of the loop be executed?
\n
a. 11 times
b. 10 times
c. 9 times
d. Once\n"""
 
q9 = """Consider the following code snippet:
x = 10
while x > 0:
  x = x + 1
How many times will the body of the loop be executed?
\n
a. It will never be executed
b. 10 times
c. Once
d. An infinite amount of times\n"""
 
q10 = """Given an initial empty state,
what is the value bound to s in the state
after the following code has been executed?
stars = 4
s = ''
while stars > 0:
    s = s + '*\n'
    stars = stars - 1
\n
a. '*\n*\n*\n*\n'
b. '*\n*\n*\n'
c. '****'
d. '*****'\n"""
 
q11 = """Given an initial empty state, 
what does the state look like after executing the following code?
x = 2
s = ''
while x < 13:
  if x >= 6:
    s = s + '*'
  x = x + 2
\n
a. x = 13 | s = '****'
b. x = 14 | s = '******'
c. x = 14 | s = '************'
d. x = 14 | s = '***'\n""" 
 
q12 = """Consider the following code snippet:
i = 0
while i < 2:
    j = 0
    while j < 3:
        j = j + 1
    i = i + 1
How many times will the body of the outer loop be executed?
In other words, how many times will the line of code i = i + 1 be executed?
\n
a. 6
b. 3
c. 5
d. 2\n"""
 
q13 = """Consider the following code snippet:
i = 0
while i < 2:
    j = 0
    while j < 3:
        j = j + 1
    i = i + 1
How many times will the body of the inner loop be executed?
In other words, how many times will the line of code j = j + 1 be executed?
\n
a. 6
b. 2
c. 5
d. 3\n"""
 
q14 = """Given an initial empty state:
n = 2
s = ''
while n > 0:
    s = s + 'Ha\n'
    n = n - 1
what is the value bound to s in the state after the following code has been executed?
\n
a. 'Ha\nHa\n'
b. 'Ha Ha'
c. 'Ha\nHa\nHa\n'
d. 'Ha Ha Ha'\n"""
 
q15 = """Given an initial empty state:
x = 1 + 6
what is the value bound to x in the state after the following code has been executed?
\n
a. 1
b. 7
c. 6
d. x\n"""
 
q16 = """Given the following expression:
3 + 2 * 5
What is the resulting expression after ONE step of evaluation?
\n
a. 2
b. 5 * 5
c. 13
d. 3 + 10\n"""
 
q17 = """Given an initial empty state:
x = 2 + 3 * 3
what is the value bound to x in the state after the following code has been executed?
\n 
a. 11
b. 18
c. 8
d. 15\n"""
 
q18 = """Given the following expression:
(3 + 2) * 5
What is the resulting expression after ONE step of evaluation?
\n
a. 13
b. 5 * 5
c. 3 + 10
d. 25\n"""
 
q19 = """Given the following expression:
3 * 2 + 10 * 5 - 3
What is the resulting expression after ONE step of evaluation?
\n
a. 6 + 10 * 5 - 3
b. 3 * 2 + 50 - 3
c. 6 + 50 - 3
d. 53\n"""
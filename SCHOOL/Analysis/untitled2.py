# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 23:21:08 2021

@author: ayubs
"""

n = input()
result = 'ERROR'
dot= '.'
cNumber = 0
multi = 10
dotCheck = False
iSBN = ''
multiStore = False
cDigitCheck = False
if len(n) == 10 and dot not in n:
    if n[-1] == 'X':
        cDigit = 10
    else:
        cDigit = int(n) % 10 
    n = n[:-1]
    for i in n:
        cNumber = cNumber + int(i) * multi
        multi -= 1
    if cDigit == (11 - cNumber % 11):
        result = 'VALID'
    else:
        result = 'INVALID'
elif len(n) == 10 and dot in n:
    if n[-1] == 'X':
        cDigit = 10
    elif n[-1] != '.':
        cDigit = int(n[-1])
    nUgh = n[:-1]
    for i in nUgh:
        if i == dot:
            multiStore = multi
            i = '0'
        iSBN = iSBN + i
        cNumber = cNumber + int(i) * multi
        multi -= 1
    x = 0
    if multiStore == False:
        while cDigitCheck == False:
            if x == (11 - cNumber % 11):
                cDigitCheck = True
                result = x
                if x == 10:
                    result = 'X'
            x += 1
    else:
        while dotCheck == False:
            cNumberDot = multiStore * x + cNumber
            if cDigit == (11 - cNumberDot % 11):
                dotCheck = True
                result = x
                if x == 10:
                    result = 'X'
            x += 1
            
else:
    result = 'INPUT ERROR'
print(result)
    if screen == 3 and mouseOnItem1() == True:
        if player == 1:
            if inventoryDict['item1'] > 0: 
                inventoryDict['item1'] -= 1
        elif player == 2:
            if inventoryDict2['item1'] > 0: 
                inventoryDict2['item1'] -= 1
        elif player == 3:
            if inventoryDict3['item1'] > 0: 
                inventoryDict3['item1'] -= 1
        elif player == 4:
            if inventoryDict4['item1'] > 0: 
                inventoryDict4['item1'] -= 1
        elif player == 5:
            if inventoryDict5['item1'] > 0: 
                inventoryDict5['item1'] -= 1
        elif player == 6:
            if inventoryDict6['item1'] > 0: 
                inventoryDict6['item1'] -= 1
                    
    elif screen == 3 and mouseOnItem2() == True:
        if player == 1:
            if inventoryDict['item2'] > 0: 
                inventoryDict['item2'] -= 1
        elif player == 2:
            if inventoryDict2['item2'] > 0: 
                inventoryDict2['item2'] -= 1
        elif player == 3:
            if inventoryDict3['item2'] > 0: 
                inventoryDict3['item2'] -= 1
        elif player == 4:
            if inventoryDict4['item2'] > 0: 
                inventoryDict4['item2'] -= 1
        elif player == 5:
            if inventoryDict5['item2'] > 0: 
                inventoryDict5['item2'] -= 1
        elif player == 6:
            if inventoryDict6['item2'] > 0: 
                inventoryDict6['item2'] -= 1
                
    elif screen == 3 and mouseOnItem3() == True:
        if player == 1:
            if inventoryDict['item3'] > 0: 
                inventoryDict['item3'] -= 1
        elif player == 2:
            if inventoryDict2['item3'] > 0: 
                inventoryDict2['item3'] -= 1
        elif player == 3:
            if inventoryDict3['item3'] > 0: 
                inventoryDict3['item3'] -= 1
        elif player == 4:
            if inventoryDict4['item3'] > 0: 
                inventoryDict4['item3'] -= 1
        elif player == 5:
            if inventoryDict5['item3'] > 0: 
                inventoryDict5['item3'] -= 1
        elif player == 6:
            if inventoryDict6['item3'] > 0: 
                inventoryDict6['item3'] -= 1
                
    elif screen == 3 and mouseOnItem4() == True:
        if player == 1:
            if inventoryDict['item4'] > 0: 
                inventoryDict['item4'] -= 1
        elif player == 2:
            if inventoryDict2['item4'] > 0: 
                inventoryDict2['item4'] -= 1
        elif player == 3:
            if inventoryDict3['item4'] > 0: 
                inventoryDict3['item4'] -= 1
        elif player == 4:
            if inventoryDict4['item4'] > 0: 
                inventoryDict4['item4'] -= 1
        elif player == 5:
            if inventoryDict5['item4'] > 0: 
                inventoryDict5['item4'] -= 1
        elif player == 6:
            if inventoryDict6['item4'] > 0: 
                inventoryDict6['item4'] -= 1
                
    elif screen == 3 and mouseOnItem5() == True:
        if player == 1:
            if inventoryDict['item5'] > 0: 
                inventoryDict['item5'] -= 1
        elif player == 2:
            if inventoryDict2['item5'] > 0: 
                inventoryDict2['item5'] -= 1
        elif player == 3:
            if inventoryDict3['item5'] > 0: 
                inventoryDict3['item5'] -= 1
        elif player == 4:
            if inventoryDict4['item5'] > 0: 
                inventoryDict4['item5'] -= 1
        elif player == 5:
            if inventoryDict5['item5'] > 0: 
                inventoryDict5['item5'] -= 1
        elif player == 6:
            if inventoryDict6['item5'] > 0: 
                inventoryDict6['item5'] -= 1

    elif screen == 3 and mouseOnItem6() == True:
        if player == 1:
            if inventoryDict['item6'] > 0: 
                inventoryDict['item6'] -= 1
        elif player == 2:
            if inventoryDict2['item6'] > 0: 
                inventoryDict2['item6'] -= 1
        elif player == 3:
            if inventoryDict3['item6'] > 0: 
                inventoryDict3['item6'] -= 1
        elif player == 4:
            if inventoryDict4['item6'] > 0: 
                inventoryDict4['item6'] -= 1
        elif player == 5:
            if inventoryDict5['item6'] > 0: 
                inventoryDict5['item6'] -= 1
        elif player == 6:
            if inventoryDict6['item6'] > 0: 
                inventoryDict6['item6'] -= 1

    elif screen == 3 and mouseOnItem7() == True:
        if player == 1:
            if inventoryDict['item7'] > 0: 
                inventoryDict['item7'] -= 1
        elif player == 2:
            if inventoryDict2['item7'] > 0: 
                inventoryDict2['item7'] -= 1
        elif player == 3:
            if inventoryDict3['item7'] > 0: 
                inventoryDict3['item7'] -= 1
        elif player == 4:
            if inventoryDict4['item7'] > 0: 
                inventoryDict4['item7'] -= 1
        elif player == 5:
            if inventoryDict5['item7'] > 0: 
                inventoryDict5['item7'] -= 1
        elif player == 6:
            if inventoryDict6['item7'] > 0: 
                inventoryDict6['item7'] -= 1 
                
    elif screen == 3 and mouseOnItem8() == True:
        if player == 1:
            if inventoryDict['item8'] > 0: 
                inventoryDict['item8'] -= 1
        elif player == 2:
            if inventoryDict2['item8'] > 0: 
                inventoryDict2['item8'] -= 1
        elif player == 3:
            if inventoryDict3['item8'] > 0: 
                inventoryDict3['item8'] -= 1
        elif player == 4:
            if inventoryDict4['item8'] > 0: 
                inventoryDict4['item8'] -= 1
        elif player == 5:
            if inventoryDict5['item8'] > 0: 
                inventoryDict5['item8'] -= 1
        elif player == 6:
            if inventoryDict6['item8'] > 0: 
                inventoryDict6['item8'] -= 1

    
    
######### Mouse on item in inventory ----- ayub
def mouseOnItem1():
    global screen, players, playerInventory, score, inventoryDict, player, allItems
    if 100 < mouseX < 200 and 200 < mouseY < 300:
        return True
    else: 
        return False 
def mouseOnItem2():
    if 400 < mouseX < 500 and 200 < mouseY < 300:
        return True
    else: 
        return False 
def mouseOnItem3():
    if 100 < mouseX < 200 and 340 < mouseY < 440:
        return True
    else: 
        return False 
def mouseOnItem4():
    if 400 < mouseX < 500 and 340 < mouseY < 440:
        return True
    else: 
        return False 
def mouseOnItem5():
    if 100 < mouseX < 200 and 480 < mouseY < 580:
        return True
    else: 
        return False 
def mouseOnItem6():
    if 400 < mouseX < 500 and 480 < mouseY < 580:
        return True
    else: 
        return False 
def mouseOnItem7():
    if 100 < mouseX < 200 and 620 < mouseY < 720:
        return True
    else: 
        return False 
def mouseOnItem8():
    if 400 < mouseX < 500 and 620 < mouseY < 720:
        return True
    else: 
        return False 
    
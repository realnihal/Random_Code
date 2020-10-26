### Rock, Paper, Scissors Game
### Nihal
### 16-16-2020

import random
def getval():
    values = ['R','P','S']
    output = values[random.randint(0,2)]
    return output
print("Welcome to Rock, Paper, Scissors Game")
yourScore = 0
compScore = 0
while (yourScore < 5) and (compScore < 5):
    play = input("Enter your value 'R','P','S' : ")
    comp = getval()
    if play == 'R':
        if comp == 'S':
            print("Computer plays S, you get a point")
            yourScore += 1
            continue
        elif comp == 'P':
            print("Computer plays P, comp gets a point")
            compScore += 1
            continue
        else:
            print("Computer also plays R")
            continue
    elif play == 'P':
        if comp == 'S':
            print("Computer plays S, comp gets a point")
            compScore += 1
            continue
        elif comp == 'R':
            print("Computer plays R, you get a point")
            yourScore += 1
            continue
        else:
            print("Computer also plays P")
            continue
    elif play == 'S':
        if comp == 'R':
            print("Computer plays R, comp gets a point")
            compScore += 1
            continue
        elif comp == 'P':
            print("Computer plays P, you get a point")
            yourScore += 1
            continue
        else:
            print("Computer also plays S")
            continue
    else:
        print("check syntax")
if(compScore > yourScore):
    print("GAME OVER")
    print("your score: " + str(yourScore) + "\ncomp score:" + str(compScore) )
else:
    print("you won the game")
    print("your score: " + str(yourScore) + "\ncomp score: " + str(compScore) ) 
input()
            
